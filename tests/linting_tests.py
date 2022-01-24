import os
import sys
import unittest
import subprocess
import pytest
import pycodestyle
from pylint.epylint import lint
from django.conf import settings


class TestLinting(unittest.TestCase):
    """ Test pep8 """

    def test_pep8(self):
        """ Testea si el codigo cumple con el PEP 8 """
        print(">>> Corriendo pycodestyle (PEP 8) <<<")
        excluded_patterns = ['migrations', 'management']
        excluded_files = [
            '__init__.py',
            'apps.py',
            'init.py',
            'settings.py',
            'tests.py',
        ]
        pyfiles = []
        for dirpath, _, files in os.walk(settings.BASE_DIR):
            for file in files:
                if file.endswith('.py') and file not in excluded_files \
                        and not any((m in dirpath for m in excluded_patterns)):
                    pyfiles.append(os.path.join(dirpath, file))
        style = pycodestyle.StyleGuide(quiet=False, ignore=['W292'])
        result = style.check_files(pyfiles)
        self.assertEqual(result.total_errors, 0,
                         "Se encontraron errores de estilo de código")
