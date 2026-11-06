#!/bin/zsh
cd -- "${0:A:h}"
url=http://127.0.0.1:8531
if curl -fsS "${url}/api/course" >/dev/null 2>&1; then
  open "$url"
  exit
fi
python3 -c 'import numpy' || exit 1
export PYTHONDONTWRITEBYTECODE=1
python3 server.py &
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
