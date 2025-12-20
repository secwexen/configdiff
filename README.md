# ConfigDiff 🔑
A simple CLI tool to compare two configuration files and highlight the differences.  
Useful for developers, DevOps engineers, and security teams who need to track changes between environments (`dev`, `staging`, `prod`).

---

## Usage
```bash
python src/diff.py examples/config_old.json examples/config_new.json
```

---

## Example Output
```diff
- "debug": true
+ "debug": false
```

---

## Features
- Compare JSON configuration files (YAML support can be added easily).
- Clear diff output using standard `unified_diff`.
- Lightweight, single-file implementation.
- Easy to extend for custom formats.

---

## Project Structure
```
ConfigDiff/
├── src/diff.py
├── examples/config_old.json
├── examples/config_new.json
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md 
├── LICENSE
├── README.md
├── SECURITY.md
├── requirements.txt
```

---

## Requirements
- Python 3.8+
- No external dependencies (uses built-in `json` and `difflib` modules).

---

## License
This project is licensed under the Apache-2.0 License. See the [LICENSE](https://github.com/X99874/configdiff/blob/main/LICENSE) file for details.
