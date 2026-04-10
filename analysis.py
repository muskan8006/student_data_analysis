import pandas as pd

#  LOAD DATA FROM CSV
df = pd.read_csv("student_dataset_v2.csv")

print(" FIRST 10 ROWS ")
print(df.head(10))

print("\n LAST 5 ROWS ")
print(df.tail(5))

#  UNDERSTAND DATA
print("\n SHAPE OF DATASET ")
print(df.shape)

print("\n COLUMN NAMES")
print(df.columns)

print("\n DATA TYPES")
print(df.dtypes)

print("\n DATA INFO ")
df.info()
#  DATA CLEANING
print("\n MISSING VALUES BEFORE ")
print(df.isnull().sum())

# Fill missing values in Marks column
if 'Marks' in df.columns:
    df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print("\n MISSING VALUES AFTER")
print(df.isnull().sum())
#  BASIC ANALYSIS
if 'Attendance' in df.columns:
    print("\n HIGHEST ATTENDANCE")
    print(df['Attendance'].max())

if 'StudyHours' in df.columns:
    print("\n AVERAGE STUDY HOURS ")
    print(df['StudyHours'].mean())
    
#  SUMMARY STATISTICS

print("\n DATA SUMMARY ")
print(df.describe())
# END
print("\n Analysis Completed Successfully!")