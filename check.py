import urllib.request
import socket
import ssl
from datetime import datetime
import re

socket.setdefaulttimeout(5)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

online = []
offline = []

def check_server(host, port):
    url = f"https://{host}:{port}"
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": "RFD-status-checker"}
    )
    urllib.request.urlopen(req, context=ctx)

with open("ips.list", "r", encoding="utf-8") as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue

        entry, *meta = raw.split("|")
        host, port = entry.split(":")

        meta_info = ""
        if meta:
            meta_info = f" (RCC endpoints: {meta[0].replace('rcc=', '')})"
        try:
            check_server(host, port)
            online.append(f"- {host}:{port}{meta_info}")
        except Exception:
            offline.append(f"- {host}:{port}")

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

status.extend(online if online else ["- None"])

status += [
    "",
    "### Offline / Unreachable",
]

status.extend(offline if offline else ["- None"])

new_block = f"{START}\n" + "\n".join(status) + f"\n{END}"

content = re.sub(
    f"{START}[\\s\\S]*?{END}",
    new_block,
    content,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
