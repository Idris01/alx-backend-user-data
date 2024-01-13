#!/usr/bin/env python3
"""This module define a filterred logger function
"""
import logging
import re
from typing import Sequence, Type
import mysql.connector as connector
import os

MySQLConnection = connector.connection.MySQLConnection
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: Sequence[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Perform filtering and replacement"""
    for fld in fields:
        message = re.sub(fld + "=" + "[^;]*", fld + "=" + redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Sequence[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format for the log message"""
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Get a new logger
    """
    this_logger = logging.getLogger("user_data")
    this_logger.setLevel(logging.INFO)
    this_logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    this_logger.setHandler(logging.StreamHandler(stream))
    return this_logger


def get_db() -> MySQLConnection:
    """get connection to database
    """
    connection = connector.connect(
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            database=os.getenv("PERSONAL_DATA_DB_NAME"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""))
    return connection


def main() -> None:
    """query and log all users in the database
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT *  FROM users")
    allfields = (
            "name", "email", "phone", "ssn",
            "password", "ip", "last_login", "user_agent")
    template = "={};".join(allfields) + "={};"
    formatter = RedactingFormatter(fields=PII_FIELDS)

    for row in cursor:
        log_record = logging.LogRecord(
                "user_data", logging.INFO,
                None, None, template.format(*row), None, None)
        print(formatter.format(log_record))


if __name__ == "__main__":
    main()
