import urllib.request
import socket
import ssl
from datetime import datetime
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
socket.setdefaulttimeout(5)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
MAX_WORKERS = 10
def check_server(host, port):
    url = f"https://{host}:{port}"
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": "RFD-status-checker"}
    )
    urllib.request.urlopen(req, context=ctx)

def parse_meta(meta_raw):
    meta = {}
    if not meta_raw:
        return meta

    for part in meta_raw.split("|"):
        if "=" not in part:
            continue
        key, val = part.split("=", 1)
        meta[key.strip()] = val.strip().strip('"')
    return meta

def process_line(raw):
    raw = raw.strip()
    if not raw:
        return None

    entry, *meta_raw = raw.split("|", 1)
    host, port = entry.split(":")
    meta = parse_meta(meta_raw[0] if meta_raw else "")

    suffix = []
    if "rcc" in meta:
        suffix.append(f"RCC Services {meta['rcc']}")
    if "note" in meta:
        suffix.append(f"Notes: {meta['note']}")

    suffix_text = f" | {' | '.join(suffix)}" if suffix else ""
    label = f"- {host}:{port}{suffix_text}"

    try:
        check_server(host, port)
        return ("online", label)
    except Exception:
        return ("offline", label)

online = []
offline = []
with open("ips.list", "r", encoding="utf-8") as f:
    lines = list(f)
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = [executor.submit(process_line, line) for line in lines]
    for future in as_completed(futures):
        result = future.result()
        if not result:
            continue
        state, label = result
        if state == "online":
            online.append(label)
        else:
            offline.append(label)
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
START = "<!-- STATUS-START -->"
END = "<!-- STATUS-END -->"
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
status = [
    "## Status Test",
    f"Last check: {now}",
    "",
    "### Online",
]
status.extend(sorted(online) or ["- None"])
status += [
    "",
    "### Offline / Unreachable",
]
status.extend(sorted(offline) or ["- None"])
new_block = f"{START}\n" + "\n".join(status) + f"\n{END}"
content = re.sub(
    f"{START}[\\s\\S]*?{END}",
    new_block,
    content,
)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
