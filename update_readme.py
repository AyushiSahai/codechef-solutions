import os

def count_files(folder):
    if not os.path.exists(folder):
        return 0
    return len([f for f in os.listdir(folder) if f.endswith('.py')])

easy = count_files('Easy')
medium = count_files('Medium')
hard = count_files('Hard')
contests = count_files('Contests')
total = easy + medium + hard + contests

all_files = []
for folder in ['Easy', 'Medium', 'Hard', 'Contests']:
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith('.py'):
                path = os.path.join(folder, f)
                all_files.append((os.path.getmtime(path), folder, f))

all_files.sort(reverse=True)
recent = all_files[:5]

recent_list = ""
for _, folder, fname in recent:
    name = fname.replace('.py', '').replace('_', ' ')
    recent_list += f"| {name} | {folder} |\n"

readme = f"""# 🍴 CodeChef Solutions

A clean, organized collection of my CodeChef problem solutions in Python.

![Language](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-CodeChef-orange)
![Problems](https://img.shields.io/badge/Problems%20Solved-{total}-brightgreen)

## 📊 Progress (Auto Updated!)

| Difficulty | Solved |
|------------|--------|
| ⭐ Easy | {easy} |
| ⭐⭐ Medium | {medium} |
| ⭐⭐⭐ Hard | {hard} |
| 🏆 Contests | {contests} |
| **Total** | **{total}** |

## 🕐 Recently Added

| Problem | Difficulty |
|---------|------------|
{recent_list}
## 🚀 Daily Workflow

1. Solve problem on CodeChef ✅
2. Go to GitHub → correct folder → Add file
3. Paste code → Commit!
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"✅ README updated! Easy:{easy} Medium:{medium} Hard:{hard} Total:{total}")
