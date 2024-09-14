import pandas as pd
source = pd.read_csv("EMP.csv")
print("TestCase 01: Following are the column name in source file \n")
print(source.columns)
print("\n")

print("TestCase 02: Row X Columns in the source file \n")
print(source.shape)
print("\n")

print("TestCase 03: No's of row under each column \n")
print(source.count())
print("\n")


print("TestCase 04: Duplicate records in source file \n")
print(source.duplicated().sum())
print("\n")

print("TestCase 05: check if null exists in phone_number \n")
print(source[source['phone_number'].isnull()])
print("\n")

print("TestCase 06: Unique value of employee_id \n")
print(source['employee_id'].unique())
print("\n")