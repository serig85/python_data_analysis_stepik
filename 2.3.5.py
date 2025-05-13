import pandas as pd
import numpy as np
from io import StringIO
import json
import csv
l = []
data = """stud_id;Subject;grade
1;ТВиМС;60
2;МОР;70
3;ТВиМС;80
4;МОР;85
5;ТВиМС;91"""

#df = pd.DataFrame(data)

df = pd.read_csv(StringIO(data), sep=";")
df['EurGrad'] = (df['grade'].apply
                 (lambda x:
                      'A' if x >= 90 and x <= 100
                 else 'B' if x >= 85 and x <= 89
                 else 'C' if x >= 75 and x <= 84
                 else 'D' if x >= 65 and x <= 74
                 else 'E' if x >= 60 and x <= 64
                 else 'F' if x >= 0 and x < 60
                 else ''))
print(df)
