import pandas as pd
import json
import csv
l = []
data = """stud_id;Subject;grade
1;ТВиМС;60
2;МОР;70
3;ТВиМС;80
4;МОР;85
5;ТВиМС;100"""
data = data.replace(';', ',')
print(data)
l0 = data.split(sep='\n')
print(l0)
for i in l0:
    l.append(i.split(sep=';'))
#l = str(l)
#l = l.replace("'", "")
print(l)
#print(json.loads((l)))


