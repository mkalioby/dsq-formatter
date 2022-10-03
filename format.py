#! /usr/bin/env python3
import sys
import json

from prettytable import PrettyTable

data = json.loads(sys.stdin.read())
x=None

header =None
for record in data:
   # print(record.values())
    if x is None:
        x = PrettyTable()
        header = record.keys()
        x.field_names = record.keys()
    l=[]
    for k in header:
        l.append(record[k])
    x.add_rows([l])
print(x)

