import json, sys
from difflib import unified_diff

def load_file(path):
    with open(path) as f:
        return json.load(f)

def compare_json(file1, file2):
    j1, j2 = load_file(file1), load_file(file2)
    s1, s2 = json.dumps(j1, indent=2).splitlines(), json.dumps(j2, indent=2).splitlines()
    diff = unified_diff(s1, s2, fromfile=file1, tofile=file2, lineterm="")
    return "\n".join(diff)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python src/diff.py old.json new.json")
        sys.exit(1)
    print(compare_json(sys.argv[1], sys.argv[2]))
