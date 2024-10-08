#!/usr/bin/env python3
"""Module to filter and obfuscate sensitive data in log messages."""
import logging
import re
from typing import List
import os
import mysql.connector
from mysql.connector import Error

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
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
    for test in fields:
        message = re.sub(
            f"{test}=[^{separator}]*",
            f"{test}={redaction}",
            message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by filtering sensitive information.
        """
        original_message = record.getMessage()
        redacted_message = filter_datum(
            self.fields,
            self.REDACTION,
            original_message,
            self.SEPARATOR)

        record.msg = redacted_message
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    function that takes no arguments and returns a logging.Logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    function that returns a connector to the
    database (mysql.connector.connection.MySQLConnection object).
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(user=username,
                                         password=password,
                                         host=host,
                                         database=database)
    return connection
