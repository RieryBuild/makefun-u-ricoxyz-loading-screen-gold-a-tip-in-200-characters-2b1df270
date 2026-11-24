"""Write the loading-screen tip to entry.txt.

The joke: the AI agent has supposedly read the function three
times and still cannot say what it does — and neither can the
developer staring at the same loading screen. The last beat
turns the knife: the developer wrote it. Both sides of the
keyboard are equally lost, which is why it lands for both.
"""

import os

TIP = "Loading... Your agent has read this function three times. It still has no idea what it does. Neither do you. You wrote it."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TIP)
