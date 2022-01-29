# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=[], types=[]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # Filter headers if 'select' is provided
        if select:
            indexes = [headers.index(s) for s in select]
            headers = select
            
        records = []
        for row in rows:
            if not row:
                continue
            # Filter columns if 'select' is provided
            if select:
                row = [row[i] for i in indexes]
            # Type convert if 'types' is provided
            if types:
                row = [func(val) for func, val in zip(types, row)]
            record = dict(zip(headers, row))
            records.append(record)
    return records
