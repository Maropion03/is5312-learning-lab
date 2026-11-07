#!/bin/zsh
cd -- "${0:A:h}"
url=http://127.0.0.1:8531
if curl -fsS "${url}/api/course" >/dev/null 2>&1; then
  open "$url"
  exit
fi
python_bin=python3
if [[ -x .venv/bin/python ]]; then python_bin=.venv/bin/python; fi
"$python_bin" -c 'import numpy, pandas' || exit 1
export PYTHONDONTWRITEBYTECODE=1
"$python_bin" server.py &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null' EXIT
for attempt in {1..30}; do
  if curl -fsS "${url}/api/course" >/dev/null 2>&1; then
    open "$url"
    wait "$server_pid"
    exit
  fi
  sleep 0.2
done
wait "$server_pid"
