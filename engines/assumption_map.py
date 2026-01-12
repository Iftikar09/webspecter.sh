from urllib.parse import urlparse, parse_qs
from engines.common import *

params = safe_read(f"{SIG}/params.txt")

out = os.path.join(BASE, "assumptions.md")
with open(out, "w") as f:
    f.write("# 🧠 Assumption Map\n\n")
    if not params:
        f.write("No URL parameters observed.\n")
    for u in params:
        qs = parse_qs(urlparse(u).query)
        for k in qs:
            if "id" in k.lower():
                f.write(f"- Possible ownership dependency via `{k}` (observed in URL)\n")

print("[+] Assumption map generated")
