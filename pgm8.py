import pandas as pd
df = pd.read_csv("student.csv")
df1 = df.copy()

for col in df.columns[1:]:
    mean = df[col].mean(skipna=True)
    df1[col] = df1[col].fillna(mean)

avg = df1.iloc[:, 1:].mean()

print("Cleaned Data:")
print(df1)
print("Average Marks per Subject:")
print(avg)
