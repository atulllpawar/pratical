import pandas as pd 
from sklearn.preprocessing import StandardScaler 
data = { 
    "Age": [22, 25, 28, 32, 35], 
    "Salary": [25000, 30000, 40000, 50000, 60000], 
    "Experience": [1, 3, 5, 8, 10], 
    "Working_Hours": [35, 40, 42, 45, 50], 
    "Performance_Score": [60, 65, 72, 80, 90] 
} 
df = pd.DataFrame(data) 
 
print("Original Dataset:") 
print(df) 
scaler = StandardScaler() 
standardized_data = scaler.fit_transform(df) 
standardized_df = pd.DataFrame( 
    standardized_data, 
    columns=df.columns 
) 
print("\nStandardized Data:") 
print(standardized_df) 