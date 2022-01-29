# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)
    
    return records
