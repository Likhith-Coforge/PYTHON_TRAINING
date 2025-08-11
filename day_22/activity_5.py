import pandas as pd

data = pd.read_csv('student.csv')

result = data[(data['gender']=='male') & (data['mark']>70) & (data['class'].isin(['Five','Four']))]

print(result)