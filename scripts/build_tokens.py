"""Regenerate assets/css/tokens.css from design-system/tokens.json.

Run from the repository root:  python3 scripts/build_tokens.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((ROOT / "design-system/tokens.json").read_text(encoding="utf-8"))


def value(tok, theme):
    raw = tok["value"]
    if not isinstance(raw, str):
        raw = raw.get(theme, raw["light"])
    return re.sub(r"\{(.+?)\}", r"var(--\1)", raw)


def block(selector, theme, families, indent=""):
    rows = "".join(
        f"{indent}  --{t['name']}: {value(t, theme)};\n"
        for fam in families
        for t in tokens.get(fam, {}).get("tokens", [])
    )
    return f"{indent}{selector} {{\n{rows}{indent}}}\n"


themed = ["color", "shadow"]
out = ["/* ByPilares: generated from design-system/tokens.json. Edit the JSON, then run python3 scripts/build_tokens.py */"]
out.append(block(':root, [data-theme="light"]', "light", themed))
out.append("@media (prefers-color-scheme: dark) {\n" + block(':root:not([data-theme="light"])', "dark", themed, "  ") + "}\n")
out.append(block('[data-theme="dark"]', "dark", themed))

static = "".join(
    f"  --{t['name']}: {t['value']};\n" for fam in ("spacing", "radius") for t in tokens[fam]["tokens"]
)
fonts = "".join(f"  --font-{k}: {v};\n" for k, v in tokens["type"]["families"].items())
out.append(":root {\n" + static + fonts + "}\n")

for group in tokens["type"]["groups"]:
    for s in group["styles"]:
        props = [
            f"font-family: var(--font-{s.get('family', group['family'])})",
            f"font-size: {s['fontSize']}",
            f"line-height: {s['lineHeight']}",
            f"font-weight: {s['fontWeight']}",
        ]
        if "letterSpacing" in s:
            props.append(f"letter-spacing: {s['letterSpacing']}")
        if "fontStyle" in s:
            props.append(f"font-style: {s['fontStyle']}")
        out.append(f".t-{s['name']} {{ {'; '.join(props)}; }}")

(ROOT / "assets/css/tokens.css").write_text("\n".join(out) + "\n", encoding="utf-8")
print("Wrote assets/css/tokens.css")
