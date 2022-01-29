# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=[], types=[], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("'select' argument requires column headers")
    
    rows = csv.reader(lines)
    # Skip headers if not has_headers
    if has_headers:
        headers = next(rows)
        # Filter headers if 'select' is provided
        if select:
            indexes = [headers.index(s) for s in select]
            headers = select
        
    records = []
    row_no = 0
    for row in rows:
        row_no += 1
        if not row:
            continue
        # Filter columns if 'select' is provided
        if select:
            row = [row[i] for i in indexes]
        # Type convert if 'types' is provided
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {row_no}: Couldnt convert {row}')
                    print(' ', e)
        # Convert to dict if has_headers
        if has_headers:
            record = dict(zip(headers, row))
        # Convert to tuple if not has_headers
        else:
            record = tuple(row)
        records.append(record)
    return records
