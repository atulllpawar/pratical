import pandas as pd 
data = { 
    'Employee_ID': [101, 102, 103, 104, 105, 105], 
    'Age': [25, 30, None, 45, 120, None], 
    'Department': ['HR', 'IT', 'Finance', None, 'IT', 'IT'], 
    'Experience': [2, 5, None, 20, 3, 3], 
    'Performance_Score': [85, 90, 88, None, 95, 95] 
} 
df = pd.DataFrame(data) 
print("Original Data:") 
print(df) 
df['Age'] = df['Age'].fillna(df['Age'].mean()) 
df['Experience'] = df['Experience'].fillna(df['Experience'].mean()) 
df['Performance_Score'] = df['Performance_Score'].fillna(df['Performance_Score'].mean()) 
 
df['Department'] = df['Department'].fillna('unknown') 
print("\nData after handling missing values:") 
print(df) 
df.drop_duplicates(inplace=True) 
print("\nData after removing duplicates:") 
print(df) 
Q1 = df['Age'].quantile(0.25) 
Q3 = df['Age'].quantile(0.75) 
 
IQR = Q3 - Q1 
 
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR 
 
outliers = df[ 
    (df['Age'] < lower_bound) | 
    (df['Age'] > upper_bound) 
] 
print("\nOutliers in Age:") 
print(outliers) 
 
print("\nFinal Cleaned Data:") 
print(df) 