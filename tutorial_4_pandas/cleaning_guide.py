import pandas as pd

print(pd.__version__)

df = pd.read_csv("employees.csv")

# print(df)
print(f"Shape: {df.shape}")

print("----------")
print(f"Info: {df.info()}")

print("----------")
print(f"Top 5 rows: {df.head()}")
print("----------")
print(f"Top 3 rows: {df.head(3)}")

print("----------")
print(f"Missing Values Count: {df.isnull().sum()}")

print("----------")
print(f"Before removing: {df.shape}")
df = df.drop_duplicates()
print(f"After removing: {df.shape}")



print("----------")

# print(df["department"].fillna("Unknown"))
df["department"]=df["department"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["email"] = df["email"].fillna("not_available@company.com")
print("Before cleaning salary:",df["salary"])
avg_salary = df["salary"].mean()
df["salary"] = df["salary"].fillna(avg_salary)
df["joining_date"] = df["joining_date"].fillna("2015-01-01")

print("After cleaning salary:",df["salary"])

print("----------")
df = df.dropna(subset=['name'])
print(df)

print("----------")
df["department"] = df["department"].str.strip().str.upper()

print(df["department"].unique())

print("----------")
print(f"Missing Values Count: {df.isnull().sum()}")

df.to_csv("employees_cleaned.csv", index=False)