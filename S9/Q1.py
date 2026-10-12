import pandas as pd 
from sklearn.preprocessing import MinMaxScaler 
data = { 
'Product_ID': [101, 102, 103, 104, 105], 
'Price': [100, 200, 150, 300, 250], 
'Quantity_Sold': [10, 20, 15, 30, 25], 
'Discount': [5, 10, 0, 15, 20], 
'Revenue': [950, 3600, 2250, 7650, 5000] 
} 
df = pd.DataFrame(data) 
print("Original DataFrame:") 
print(df) 
scaler = MinMaxScaler() 
scaled_data = scaler.fit_transform(df) 
scaled_df = pd.DataFrame(scaled_data, columns=df.columns) 
print("\nDataFrame after Min-Max Scaling:") 
print(scaled_df)