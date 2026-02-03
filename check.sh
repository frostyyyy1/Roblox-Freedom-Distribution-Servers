#!/bin/bash
cd "$(dirname "$0")"
set -euo pipefail
MAX_WORKERS=25
TIMEOUT=5
IPS_FILE="server.list"
README="README.md"

START="<!-- STATUS-START -->"
END="<!-- STATUS-END -->"

TMP_ONLINE="$(mktemp)"
TMP_OFFLINE="$(mktemp)"
TMP_README="$(mktemp)"
trap 'rm -f "$TMP_ONLINE" "$TMP_OFFLINE" "$TMP_README"' EXIT

check_server() {
  local host="$1"
  local port="$2"

  curl --insecure --silent --head \
    --connect-timeout "$TIMEOUT" \
    --max-time "$TIMEOUT" \
    --user-agent "RFD-status-checker" \
    "https://$host:$port" >/dev/null
}

parse_and_check() {
  local raw="$1"
  raw="$(echo "$raw" | xargs)"
  [[ -z "$raw" ]] && return

  local entry meta host port
  entry="${raw%%|*}"
  meta=""
  [[ "$raw" == *"|"* ]] && meta="${raw#*|}"

  host="${entry%%:*}"
  port="${entry##*:}"

  local suffix=""
  if [[ -n "$meta" ]]; then
    IFS='|' read -ra parts <<< "$meta"
    for part in "${parts[@]}"; do
      key="${part%%=*}"
      val="${part#*=}"
      val="${val%\"}"
      val="${val#\"}"

      # Removes excess whitespace.
      key="$(echo "$key" | xargs)"
      val="$(echo "$val" | xargs)"

      case "$key" in
        rcc)  suffix+=" - RCC Services $val" ;;
        note) suffix+=" - Notes: $val" ;;
      esac
    done
  fi

  label="- **\`$host:$port\`**$suffix"
  if check_server "$host" "$port"; then
    echo "ONLINE   $label"
    echo "$label" >> "$TMP_ONLINE"
  else
    echo "OFFLINE  $label"
    echo "$label" >> "$TMP_OFFLINE"
  fi
}

export -f check_server parse_and_check
export TMP_ONLINE TMP_OFFLINE TMP_README TIMEOUT

xargs -a "$IPS_FILE" -P "$MAX_WORKERS" -I {} bash -c 'parse_and_check "$@"' _ {}

NOW="$(date -u '+%Y-%m-%d %H:%M:%S UTC')"

ONLINE="$(sort "$TMP_ONLINE" 2>/dev/null || true)"
OFFLINE="$(sort "$TMP_OFFLINE" 2>/dev/null || true)"

[[ -z "$ONLINE" ]] && ONLINE="- None"
[[ -z "$OFFLINE" ]] && OFFLINE="- None"

STATUS_BLOCK=$(cat <<EOF
$START
## Status Test
Last check: $NOW

### Online
$ONLINE

### Offline / Unreachable
$OFFLINE
$END
EOF
)

awk -v start="$START" -v end="$END" -v block="$STATUS_BLOCK" '
  BEGIN { in_block=0 }
  $0 ~ start { print block; in_block=1; next }
  $0 ~ end   { in_block=0; next }
  !in_block  { print }
' "$README" > "$TMP_README"

mv "$TMP_README" "$README"
