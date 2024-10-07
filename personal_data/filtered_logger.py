#!/usr/bin/env python3
"""Module to filter and obfuscate sensitive data in log messages."""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): The list of fields to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message to be filtered.
        separator (str): The field separator in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]+"
    return re.sub(pattern, lambda match: f"{match.group(1)}={redaction}", message)
