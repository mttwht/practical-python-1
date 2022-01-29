# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=[]):
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
            
            if select:
                record = dict(zip(select, [record[s] for s in select]))
            
            records.append(record)
    
    return records
