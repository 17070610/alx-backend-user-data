#!/usr/bin/env python3
import re
"""Task 0 module"""

def filter_datum(fields, redaction, message, separator):
    pattern = '({})=[^{}]*'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1={}'.format(redaction), message)
