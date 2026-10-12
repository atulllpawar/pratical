import pandas as pd 
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer 
data = { 
"Temperature": [20, 25, 30, 35, 40], 
"Humidity": [40, 50, 60, 70, 80], 
"Wind-Speed": [10, 15, 20, 25, 30], 
"Pressure": [1000, 1010, 1020, 1030, 1040], 
"Rainfall": [50, 100, 150, 200, 250] 
} 
df = pd.DataFrame(data) 
print("Original Dataset:") 
print(df) 
minmax_scaler = MinMaxScaler() 
minmax_data = minmax_scaler.fit_transform(df) 
minmax_df = pd.DataFrame( 
minmax_data, 
columns=df.columns 
) 
print("\nMin-Max Scaled Data:") 
print(minmax_df) 
standard_scaler = StandardScaler() 
standard_data = standard_scaler.fit_transform(df) 
standard_df = pd.DataFrame( 
standard_data, 
columns=df.columns 
) 
print("\nStandardized Data:") 
print(standard_df) 
normalizer = Normalizer() 
normalized_data = normalizer.fit_transform(df) 
normalized_df = pd.DataFrame( 
normalized_data, 
columns=df.columns 
) 
print("\nNormalized Data:") 
print(normalized_df) 