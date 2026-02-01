import urllib.request
import socket
from datetime import datetime

socket.setdefaulttimeout(3)

online = []
offline = []

with open("ips.list") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # assume http by default
        if not line.startswith("http://") and not line.startswith("https://"):
            url = "http://" + line
        else:
            url = line

        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req):
                online.append(line)
        except Exception:
            offline.append(line)

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

with open("README.md", "w") as f:
    f.write("# Status Test\n\n")
    f.write(f"Last check: {now}\n\n")

    f.write("## Online\n")
    if online:
        for h in online:
            f.write(f"- {h}\n")
    else:
        f.write("None\n")

    f.write("\n## Offline / Unreachable\n")
    if offline:
        for h in offline:
            f.write(f"- {h}\n")
    else:
        f.write("None\n")
