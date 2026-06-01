"""Tests for the KOTUS dictionary class tags (KTN/KAV) in the omor format.

These cover the `ktnkav` extension of the omor tagset: the `[KTN=N]` and
`[KAV=X]` tags emitted by `OmorFormatter` when `ktnkav=True`. The feature is
opt-in and off by default, so the first job of the suite is to pin that the
default output is untouched; the rest verify that, when enabled, the tags are
declared as multichar symbols and emitted to match that declaration.

Run: python3 -m unittest test.test_ktnkav  (from the repository root, or
point PYTHONPATH at src/python).
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "python")
)

from omor_formatter import OmorFormatter  # noqa: E402
from string_manglers import lexc_escape  # noqa: E402


def wordmap(kotus_tn, kotus_av=None, upos="NOUN"):
    """Minimal wordmap with the only fields kotus_tags reads."""
    return {"upos": upos, "kotus_tn": kotus_tn, "kotus_av": kotus_av}


# KOTUS class numbers that contain a zero. lexc treats a bare "0" as the
# epsilon symbol, so these are exactly the numbers a careless escape mangles.
ZERO_CLASSES = ["10", "20", "30", "40", "50", "60", "70"]
# A few non-zero classes as the control group.
PLAIN_CLASSES = ["1", "9", "38", "52", "71", "78"]


class DefaultBehaviourUnchanged(unittest.TestCase):
    """ktnkav is off by default; nothing about the default output changes."""

    def test_off_by_default(self):
        self.assertFalse(OmorFormatter().ktnkav)

    def test_no_tags_when_disabled(self):
        fmt = OmorFormatter()
        for tn in ZERO_CLASSES + PLAIN_CLASSES:
            self.assertEqual(fmt.kotus_tags(wordmap(tn, "F")), "")

    def test_no_ktn_kav_in_multichars_when_disabled(self):
        header = OmorFormatter().multichars_lexc()
        self.assertNotIn("[KTN=", header)
        self.assertNotIn("[KAV=", header)


class MulticharDeclaration(unittest.TestCase):
    """When enabled, every KTN/KAV symbol must be declared in the header."""

    def setUp(self):
        self.header = OmorFormatter(ktnkav=True).multichars_lexc()

    def test_declares_zero_classes(self):
        for tn in ZERO_CLASSES:
            self.assertIn(f"[KTN={tn}]", self.header)

    def test_declares_plain_classes(self):
        for tn in PLAIN_CLASSES:
            self.assertIn(f"[KTN={tn}]", self.header)

    def test_declares_gradation_classes(self):
        for kav in ["A", "F", "J", "L"]:
            self.assertIn(f"[KAV={kav}]", self.header)


class TagEmission(unittest.TestCase):
    """Emitted tags are unescaped and match the declared multichar symbols."""

    def setUp(self):
        self.fmt = OmorFormatter(ktnkav=True)

    def test_zero_classes_emit_unescaped(self):
        # The regression this whole change is about: 10 must stay 10, not 1%0.
        for tn in ZERO_CLASSES:
            self.assertEqual(self.fmt.kotus_tags(wordmap(tn)), f"[KTN={tn}]")

    def test_every_standard_class_round_trips(self):
        # For all 1..78, when a tag is emitted it equals [KTN=N] and is a
        # declared multichar symbol. This is the invariant the escape broke.
        for n in range(1, 79):
            tag = self.fmt.kotus_tags(wordmap(str(n)))
            if tag:
                self.assertEqual(tag, f"[KTN={n}]")
                self.assertIn(f"[KTN={n}]", self.fmt.ktnkav_multichars)

    def test_gradation_appended(self):
        self.assertEqual(self.fmt.kotus_tags(wordmap("60", "F")), "[KTN=60][KAV=F]")
        self.assertEqual(self.fmt.kotus_tags(wordmap("9", "A")), "[KTN=9][KAV=A]")

    def test_no_gradation_no_kav(self):
        self.assertEqual(self.fmt.kotus_tags(wordmap("9", None)), "[KTN=9]")

    def test_exceptional_classes_emit(self):
        # 1007-1026 are intentional exceptional nominal classes; they contain
        # zeros and are listed in ktnkav_multichars.
        for tn in ["1007", "1009", "1010", "1024", "1026"]:
            if f"[KTN={tn}]" in self.fmt.ktnkav_multichars:
                self.assertEqual(self.fmt.kotus_tags(wordmap(tn)), f"[KTN={tn}]")

    def test_ambiguous_pipe_class_emits_nothing(self):
        # Pipe-joined classes (e.g. "5|6") are not declared symbols, so they
        # emit nothing -- unchanged from before.
        for tn in ["5|6", "39|41", "1|3"]:
            self.assertEqual(self.fmt.kotus_tags(wordmap(tn)), "")

    def test_acronym_emits_nothing(self):
        self.assertEqual(self.fmt.kotus_tags(wordmap("1", "A", upos="ACRONYM")), "")


class LexcEscapeIsUnchanged(unittest.TestCase):
    """lexc_escape itself is still correct; we only stopped applying it here."""

    def test_escapes_epsilon_zero(self):
        # lexc_escape must keep protecting a literal "0" in ordinary lexc text
        # (surface forms, lemmas). The fix does not touch this behaviour.
        self.assertEqual(lexc_escape("10"), "1%0")
        self.assertEqual(lexc_escape("60"), "6%0")
        self.assertEqual(lexc_escape("9"), "9")


@unittest.skipUnless(
    shutil.which("hfst-lexc") and shutil.which("hfst-fst2strings"),
    "hfst-lexc / hfst-fst2strings not available",
)
class FstCompilation(unittest.TestCase):
    """End-to-end: a declared [KTN=10] survives FST compilation intact.

    Without the multichar declaration the inner "0" is read as epsilon and
    "[KTN=10]" collapses to "[KTN=1]"; this is why both the declaration and
    the unescaped emission are needed.
    """

    def _compile_and_dump(self, lexc_text):
        with tempfile.TemporaryDirectory() as d:
            lexc = os.path.join(d, "t.lexc")
            fst = os.path.join(d, "t.hfst")
            with open(lexc, "w") as f:
                f.write(lexc_text)
            subprocess.run(
                ["hfst-lexc", lexc, "-o", fst],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            out = subprocess.run(
                ["hfst-fst2strings", fst],
                check=True, capture_output=True, text=True,
            )
            return out.stdout

    def test_declared_symbol_survives(self):
        dump = self._compile_and_dump(
            "Multichar_Symbols [KTN=9] [KTN=10]\n"
            "LEXICON Root\n"
            "[KTN=9]:nine # ;\n"
            "[KTN=10]:ten # ;\n"
        )
        self.assertIn("[KTN=10]", dump)
        self.assertIn("[KTN=9]", dump)

    def test_undeclared_symbol_loses_zero(self):
        dump = self._compile_and_dump(
            "Multichar_Symbols [KTN=9]\n"
            "LEXICON Root\n"
            "[KTN=10]:ten # ;\n"
        )
        # the 0 is eaten as epsilon -> 10 becomes 1
        self.assertIn("[KTN=1]", dump)
        self.assertNotIn("[KTN=10]", dump)

    def test_formatter_header_makes_tag_atomic(self):
        # Use the formatter's real declaration block, then a lexeme that emits
        # what kotus_tags() produces for a class-10 word.
        fmt = OmorFormatter(ktnkav=True)
        tag = fmt.kotus_tags(wordmap("10", "F"))
        header = fmt.multichars_lexc()
        dump = self._compile_and_dump(
            header + "\nLEXICON Root\n" + f"{tag}:ten # ;\n"
        )
        self.assertIn("[KTN=10]", dump)
        self.assertIn("[KAV=F]", dump)


if __name__ == "__main__":
    unittest.main()
