"""
Script execution for script fragments in content.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import textwrap

import six


def run_script(pycode):
    """Run the Python in `pycode`, and return a dict of the resulting globals."""
    # Fix up the whitespace in pycode.
    if pycode[0] == "\n":
        pycode = pycode[1:]
    pycode.rstrip()
    pycode = textwrap.dedent(pycode)

    # execute it.
    globs = {}
    six.exec_(pycode, globs, globs)  # pylint: disable=W0122

    return globs
