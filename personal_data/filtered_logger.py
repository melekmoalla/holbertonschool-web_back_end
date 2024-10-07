#!/usr/bin/env python3

"""
filter_datum file
"""

import re


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]+",
            f"{field}={redaction}",
            message)
    return message


"""def filter_datum(fields, redaction, message, separator):
    value = ""
    ph = ""
    list = message.split(separator)

    for i in list[:-1]:
        lis= i.split('=')
        for b in fields:
            if b == lis[0]:
                value += lis[0]+'='+redaction
                break
        if value != "":
            ph += value + separator
            value = ""
        else:
            ph += i + separator
    return ph"""
