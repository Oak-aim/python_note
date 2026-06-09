import csv
import pandas as pd

df = pd.read_csv('sample.csv')
print(df)

data = {
    "Name": ["Alice", "Bob"],
    "Age": [30, 25],
    "City": ["New York", "Los Angeles"]
}

df = pd.DataFrame(data)
df.to_csv('sample.csv', index=False)

with open('data.csv', mode='r', encoding='utf-8') as file:    
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('data.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Charlie", 28, "Chicago"])
    writer.writerow(["Diana", 22, "Houston"])
