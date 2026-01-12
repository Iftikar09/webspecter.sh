from urllib.parse import urlparse, parse_qs
from engines.common import *

print("\n🧠 Context-Aware Hints")
print("-" * 40)

for u in safe_read(f"{SIG}/params.txt", 2):
    p = urlparse(u)
    print(f"• Path: {p.path}")
    print(f"  Params: {', '.join(parse_qs(p.query).keys())}")
    print("  → Check auth, ownership, reflection")

for j in safe_read(f"{SIG}/js.txt", 2):
    print(f"• JS: {j}")
    print("  → Inspect hidden APIs, role checks")

print("-" * 40)
