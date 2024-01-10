#!/usr/bin/env python3
"""This module define a filterred logger function
"""
import logging
import re
from typing import List

pat = r"{}=(?P<{}>.*?){}"
fd = re.findall


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Perform filtering and replacement"""
    n = fd("".join([pat.format(fi, fi, separator) for fi in fields]), message)
    value_pattern = "|".join(n[0])
    return re.subn(value_pattern, redaction, message)[0]
