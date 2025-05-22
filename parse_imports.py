import json
import re

with open("package_install.ipynb", 'r', encoding='utf-8') as f:
    notebook = json.load(f)

imports = set()
pattern = re.compile(r'^\s*(?:import|from)\s+([a-zA-Z_][\w\.]*)')

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        for line in cell['source']:
            match = pattern.match(line)
            if match:
                root_pkg = match.group(1).split('.')[0]
                imports.add(root_pkg)

with open("requirements.txt", "w") as f:
    for imp in sorted(imports):
        f.write(f"{imp}\n")