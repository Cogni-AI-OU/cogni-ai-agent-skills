import os
import glob
import re


def check_skill(filepath):
    issues = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    folder_name = os.path.basename(os.path.dirname(filepath))

    # 1. Check YAML frontmatter
    if not content.startswith("---"):
        issues.append("Missing YAML frontmatter")
    else:
        fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
            desc_match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
            license_match = re.search(r"^license:\s*(.+)$", fm, re.MULTILINE)

            if not name_match:
                issues.append("Missing 'name' in frontmatter")
            elif name_match.group(1).strip() != folder_name:
                issues.append("Name does not match folder")

            if not desc_match:
                issues.append("Missing 'description' in frontmatter")
            else:
                desc = desc_match.group(1).strip()
                if not (desc.startswith("'") and desc.endswith("'")):
                    issues.append("Description is not wrapped in single quotes")

            if not license_match:
                issues.append("Missing 'license' in frontmatter")
        else:
            issues.append("Malformed YAML frontmatter")

    # 2. Check Title
    if not re.search(r"^#\s+.+", content, re.MULTILINE):
        issues.append("Missing H1 Title")

    # 3. Check Markdownlint overrides
    if "<!-- markdownlint-disable " not in content:
        issues.append("Missing markdownlint overrides")

    # 4. & 5. Check mandatory sections
    if not re.search(r"^## When to Use", content, re.MULTILINE):
        issues.append("Missing '## When to Use'")
    if not re.search(r"^## When Not to Use", content, re.MULTILINE):
        issues.append("Missing '## When Not to Use'")

    if not re.search(r"^## Gotchas", content, re.MULTILINE):
        issues.append("Missing '## Gotchas'")

    return issues


skill_files = glob.glob("*/SKILL.md")
stats = {}
total = len(skill_files)
fully_compliant = 0

for sf in skill_files:
    issues = check_skill(sf)
    if not issues:
        fully_compliant += 1
    for issue in issues:
        stats[issue] = stats.get(issue, 0) + 1

print(f"Total Skills Checked: {total}")
print(f"Fully Compliant Skills: {fully_compliant}")
print("\nIssues Breakdown:")
for issue, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
    print(f"- {issue}: {count} skills ({count/total*100:.1f}%)")
