#!/usr/bin/env python3
"""Module to filter and obfuscate sensitive data in log messages."""
import re
from typing import List


def filter_datum(
           fields,
        redaction,
        message,
        separator) -> str:

    pattern = f"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(
        pattern,
        lambda match: f"{match.group(1)}={redaction}",
        message)
