import json
from pathlib import Path

# Generates reports-index.json listing HTML reports under ./reports
# Format: [{"path":"reports/foo.html","title":"...","date":"YYYY-MM-DD"}, ...]

reports_dir = Path('reports')
items = []

if reports_dir.exists():
    for p in sorted(reports_dir.glob('**/*.html')):
        # naive title extraction
        title = None
        try:
            txt = p.read_text(encoding='utf-8', errors='ignore')
            import re
            m = re.search(r'<title>(.*?)</title>', txt, re.IGNORECASE | re.DOTALL)
            if m:
                title = ' '.join(m.group(1).split())
        except Exception:
            pass
        items.append({
            'path': str(p.as_posix()),
            'title': title or p.stem,
        })

out = Path('reports-index.json')
out.write_text(json.dumps(items, indent=2) + "\n", encoding='utf-8')
print(f"Wrote {out} with {len(items)} item(s)")
