print("Starting Text2Table")
import random
from tqdm import tqdm
print("Opening lines.txt...")

newlines = []

try:
    file = open("lines.txt", "r", encoding="utf8")
    lines = file.readlines()
    print("Processing lines...")
    for i in tqdm(range(len(lines)), desc="Processing Lines"):
        v = lines[i]
        nv = v.strip()
        newlines.append(nv)
    print(newlines)
except OSError as oe:
    print(f"Error getting lines.txt: {oe}")
except UnicodeDecodeError as de:
    print(f"Error! Unable to decode file: {de}")

for i in range(5):
    print(random.choice(lines))
input("Press enter to exit...")
