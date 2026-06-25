"""
main.py
Runs the complete Family Peace Assistant pipeline.
"""
print("=" * 55)
print("  🕊️  FAMILY PEACE ASSISTANT")
print("  CodTech IT Solutions — ML Internship")
print("  Intern   : Abhishek Prasad")
print("  Intern ID: CITS5099")
print("  Project  : Family Peace Assistant")
print("=" * 55)

import subprocess, sys

steps = [
    ("Step 1: Generating emotion dataset...",   "generate_data.py"),
    ("Step 2: Training emotion detector...",     "train_model.py"),
    ("Step 3: Creating visualizations...",       "visualize.py"),
]

for msg, script in steps:
    print(f"\n{'─'*55}")
    print(f" {msg}")
    print(f"{'─'*55}")
    result = subprocess.run([sys.executable, script], capture_output=False)
    if result.returncode != 0:
        print(f"\n❌ Error in {script}. Stopping.")
        sys.exit(1)

print("\n" + "=" * 55)
print(" ✅ Setup complete! Starting the assistant...\n")
print(" Now you can type how you are feeling")
print(" and I will give you helpful advice. 💙")
print("=" * 55)

# Start the interactive assistant
from predict import run_interactive
run_interactive()
