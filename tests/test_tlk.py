import pytest
from pathlib import Path
import lib_scan as ls


class TestTLK:

    def test_init(self):

        library_scan = ls.LibraryScan()

        assert isinstance(library_scan, ls.LibraryScan)
