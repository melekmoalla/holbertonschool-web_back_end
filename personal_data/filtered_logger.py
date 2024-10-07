#!/usr/bin/env python3
"""Module to filter and obfuscate sensitive data in log messages."""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:

    for test in fields:
        message = re.sub(f"{test}=[^{separator}]*",
                         f"{test}={redaction}", message)
    return message
