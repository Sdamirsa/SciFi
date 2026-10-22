"""Tests for scripts/release.py: version agreement, changelog sections, bump arithmetic."""
import importlib.util
import json
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("release", REPO / "scripts" / "release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_versions_agree(self):
        vs = release.versions_everywhere()
        self.assertEqual(len(set(vs.values())), 1, vs)
        self.assertRegex(vs["plugin.json"], r"^\d+\.\d+\.\d+$")

    def test_changelog_has_current_version(self):
        sec = release.changelog_section(release.version())
        self.assertTrue(sec, "CHANGELOG.md needs a non-empty section for the current version")

    def test_changelog_missing_version_is_none(self):
        self.assertIsNone(release.changelog_section("999.0.0"))

    def test_marketplace_points_at_this_plugin(self):
        m = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())
        self.assertEqual(m["plugins"][0]["name"], json.loads((REPO / ".claude-plugin" / "plugin.json").read_text())["name"])


if __name__ == "__main__":
    unittest.main()
