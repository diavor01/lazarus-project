import sys


for line in sys.stdin:
    # Strip newline and process each line
    line = line.strip()
    if line:  # Skip empty lines
        print(f"Processing: {line}")