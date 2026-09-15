import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_report


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "assets").mkdir()
        (self.root / "assets/photo.png").write_bytes(b"image")
        self.patch = patch.object(build_report, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def test_links_resolve_from_source_and_leave_examples_intact(self):
        text = '''![Foto](../assets/photo.png)
<img src="../assets/photo.png">
[Informe](chapter.md#intro)
[Sitio](https://example.org/page)
[Sección](#intro)
[foto]: ../assets/photo.png "Foto"
`<img src="../assets/missing.png">`
```markdown
![Ejemplo](../assets/missing.png)
# Encabezado de ejemplo
```
'''
        (self.root / "docs/chapter.md").write_text("# Intro\n")
        result = build_report.rewrite_links(text, Path("docs/chapter.md"))
        self.assertIn('![Foto](assets/photo.png)', result)
        self.assertIn('<img src="assets/photo.png">', result)
        self.assertIn('[Informe](docs/chapter.md#intro)', result)
        self.assertIn('[foto]: assets/photo.png "Foto"', result)
        self.assertIn('[Sitio](https://example.org/page)', result)
        self.assertIn('[Sección](#intro)', result)
        self.assertIn('`<img src="../assets/missing.png">`', result)
        self.assertIn('![Ejemplo](../assets/missing.png)', result)
        self.assertEqual(list(build_report.headings(result)), [])

    def test_missing_local_asset_fails_with_source_name(self):
        with self.assertRaisesRegex(ValueError, r"docs/chapter.md.*missing.png"):
            build_report.rewrite_links('![Foto](../assets/missing.png)', Path("docs/chapter.md"))

    def test_toc_uses_real_headings_and_unique_unicode_anchors(self):
        manifest = {"cover": "docs/cover.md", "info": "docs/info.md", "sections": [{"file": "docs/chapter.md"}]}
        (self.root / "docs/report.json").write_text(json.dumps(manifest))
        (self.root / "docs/cover.md").write_text("## Equipo\n")
        (self.root / "docs/info.md").write_text("## Student Outcome\n")
        chapter = self.root / "docs/chapter.md"
        chapter.write_text("# Capítulo I: Introducción\n\n## Equipo\n\n## Equipo\n\n## A & B\n\n```md\n## Invisible\n```\n")
        result = build_report.build()
        self.assertIn('- [Capítulo I: Introducción](#capítulo-i-introducción)', result)
        self.assertIn('  - [Equipo](#equipo-1)', result)
        self.assertIn('  - [Equipo](#equipo-2)', result)
        self.assertIn('  - [A & B](#a--b)', result)
        self.assertNotIn('[Invisible]', result)
        self.assertEqual(result, build_report.build())
        chapter.write_text("# Capítulo I\n<<<<<<< HEAD\nconflicto\n=======\notro\n>>>>>>> main\n")
        with self.assertRaisesRegex(ValueError, "conflicto de Git"):
            build_report.build()


if __name__ == "__main__":
    unittest.main()
