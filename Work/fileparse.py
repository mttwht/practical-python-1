# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=[], types=[], has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("'select' argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Skip headers if not has_headers
        if has_headers:
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
			# Convert to dict if has_headers
            if has_headers:
                record = dict(zip(headers, row))
            # Convert to tuple if not has_headers
            else:
                record = tuple(row)
            records.append(record)
    return records
