import os

LINE = "Tomorrow in Nowhere: sunny with a 100% chance of your umbrella being useless."

LIMIT = 120
if len(LINE) != 77 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 77 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# A forecast for a city that isn't: specific weather, useless advice.
