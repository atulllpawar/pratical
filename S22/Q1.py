import pandas as pd 
from sklearn.preprocessing import Normalizer 
data = { 
"City": ["Mumbai","Pune","Delhi","Ahmedabad","Bengaluru"], 
"House_Type": ["1BHK","2BHK","3BHK","2BHK","1BHK"], 
"House_Area": [550,900,1400,1000,600], 
"Number_of_Rooms": [ 2,3,4,3,2], 
"Monthly_Rent": [18000,25000,40000,22000,20000] 
} 
df = pd.DataFrame(data) 
print("Original Dataset:") 
print(df) 
numerical_columns = [ 
"House_Area", 
"Number_of_Rooms", 
"Monthly_Rent" 
] 
X = df[numerical_columns] 
normalizer = Normalizer() 
normalized_data = normalizer.fit_transform(X) 
normalized_df = pd.DataFrame( 
normalized_data, 
columns=numerical_columns 
) 
print("\nNormalized Data:") 
print(normalized_df)