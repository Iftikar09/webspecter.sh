from engines.common import *

chains = []

if os.path.exists(f"{SIG}/params.txt") and os.path.exists(f"{SIG}/js.txt"):
    chains.append("JS logic → hidden API → missing auth → IDOR")

if os.path.exists(f"{SIG}/params.txt"):
    chains.append("User-controlled ID → missing ownership check → privilege escalation")

chains = list(dict.fromkeys(chains))

print("\n🧵 Advanced Chain Brainstorming")
print("-" * 50)

if not chains:
    print("No strong chains detected.")
else:
    for i, c in enumerate(chains, 1):
        print(f"{i}. {c}")
        print("   How:")
        print("   • Identify entry point")
        print("   • Bypass UI")
        print("   • Test cross-user access")

print("-" * 50)
