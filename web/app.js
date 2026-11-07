const $ = (id) => document.getElementById(id);
const escape = (value = '') => String(value).replace(/[&<>"']/g, (character) =>
  ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'})[character]);
const storageKey = 'is5312-learning-lab-v1';
const initialState = () => ({version: 1, week: 1, lesson: {}, visited: {}, drafts: {}, records: {}, exams: {}});
let state;
try { state = JSON.parse(localStorage.getItem(storageKey)) || initialState(); }
catch { state = initialState(); }
const save = () => localStorage.setItem(storageKey, JSON.stringify(state));

async function api(action, data) {
  const response = await fetch('/api/' + action, data === undefined ? {} : {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    const failure = await response.json().catch(() => ({}));
    throw new Error(failure.error || '本地 Python 服务暂不可用。');
  }
  return response.json();
}

let course;
try { course = await api('course'); }
catch (error) {
  $('content').textContent = error.message;
  throw error;
}

const questions = Object.fromEntries(
  [...course.weeks.flatMap((week) => [...week.practice, ...week.exam]), ...course.mock].map((question) => [question.id, question])
);
const filters = ['全部', '必做', '独立编写', '预测输出', '调试', '补全', '综合补练'];
let view = state.resume?.view || 'study';
let activeQuestion = state.resume?.question || '';
let activeExam = state.resume?.exam || '';
let practiceFilter = state.resume?.filter || '全部';
let errorReviewIds = state.resume?.errorReviewIds || [];
let panel = null;
let feedback = new Map();
let hints = new Map();
let hintLevels = new Map();
const week = () => course.weeks[state.week - 1];
const allLessons = course.weeks.flatMap((item) => item.lessons);
const lesson = () => week().lessons.find((item) => item.id === state.lesson[state.week]) || week().lessons[0];
const pad = (number) => String(number).padStart(2, '0');
const examName = (id) => id === 'mock' ? '第 1–9 周综合上机模拟' : '第 ' + Number(id.slice(5)) + ' 周测';
const examQuestions = (id) => id === 'mock' ? course.mock : course.weeks[Number(id.slice(5)) - 1].exam;
const record = (id) => state.records[id] || {attempts: 0};
const related = (first, second) => first.id !== second.id && (
  first.topic ? first.topic === second.topic && !(
    (['独立编写', '补全'].includes(first.mode) && ['独立编写', '补全'].includes(second.mode) && !first.exam && !second.exam) ||
    (['预测输出', '调试'].includes(first.mode) && ['预测输出', '调试'].includes(second.mode))
  ) : first.week === second.week
);
const currentExam = () => state.exams[activeExam];

function mode(next) {
  view = next;
  activeQuestion = '';
  activeExam = '';
  render();
}

function selectWeek(number) {
  state.week = number;
  activeQuestion = '';
  activeExam = '';
  practiceFilter = '全部';
  if (view === 'errors') view = 'study';
  save();
  render();
}

function openQuestion(id, fromErrors = false) {
  const question = questions[id];
  if (fromErrors && (view !== 'errors' || !activeQuestion)) {
    errorReviewIds = unresolvedErrors().map(([key]) => key).filter(canReviewError);
  }
  state.week = question.week;
  activeQuestion = id;
  activeExam = question.exam;
  view = fromErrors ? 'errors' : question.exam ? 'exam' : 'practice';
  if (view === 'practice' && !filteredPracticeItems().includes(question)) practiceFilter = '全部';
  const entries = fromErrors ? unresolvedErrors().map(([key]) => questions[key])
    : question.exam ? examQuestions(question.exam) : filteredPracticeItems();
  const index = entries.indexOf(question);
  if (index >= 0) (state.listPages ??= {})[listKey()] = Math.floor(index / listPageSize);
  render();
}

function sidebar() {
  const completed = allLessons.filter((item) => state.visited[item.id]).length;
  $('sidebar').innerHTML = `
    <div class="sidebar-head"><strong>课程目录</strong><span class="caption">已运行 ${completed} / ${allLessons.length} 节示例</span>
      <div class="progress" role="progressbar" aria-label="示例完成度" aria-valuemin="0" aria-valuemax="${allLessons.length}" aria-valuenow="${completed}"><i style="--p:${completed / allLessons.length}"></i></div></div>
    <div class="week-list">${course.weeks.map((item, order) => {
      const selected = item.week === state.week;
      const count = item.lessons.filter((entry) => state.visited[entry.id]).length;
      return `<button class="week" data-week="${item.week}" aria-expanded="${selected}" data-done="${count === 6}" style="--i:${order}"><span class="index">${pad(item.week)}</span><span>${item.title}</span><small>${count}/6</small><i class="meter" style="--p:${count / 6}" aria-hidden="true"></i></button>
      ${selected && view === 'study' ? `<div class="lesson-nav">${item.lessons.map((entry, position) =>
        `<button class="lesson-link" data-lesson="${entry.id}" style="--i:${position}" ${entry.id === lesson().id ? 'aria-current="step"' : ''}>${escape(entry.title)}${state.visited[entry.id] ? '<span class="tick" aria-label="已运行"> ✓</span>' : ''}</button>`).join('')}</div>` : ''}
      `;
    }).join('')}</div>
    ${view === 'study' ? `<label class="mobile-lessons">知识点
      <select id="mobile-lesson">${week().lessons.map((entry) =>
        `<option value="${entry.id}" ${entry.id === lesson().id ? 'selected' : ''}>${escape(entry.title)}</option>`).join('')}
      </select></label>` : ''}
    <div class="sidebar-footer caption">Analytical Programming<br>with Python</div>`;
}

const lessonPages = ['概念', '读代码', '动手实验', '练习'];

function updateLessonPage(index) {
  (state.lessonPages ??= {})[lesson().id] = index;
  save();
  $('lesson-page-content').scrollTop = 0;
  $('content').querySelectorAll('[data-lesson-panel]').forEach((section, page) => {
    section.hidden = page !== index;
  });
  $('content').querySelectorAll('[data-lesson-page]').forEach((button, page) => {
    if (page === index) button.setAttribute('aria-current', 'step');
    else button.removeAttribute('aria-current');
  });
  $('lesson-page-count').textContent = `第 ${index + 1} / ${lessonPages.length} 页`;
  $('lesson-page-previous').disabled = index === 0;
  $('lesson-page-next').hidden = index === lessonPages.length - 1;
  if ($('lesson-page-next-unit')) $('lesson-page-next-unit').hidden = index !== lessonPages.length - 1;
}

function study() {
  const item = lesson();
  const number = week().lessons.indexOf(item) + 1;
  const hasNext = number < week().lessons.length || state.week < course.weeks.length;
  const source = week().ppt
    ? `按 ${escape(week().ppt)} 编写的可运行示例`
    : `基于原课程示例 · week${state.week}.py <button data-source="${state.week}">原代码</button><button data-notes="${state.week}">详细讲义</button>`;
  const experiment = item.experiment;
  $('content').innerHTML = `
    <div class="lesson-heading">
      <div class="eyebrow">WEEK ${pad(state.week)} / LESSON ${pad(number)}</div>
      <h1>${escape(item.title)}</h1>
      <nav class="lesson-page-nav" aria-label="本节分页">
        ${lessonPages.map((label, index) => `<button data-lesson-page="${index}">${label}</button>`).join('')}
      </nav>
    </div>
    <div class="lesson-page-content" id="lesson-page-content">
    <section data-lesson-panel>
      <p class="caption">${escape(week().title)} · ${escape(week().description)}</p>
      <p class="lead">${escape(item.goal)}</p>
      <h2>先理解</h2>
      <p>${escape(item.concept)}</p>
      <div class="source">${source}</div>
    </section>
    <section data-lesson-panel hidden>
      <h2>逐行读示例</h2>
      <ol class="lesson-trace">${item.trace.map((step) => `
        <li>
          <span class="caption">第 ${step.lines} 行</span>
          <pre><code>${escape(step.code)}</code></pre>
          <p>${escape(step.explanation)}</p>
        </li>`).join('')}</ol>
      <div class="actions"><button data-example="original">打开原示例</button></div>
      <details><summary>核对原示例输出</summary><pre class="sample">${escape(item.output)}</pre></details>
    </section>
    <section data-lesson-panel hidden>
      <h2>改一处，看看会发生什么</h2>
      <p>${escape(experiment.question)}</p>
      <div class="actions"><button data-example="variation">载入改动后的示例</button></div>
      <details><summary>查看改动与结果</summary>
        <div class="lesson-diff"><span class="caption">改动前</span><pre><code>${escape(experiment.before)}</code></pre>
          <span class="caption">改动后</span><pre><code>${escape(experiment.after)}</code></pre></div>
        <pre class="sample">${escape(experiment.output)}</pre>
        <p class="lesson-result-note">${escape(experiment.why)}</p>
      </details>
      <div class="lesson-section">
        <h2>常见错误</h2>
        <p>${escape(item.pitfall)}</p>
      </div>
    </section>
    <section data-lesson-panel hidden>
      <h2>轮到你</h2>
      <p>可以先做补全熟悉写法，再试独立题。两种模式使用同一任务，想先检验自己时直接选独立编程。</p>
      <div class="actions"><button data-question="${item.id}-fill">先补全一行</button><button class="primary" data-question="${item.id}-write">独立编程</button></div>
      <div class="lesson-section">
        <h2>本周复习</h2>
        <div class="actions"><button data-view="practice">本周 28 道练习</button><button data-exam="week-${state.week}">本周上机测验</button><button data-exam="mock">综合模拟</button></div>
      </div>
    </section>
    </div>
    <nav class="lesson-pagination" aria-label="翻页">
      <button id="lesson-page-previous" data-page-step="-1">← 上一页</button>
      <span id="lesson-page-count" class="caption" role="status"></span>
      <span>
        <button class="primary" id="lesson-page-next" data-page-step="1">下一页 →</button>
        ${hasNext ? '<button class="primary" id="lesson-page-next-unit" data-next hidden>下一小节 →</button>' : ''}
      </span>
    </nav>`;
  updateLessonPage(state.lessonPages?.[item.id] ?? 0);
  showLessonEditor(item);
}

function showLessonEditor(item, variation = false) {
  workspace({
    key: variation ? item.id + ':variation' : item.id,
    lessonId: item.id,
    code: variation ? item.experiment.code : item.code,
    readOnly: false,
    title: variation ? 'experiment.py' : 'lesson.py',
  });
}

const listPageSize = 6;

function listKey() {
  if (view === 'practice') return `practice-${state.week}-${practiceFilter}`;
  if (view === 'exam') return `exam-${activeExam || 'home'}`;
  return 'errors';
}

function pagedList(heading, items, format) {
  const total = Math.max(1, Math.ceil(items.length / listPageSize));
  const page = Math.min(state.listPages?.[listKey()] ?? 0, total - 1);
  const start = page * listPageSize;
  $('content').innerHTML = `
    <div class="lesson-heading">${heading}</div>
    <div class="lesson-page-content">${format(items.slice(start, start + listPageSize), start)}</div>
    ${items.length ? `<nav class="lesson-pagination" aria-label="列表翻页">
      <button data-list-page="${page - 1}" ${page === 0 ? 'disabled' : ''}>← 上一页</button>
      <span class="caption" role="status">第 ${page + 1} / ${total} 页</span>
      <button data-list-page="${page + 1}" ${page === total - 1 ? 'disabled' : ''}>下一页 →</button>
    </nav>` : ''}`;
}

function rows(items, showMode = true, start = 0) {
  return `<div class="question-list" id="question-list">${items.map((question, index) => {
    const entry = question.exam ? state.exams[question.exam]?.results[question.id] : state.records[question.id];
    const status = entry?.total && entry.passed === entry.total ? '通过' : entry?.attempts ? '已做' : question.core && !question.exam ? '必做' : '';
    return `<button class="qrow" data-question="${question.id}" data-status="${status}" style="--i:${index}" ${question.id === activeQuestion ? 'aria-current="step"' : ''}>
      <span class="qindex">${pad(start + index + 1)}</span><span><b>${escape(question.title)}</b>${showMode ? `<br><small>${question.mode} · W${pad(question.week)}</small>` : ''}</span><small>${status}</small>
    </button>`;
  }).join('')}</div>`;
}

function filteredPracticeItems() {
  return week().practice.filter((item) => practiceFilter === '全部' || (practiceFilter === '必做' ? item.core : item.mode === practiceFilter));
}

function practice() {
  if (activeQuestion) return showQuestion(questions[activeQuestion]);
  pagedList(`
    <div class="eyebrow">PRACTICE / WEEK ${pad(state.week)}</div>
    <h1>本周题库</h1>
    <p class="lead">${escape(week().title)} · 28 道随堂及扩展题，另有 6 道周测题。</p>
    <div class="filters">${filters.map((filter) => `<button data-filter="${filter}" aria-pressed="${filter === practiceFilter}">${filter}</button>`).join('')}</div>
  `, filteredPracticeItems(), (items, start) => rows(items, true, start));
  $('workspace').innerHTML = '<div class="eyebrow">PYTHON WORKBENCH</div><h2>从题库选一道题</h2><p class="caption">先跑公开样例，再提交多组测试。</p>';
}

function examHome() {
  if (activeQuestion) return showQuestion(questions[activeQuestion]);
  if (activeExam) {
    const session = currentExam();
    const items = examQuestions(activeExam);
    const score = items.filter((question) => {
      const result = session?.results[question.id];
      return result?.total && result.passed === result.total;
    }).length;
    const started = !!session;
    const finished = session?.finished;
    pagedList(`
      <button class="quiet" data-view="exam">← 测试首页</button>
      <div class="eyebrow">COMPUTER LAB / ${items.length} QUESTIONS</div>
      <h1>${examName(activeExam)}</h1>
      <p class="lead">${finished ? `本次通过 ${score} / ${items.length} 道。点题目回看失败用例和解析。` :
        '题目可跳过和返回。答题期间显示运行错误和通过情况，交卷后开放解析。'}</p>
      <div class="actions">
        ${!started ? '<button class="primary" data-start>开始答题</button>' :
          finished ? '<button data-restart>重新开始一轮</button>' : '<button class="primary" data-finish>交卷并查看解析</button>'}
      </div>`, started ? items : [], (visible, start) => rows(visible, false, start));
  } else {
    pagedList(`
      <div class="eyebrow">COMPUTER LAB</div><h1>上机测试</h1>
      <p class="lead">先做当前周的 6 道独立编程题，或用 9 道全新题练习第 1–9 周综合技能。</p>
      <div class="actions"><button class="primary" data-exam="mock">打开综合模拟</button><button data-exam="week-${state.week}">打开第 ${state.week} 周测</button></div>
      <p class="caption work-section">综合模拟范围依据现有课件编排。正式考试范围待课程公布。</p>`,
      course.weeks, (items) => `<h2>每周测验</h2>
      ${items.map((item, order) => {
        const done = state.exams['week-' + item.week]?.finished;
        return `<button class="qrow" data-exam="week-${item.week}" data-status="${done ? '已交卷' : ''}" style="--i:${order}"><span class="qindex">${pad(item.week)}</span><span>${escape(item.title)}</span><small>${done ? '已交卷' : '6 题'}</small></button>`;
      }).join('')}`);
  }
  $('workspace').innerHTML = '<div class="eyebrow">EXAM MODE</div><h2>独立完成代码</h2><p class="caption">交卷之后可查看参考解法。测试成绩和草稿保存在当前浏览器。</p>';
}

function showQuestion(question) {
  const session = question.exam ? currentExam() : null;
  const finished = !!session?.finished;
  const reviewing = view === 'errors';
  const entries = reviewing ? errorReviewIds.map((id) => questions[id])
    : question.exam ? examQuestions(question.exam) : filteredPracticeItems();
  const index = entries.findIndex((item) => item.id === question.id);
  const result = session ? session.results[question.id] : record(question.id);
  const activeHintLevel = hintLevels.get(question.id);
  const navigation = reviewing ? 'data-error-question' : 'data-question';
  $('content').innerHTML = `
    <div class="lesson-heading">
      <div class="actions">
        <button class="quiet" data-back-question>← ${reviewing ? '错题本' : question.exam ? examName(question.exam) : '本周题库'}</button>
        <button class="lesson-return" data-to-workspace>去代码区</button>
        ${question.exam && !finished ? '<button data-finish>交卷</button>' : ''}
      </div>
      <div class="eyebrow">WEEK ${pad(question.week)} / ${question.mode}${question.core && !question.exam ? ' · 必做' : ''}</div>
      <h1>${escape(question.title)}</h1>
    </div>
    <div class="lesson-page-content">
      <p class="lead">${escape(question.prompt)}</p>
      ${question.signature ? `<pre class="sample">${escape(question.signature)}</pre>${question.week < 5 ? '<p class="caption">第一行已经写好。把代码写在缩进内，用 return 交出结果。第 5 周会系统讲解函数。</p>' : ''}` : ''}
      ${question.samples.length ? `<section class="work-section">
        <h2>公开样例</h2>
        ${!finished ? '<p class="caption">「运行」只检查当前输入。「提交判题」会用题库里的各组输入运行同一段代码，可能包含额外用例。</p>' : ''}
        ${question.samples.map((sample, index) => `<div class="public-example">
          ${question.samples.length > 1 ? `<div class="row"><span class="caption">样例 ${index + 1}</span>
            ${!finished && sample.stdin !== null ? `<button data-sample-input="${index}">载入样例 ${index + 1}</button>` : ''}</div>` : ''}
          <pre class="sample">输入\n${escape(sample.input)}\n\n预期结果\n${escape(sample.expected)}</pre>
        </div>`).join('')}
      </section>` : ''}
      ${!question.exam ? `<section class="work-section" id="hint-panel"><h2>卡住了？</h2>
        <div class="actions">${['思路', '解题步骤', '参考答案'].map((label, lvl) =>
          `<button data-hint="${lvl}" aria-pressed="${activeHintLevel === lvl}">${label}</button>`
        ).join('')}</div><pre id="hint-text" class="hint-text" hidden></pre></section>` : ''}
      ${finished ? `<section class="work-section"><h2>交卷解析</h2>
        <p class="caption">${result?.total ? `本题通过 ${result.passed} / ${result.total} 组` : '本题未提交'}</p>
        <p>${escape(session.review[question.id]?.explanation)}</p>
        <pre class="sample">${escape(session.review[question.id]?.solution)}</pre>
        ${result?.total && result.passed < result.total ? '<button data-review>查看失败用例</button>' : ''}
        <button data-remediate="${question.id}">补练相关知识点</button></section>` : ''}
    </div>
    <nav class="lesson-pagination" aria-label="题目翻页">
      <button ${index > 0 ? `${navigation}="${entries[index - 1].id}"` : 'disabled'}>← 上一题</button>
      <span class="caption" role="status">${index >= 0 ? `第 ${index + 1} / ${entries.length} 题` : ''}</span>
      <button ${index >= 0 && index < entries.length - 1 ? `${navigation}="${entries[index + 1].id}"` : 'disabled'}>下一题 →</button>
    </nav>`;
  workspace({key: question.id, code: question.starter, question, readOnly: finished || question.mode === '预测输出', title: 'exercise.py'});
  if (hints.has(question.id) && !question.exam) {
    $('hint-text').textContent = hints.get(question.id);
    $('hint-text').hidden = false;
  }
}

function unresolvedErrors() {
  return Object.entries(state.records).filter(([id, entry]) => {
    const needsReview = Math.max(entry.failedAt || 0, entry.solutionAt || 0);
    if (!needsReview || !questions[id]) return false;
    return !Object.entries(state.records).some(([other, item]) => questions[other] && item.passingAt > needsReview && related(questions[id], questions[other]));
  }).sort(([, a], [, b]) => Math.max(b.failedAt || 0, b.solutionAt || 0) - Math.max(a.failedAt || 0, a.solutionAt || 0));
}

function canReviewError(id) {
  const exam = questions[id].exam;
  return !exam || state.exams[exam]?.finished;
}

function errors() {
  if (activeQuestion) return showQuestion(questions[activeQuestion]);
  const unresolved = unresolvedErrors();
  pagedList(`<div class="eyebrow">REVIEW LOG</div><h1>错题本</h1>
    <p class="lead">${unresolved.length ? `${unresolved.length} 道题待复测。完成一道相关新题后，原错题会从待复测清单移除。` : '暂时没有待复测的题。提交失败或查看练习参考答案后，题目会出现在这里。'}</p>`,
    unresolved, (items) => items.map(([id, entry]) => `<div class="row review-row"><span><strong>${escape(questions[id].title)}</strong><br><span class="caption">W${pad(questions[id].week)} · ${questions[id].mode} · 提交 ${entry.attempts} 次</span></span>
      <span class="actions">${canReviewError(id) ? `<button data-error-question="${id}">回看</button>` : ''}
      <button data-remediate="${id}">做变式题</button></span></div>`).join(''));
  $('workspace').innerHTML = '<div class="eyebrow">RETRY / RECALL</div><h2>用新题确认掌握</h2><p class="caption">补练会选择同知识点的不同任务，找不到时转到同一周的综合补练。</p>';
}

function workspace(configuration) {
  const {key, code, question, readOnly, title, lessonId} = configuration;
  const session = question?.exam ? currentExam() : null;
  const drafts = session?.drafts || state.drafts;
  const draft = drafts[key] || {};
  const prediction = question?.mode === '预测输出';
  const canEdit = !readOnly;
  const canSubmit = question && !session?.finished;
  const hasInput = !question || (question.kind === 'script' && !prediction);
  panel = configuration;
  $('workspace').innerHTML = `
    <div class="editor-head"><strong>${title} <span class="caption">/ Python</span></strong><div class="editor-actions">
      ${lessonId || question ? `<button class="lesson-return" data-return-to-lesson>${lessonId ? '回到讲解' : '回到题面'}</button>` : ''}
      ${canEdit ? '<button data-reset>还原</button><button data-run>▶ 运行</button>' : ''}
      ${canSubmit ? '<button data-grade class="primary">提交判题</button>' : ''}
    </div></div>
    <div class="editor-frame"><pre class="line-numbers" id="numbers" aria-hidden="true"></pre><textarea id="editor" aria-label="Python 代码" spellcheck="false" autocapitalize="off" autocomplete="off" wrap="off" ${readOnly ? 'readonly' : ''}></textarea></div>
    ${prediction ? '<label class="form-label" for="answer">你预测的完整输出</label><textarea id="answer" class="answer" spellcheck="false" autocomplete="off"></textarea>' : ''}
    ${hasInput ? `<details ${question?.input ? 'open' : ''}><summary>标准输入 stdin</summary><label class="form-label" for="stdin">每行一次 input()${question ? ' · 仅用于「运行」' : ''}</label><textarea id="stdin" class="stdin" rows="2" ${readOnly ? 'readonly' : ''}></textarea></details>` : ''}
    ${question && Object.keys(question.files).length ? `<details><summary>样例文件</summary>${Object.entries(question.files).map(([name, data]) => `<div class="form-label">${escape(name)}</div><pre class="sample">${escape(data)}</pre>`).join('')}</details>` : ''}
    <div class="console"><div class="console-head"><strong>运行结果</strong><span id="status" class="caption" role="status">${canEdit ? '⌘ Enter 运行' : '等待操作'}</span></div>
      <pre id="output" aria-label="程序输出" aria-live="polite">尚未运行。</pre></div>`;
  $('editor').value = draft.code ?? code;
  if ($('answer')) $('answer').value = draft.answer ?? '';
  if ($('stdin')) $('stdin').value = draft.input ?? question?.input ?? '';
  updateNumbers();
  $('editor').addEventListener('scroll', () => { $('numbers').scrollTop = $('editor').scrollTop; });
  refreshFeedback();
}

function updateNumbers() {
  $('numbers').textContent = $('editor').value.split('\n').map((_, index) => index + 1).join('\n');
  $('numbers').scrollTop = $('editor').scrollTop;
}

const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
let firstRender = true;
let renderedPage = '';

function moveNavPill() {
  const pill = document.querySelector('.nav-pill');
  const current = document.querySelector('.top-nav [aria-current="page"]');
  if (!pill) return;
  if (!current) { pill.style.opacity = '0'; return; }
  pill.style.opacity = '1';
  pill.style.width = current.offsetWidth + 'px';
  pill.style.transform = `translateX(${current.offsetLeft}px)`;
}
addEventListener('resize', moveNavPill);

function render() {
  if (firstRender || reducedMotion.matches || !document.startViewTransition) {
    firstRender = false;
    renderNow();
    if (!reducedMotion.matches && !document.startViewTransition) {
      ['content', 'workspace'].forEach((id) => {
        $(id).classList.remove('swap');
        void $(id).offsetWidth;
        $(id).classList.add('swap');
      });
    }
    return;
  }
  document.startViewTransition(renderNow);
}

function renderNow() {
  panel = null;
  const page = [view, state.week, activeQuestion, activeExam, view === 'study' ? lesson().id : ''].join('/');
  if (renderedPage && page !== renderedPage) scrollTo(0, 0);
  renderedPage = page;
  state.resume = {view, question: activeQuestion, exam: activeExam, filter: practiceFilter};
  if (view === 'errors' && activeQuestion) state.resume.errorReviewIds = errorReviewIds;
  save();
  document.querySelectorAll('.top-nav [data-view]').forEach((button) => {
    if (button.dataset.view === view) button.setAttribute('aria-current', 'page');
    else button.removeAttribute('aria-current');
  });
  moveNavPill();
  $('python').innerHTML = '<i class="dot" aria-hidden="true"></i>Python ' + escape(course.python) + ' / LOCAL';
  $('python').classList.add('ready');
  sidebar();
  ({study, practice, exam: examHome, errors})[view]();
}

let flashTimer;
function showFeedback({message, status, bad}, animate = false) {
  if (!$('output')) return;
  $('output').textContent = message || '没有标准输出。';
  $('output').classList.toggle('bad', !!bad);
  $('status').textContent = status;
  $('status').className = bad ? 'bad' : status === '待验证' ? 'caption' : 'good';
  const consoleBox = $('output').closest('.console');
  const loading = status === '运行中';
  consoleBox.classList.remove('flash-good', 'flash-bad', 'loading');
  if (loading) { $('status').className = ''; consoleBox.classList.add('loading'); return; }
  if (!animate) return;
  void consoleBox.offsetWidth;
  consoleBox.classList.add(bad ? 'flash-bad' : 'flash-good');
  clearTimeout(flashTimer);
  flashTimer = setTimeout(() => consoleBox.classList.remove('flash-good', 'flash-bad'), 1200);
}

function gradeMessage(result, question) {
  const {passed, total, failure} = result;
  let message = `通过 ${passed} / ${total} 组测试。`;
  if (failure) {
    if (failure.input !== undefined && failure.number && question.mode !== '预测输出') {
      const label = failure.number <= question.samples.length ? `公开样例 ${failure.number}` : '额外用例';
      message += '\n首个未通过：' + label;
    }
    if (failure.input !== undefined) message += '\n\n输入：\n' + failure.input;
    if (failure.expected !== undefined) message += '\n\n预期：' + (failure.expected.includes('\n') ? '\n' : ' ') + (failure.expected || '（空）');
    if (failure.actual !== undefined) message += '\n实际：' + (failure.actual.includes('\n') ? '\n' : ' ') + (failure.actual || '（空）');
    if (failure.error) message += '\n\n' + failure.error;
  }
  return {message, status: passed === total ? '全部通过' : passed ? '部分测试失败' : '未通过', bad: passed !== total};
}

function payload() {
  return {code: $('editor').value, input: $('stdin')?.value ?? '', answer: $('answer')?.value ?? ''};
}

function refreshFeedback(animate = false) {
  const {key, question} = panel;
  const submitted = question?.exam && currentExam().results[key];
  const output = feedback.get(key) ?? (submitted && {
    ...gradeMessage(submitted, question), action: 'grade', submitted: submitted.submission,
  });
  if (!output) return;
  const current = payload();
  const previous = output.submitted;
  const stale = output.action !== 'review' && (
    previous.code !== current.code || previous.answer !== current.answer ||
    (output.action === 'run' && previous.input !== current.input)
  );
  if (stale) showFeedback({message: '代码、答案或运行输入已改动，请重新运行或提交。', status: '待验证'});
  else showFeedback(output, animate);
}

function draft() {
  if (!panel) return;
  const destination = panel.question?.exam ? currentExam().drafts : state.drafts;
  destination[panel.key] = payload();
  save();
  if (!running) refreshFeedback();
}

function updateRecord(question, result) {
  const previous = record(question.id);
  const passed = result.passed === result.total;
  const entry = {...previous, ...result, attempts: previous.attempts + 1};
  entry[passed ? 'passingAt' : 'failedAt'] = Date.now();
  state.records[question.id] = entry;
  save();
}

let running = false;
async function execute(action) {
  if (running || !panel) return;
  const {key, question, lessonId} = panel;
  const session = question?.exam ? currentExam() : null;
  const input = payload();
  const data = {id: question?.id, ...input};
  if (action === 'review') Object.assign(data, session.results[key].submission, {review: true});
  running = true;
  const busyButton = document.querySelector(action === 'run' ? '[data-run]' : '[data-grade]');
  busyButton?.classList.add('is-running');
  document.querySelectorAll('[data-run], [data-grade], [data-finish]').forEach((button) => button.disabled = true);
  showFeedback({message: '正在本机运行 Python…', status: '运行中'});
  let output;
  try {
    const result = await api(action === 'review' ? 'grade' : action, data);
    if (action === 'run') {
      const display = question?.kind === 'function' && !result.error ? '返回值：' + result.actual + '\n' + (result.output || '') : result.output;
      output = {message: [display, result.error].filter(Boolean).join('\n'), status: result.error ? '运行错误' : '运行完成', bad: !!result.error};
      if (!question && !result.error) {
        state.visited[lessonId] = true;
        save();
        if (panel?.key === key) sidebar();
      }
    } else {
      output = gradeMessage(result, question);
      if (action !== 'review') {
        if (session) {
          const previous = session.results[key];
          session.results[key] = {...result, attempts: (previous?.attempts || 0) + 1, submission: input};
          save();
        } else updateRecord(question, result);
      }
    }
  } catch (error) {
    output = {message: error.message, status: '运行失败', bad: true};
  } finally {
    running = false;
    busyButton?.classList.remove('is-running');
    document.querySelectorAll('[data-run], [data-grade], [data-finish]').forEach((button) => button.disabled = false);
  }
  feedback.set(key, {...output, action, submitted: input});
  if (panel?.key === key) refreshFeedback(true);
}

function dialog(title, html) {
  $('dialog-title').textContent = title;
  $('dialog-body').innerHTML = html;
  $('dialog').showModal();
}

// Click backdrop to close dialog smoothly
$('dialog').addEventListener('click', (event) => {
  if (event.target === $('dialog')) {
    $('dialog').close();
  }
});

async function finish() {
  if (running) return;
  const id = activeExam;
  const session = currentExam();
  const unanswered = examQuestions(id).length - Object.keys(session.results).length;
  if (unanswered && !confirm(`还有 ${unanswered} 道题未提交判题。现在交卷？`)) return;
  const review = await api('finish', {exam: id});
  session.finished = true;
  session.review = review;
  Object.entries(session.results).forEach(([key, result]) => updateRecord(questions[key], result));
  save();
  activeQuestion = '';
  render();
}

document.addEventListener('input', (event) => {
  if (!['editor', 'answer', 'stdin'].includes(event.target.id)) return;
  if (event.target.id === 'editor') updateNumbers();
  draft();
});

document.addEventListener('keydown', (event) => {
  if (event.target.id === 'editor' && event.key === 'Tab' && !event.shiftKey && !event.target.readOnly) {
    event.preventDefault();
    const editor = event.target;
    editor.setRangeText('    ', editor.selectionStart, editor.selectionEnd, 'end');
    updateNumbers();
    draft();
  }
  if ((event.metaKey || event.ctrlKey) && event.key === 'Enter' && panel) {
    const button = event.shiftKey ? document.querySelector('[data-grade]') : document.querySelector('[data-run]');
    if (button && !button.disabled) {
      event.preventDefault();
      button.click();
    }
  }
});

document.addEventListener('click', async (event) => {
  const button = event.target.closest('button, a[data-view]');
  if (!button) return;
  const {dataset} = button;
  try {
    if (dataset.view) { event.preventDefault(); return mode(dataset.view); }
    if (dataset.week) return selectWeek(Number(dataset.week));
    if (dataset.lesson) {
      state.lesson[state.week] = dataset.lesson;
      save();
      return render();
    }
    if (dataset.lessonPage !== undefined || dataset.pageStep) {
      const index = dataset.lessonPage === undefined
        ? state.lessonPages[lesson().id] + Number(dataset.pageStep)
        : Number(dataset.lessonPage);
      updateLessonPage(index);
      if (dataset.pageStep && matchMedia('(max-width: 820px)').matches) {
        $('content').scrollIntoView({block: 'start'});
      }
      return;
    }
    if (dataset.example) {
      showLessonEditor(lesson(), dataset.example === 'variation');
      if (matchMedia('(max-width: 820px)').matches) $('workspace').scrollIntoView({block: 'start'});
      $('editor').focus({preventScroll: true});
      return;
    }
    if ('returnToLesson' in dataset) return $('content').scrollIntoView({block: 'start'});
    if ('toWorkspace' in dataset) return $('workspace').scrollIntoView({block: 'start'});
    if ('next' in dataset) {
      const index = week().lessons.indexOf(lesson());
      if (index === week().lessons.length - 1) return selectWeek(state.week + 1);
      state.lesson[state.week] = week().lessons[index + 1].id;
      save();
      return render();
    }
    if (dataset.filter) {
      practiceFilter = dataset.filter;
      (state.listPages ??= {})[listKey()] = 0;
      return render();
    }
    if (dataset.listPage !== undefined) {
      (state.listPages ??= {})[listKey()] = Number(dataset.listPage);
      if (matchMedia('(max-width: 820px)').matches) $('content').scrollIntoView({block: 'start'});
      return render();
    }
    if (dataset.errorQuestion) return openQuestion(dataset.errorQuestion, true);
    if (dataset.question) return openQuestion(dataset.question);
    if (dataset.exam) { view = 'exam'; activeQuestion = ''; activeExam = dataset.exam; return render(); }
    if ('backQuestion' in dataset) { activeQuestion = ''; return render(); }
    if ('start' in dataset || 'restart' in dataset) {
      if ('restart' in dataset && !confirm('开始新一轮会重置本轮草稿与成绩。继续？')) return;
      state.exams[activeExam] = {drafts: {}, results: {}, finished: false};
      examQuestions(activeExam).forEach((question) => feedback.delete(question.id));
      save();
      return openQuestion(examQuestions(activeExam)[0].id);
    }
    if ('finish' in dataset) {
      button.disabled = true;
      try { await finish(); } finally { button.disabled = false; }
      return;
    }
    if ('run' in dataset) return execute('run');
    if ('grade' in dataset) return execute('grade');
    if ('review' in dataset) return execute('review');
    if (dataset.sampleInput !== undefined) {
      const input = $('stdin');
      input.value = panel.question.samples[Number(dataset.sampleInput)].stdin;
      input.closest('details').open = true;
      input.focus();
      return draft();
    }
    if ('reset' in dataset) {
      $('editor').value = panel.code;
      updateNumbers();
      return draft();
    }
    if (dataset.hint !== undefined) {
      const id = activeQuestion;
      const level = Number(dataset.hint);
      const response = await api('hint', {id, level});
      hints.set(id, response.text);
      hintLevels.set(id, level);
      if (level === 2) {
        state.records[id] = {...record(id), solutionAt: Date.now()};
        save();
      }
      if (id === activeQuestion && $('hint-text')) {
        document.querySelectorAll('#hint-panel [data-hint]').forEach((btn) => {
          btn.setAttribute('aria-pressed', String(Number(btn.dataset.hint) === level));
        });
        const hintEl = $('hint-text');
        hintEl.hidden = false;
        hintEl.style.animation = 'none';
        void hintEl.offsetWidth;
        hintEl.style.animation = '';
        hintEl.textContent = response.text;
      }
      return;
    }
    if (dataset.remediate) {
      const question = questions[dataset.remediate];
      const practiceSet = course.weeks[question.week - 1].practice;
      const candidates = practiceSet.filter((item) => related(question, item));
      const writing = candidates.filter((item) => ['独立编写', '调试', '综合补练'].includes(item.mode));
      const alternative = writing.find((item) => !record(item.id).attempts) || writing[0] || candidates[0];
      return openQuestion(alternative.id);
    }
    if (dataset.source || dataset.notes) {
      const number = dataset.source || dataset.notes;
      const extension = dataset.notes ? '.md' : '.py';
      const response = await fetch('/source/week' + number + extension);
      if (!response.ok) throw new Error('暂时无法读取课程原始资料。');
      const title = dataset.notes ? '详细讲义' : '课程原代码';
      return dialog(title + ' · Week ' + number, '<pre>' + escape(await response.text()) + '</pre>');
    }
    if (button.id === 'backup') {
      return dialog('学习进度备份', '<p>导出当前浏览器中的学习进度、代码草稿和错题。</p><div class="actions"><button class="primary" data-export>导出 JSON</button><label>导入备份 <input id="import" type="file" accept=".json,application/json"></label></div><p id="backup-status" role="status" class="caption"></p>');
    }
    if ('export' in dataset) {
      const url = URL.createObjectURL(new Blob([JSON.stringify(state, null, 2)], {type: 'application/json'}));
      const link = document.createElement('a');
      link.href = url;
      link.download = 'IS5312-progress.json';
      link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      $('backup-status').textContent = '已导出备份。';
    }
  } catch (error) {
    if (panel) showFeedback({message: error.message, status: '操作失败', bad: true});
    else dialog('操作失败', '<p>' + escape(error.message) + '</p>');
  }
});

document.addEventListener('change', async (event) => {
  if (event.target.id === 'mobile-lesson') {
    state.lesson[state.week] = event.target.value;
    render();
    return;
  }
  if (event.target.id !== 'import' || !event.target.files[0]) return;
  try {
    const imported = JSON.parse(await event.target.files[0].text());
    if (imported.version !== 1 || !Number.isInteger(imported.week) || imported.week < 1 || imported.week > course.weeks.length ||
      !['lesson', 'visited', 'drafts', 'records', 'exams'].every((key) => imported[key] && typeof imported[key] === 'object')) {
      throw new Error('请选择从本工作台导出的 JSON 备份。');
    }
    if (!confirm('导入会覆盖当前浏览器的学习进度。继续？')) return;
    state = imported;
    practiceFilter = state.resume?.filter || '全部';
    feedback = new Map();
    hints = new Map();
    hintLevels = new Map();
    save();
    $('dialog').close();
    mode('study');
  } catch (error) { $('backup-status').textContent = error.message; }
});

render();
