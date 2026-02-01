import urllib.request
import socket
import ssl
from datetime import datetime

socket.setdefaulttimeout(5)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

online = []
offline = []

with open("ips.list") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if not line.startswith("http://") and not line.startswith("https://"):
            url = "https://" + line
        else:
            url = line

        try:
            req = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": "status-checker"}
            )
            urllib.request.urlopen(req, context=ctx)
            online.append(line)
        except Exception as e:
            offline.append(line)
                
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

START = "<!-- STATUS-START -->"
END = "<!-- STATUS-END -->"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

status = []
status.append("## Status Test")
status.append(f"Last check: {now}\n")

status.append("### Online")
status.extend(f"- {h}" for h in online or ["None"])

status.append("\n### Offline / Unreachable")
status.extend(f"- {h}" for h in offline or ["None"])

new_block = START + "\n" + "\n".join(status) + "\n" + END

import re
content = re.sub(
    f"{START}[\\s\\S]*?{END}",
    new_block,
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
