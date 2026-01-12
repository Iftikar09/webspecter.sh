from urllib.parse import urlparse, parse_qs
from engines.common import *

print("\n🧪 Negative Test Prompts")
print("-" * 50)

params = safe_read(f"{SIG}/params.txt", 1)
if not params:
    print("No URL params → test JSON body fields & REST paths")
    sys.exit(0)

u = params[0]
p = urlparse(u)
qs = parse_qs(p.query)

print(f"Endpoint: {p.path}")
print(f"Params: {', '.join(qs.keys())}")
print("Try:")
print("• Skip UI flow")
print("• Replay request")
print("• Change HTTP method")
print("• Remove required param")
print("• Use valid token with wrong ID")
print("Success = backend action without permission")

print("-" * 50)
