#!/usr/bin/env python3

"""
filter_datum file
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    filter_datum file
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]+",
            f"{field}={redaction}",
            message)
    return message
