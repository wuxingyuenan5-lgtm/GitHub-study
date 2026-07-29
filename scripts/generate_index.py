#!/usr/bin/env python3
"""
根据 metadata/projects.yaml 生成项目索引.md
用法: python scripts/generate_index.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YAML_PATH = ROOT / "metadata" / "projects.yaml"
INDEX_PATH = ROOT / "项目索引.md"


def parse_yaml_simple(path: Path) -> list[dict]:
    """极简YAML解析，只处理本项目metadata结构。"""
    projects = []
    current = None
    in_websites = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.lstrip()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped == "projects:":
            in_websites = False
            continue

        if stripped == "websites:":
            in_websites = True
            continue

        if in_websites:
            continue  # 网站单独处理，不写入索引表

        indent = len(line) - len(stripped)

        if stripped.startswith("- id:"):
            if current:
                projects.append(current)
            current = {"id": stripped.split(":", 1)[1].strip()}
        elif current and indent >= 4 and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip()

    if current:
        projects.append(current)

    return projects


def parse_tags(tags_str: str) -> list[str]:
    inner = tags_str.strip("[]")
    if not inner:
        return []
    return [t.strip() for t in inner.split(",") if t.strip()]


def badge_for(project: dict) -> str:
    tags = parse_tags(project.get("tags", ""))
    badges = []
    if "热门" in tags:
        badges.append("🔥")
    if "推荐" in tags:
        badges.append("⭐")
    if "冷门" in tags:
        badges.append("🧊")
    license = project.get("license", "未标注")
    if license in ("GPL-3.0", "PolyForm Noncommercial"):
        badges.append("⚠️")
    return " ".join(badges)


def generate_index(projects: list[dict]) -> str:
    # 按分类分组
    categories: dict[str, list[dict]] = {}
    for p in projects:
        cat = p.get("category", "?")
        categories.setdefault(cat, []).append(p)

    lines = [
        "# 二级市场开源项目索引",
        "",
        "> 本文件由 `scripts/generate_index.py` 根据 `metadata/projects.yaml` 自动生成。",
        "> 如需修改，请编辑 `metadata/projects.yaml` 后重新运行生成脚本。",
        "> 本库仅保留项目调研评估与快速索引链接，**不备份源码**。",
        "",
        "---",
        "",
        "## 图例",
        "",
        "- 🔥 热门项目",
        "- ⭐ 推荐关注",
        "- 🧊 冷门项目",
        "- ⚠️ 许可证有约束（GPL-3.0 / PolyForm Noncommercial / 未标注）",
        "",
        "---",
        "",
    ]

    total = 0
    for cat in sorted(categories.keys()):
        cat_projects = categories[cat]
        total += len(cat_projects)
        cat_name = cat_projects[0].get("category_name", cat)
        lines.append(f"## {cat}. {cat_name}（{len(cat_projects)}个）")
        lines.append("")
        lines.append("| ID | 项目 | GitHub 地址 | Stars | 许可证 | 一句话说明 |")
        lines.append("|----|------|-------------|:-----:|--------|-----------|")

        for p in cat_projects:
            badge = badge_for(p)
            name = f"**{p['name']}** {badge}".strip()
            repo = p.get("repo", "")
            url = p.get("url", f"https://github.com/{repo}")
            stars = p.get("stars", "未显示")
            license = p.get("license", "未标注")
            summary = p.get("summary", "")
            lines.append(
                f"| {p['id']} | {name} | {url} | {stars} | {license} | {summary} |"
            )
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 使用建议",
        "",
        "1. **优先看分类 README**：每个分类目录下的 `README.md` 有详细的项目介绍、优缺点、适用场景、上手建议。",
        "2. **点击链接直达仓库**：所有项目地址均为 GitHub 原始仓库，Star/Fork/Issue 都在那里。",
        "3. **注意许可证**：涉及 GPL-3.0 和 PolyForm Noncommercial 的项目有使用限制，详见根目录 README。",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    if not YAML_PATH.exists():
        print(f"错误: 找不到 {YAML_PATH}", file=sys.stderr)
        return 1

    projects = parse_yaml_simple(YAML_PATH)
    if not projects:
        print("错误: 没有解析到任何项目", file=sys.stderr)
        return 1

    INDEX_PATH.write_text(generate_index(projects), encoding="utf-8")
    print(f"已生成 {INDEX_PATH}，共 {len(projects)} 个项目")
    return 0


if __name__ == "__main__":
    sys.exit(main())
