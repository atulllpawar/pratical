 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
 
data1 = { 
    "Brand": ["Samsung", "Apple", "OnePlus", "Xiaomi", "Vivo"], 
    "Model": ["Galaxy S24", "iPhone 15", "OnePlus 12", "Redmi Note 13", "Vivo V30"], 
    "Price": [80000, 70000, 60000, 25000, 30000], 
    "RAM": [8, 6, 12, 8, 8] 
} 
 
df1 = pd.DataFrame(data1) 
 
data2 = { 
    "Model": ["Galaxy S24", "iPhone 15", "OnePlus 12", "Redmi Note 13", "Vivo V30"], 
    "Storage": [256, 128, 256, 128, 256], 
    "Battery_Capacity": [4000, 3349, 5400, 5000, 5000], 
    "Operating_System": [ 
        "Android", 
        "iOS", 
        "Android", 
        "Android", 
        "Android" 
    ] 
} 
df2 = pd.DataFrame(data2) 
 
print("DataFrame 1:") 
print(df1) 
 
print("\nDataFrame 2:") 
print(df2) 
 
merged_df = pd.merge( 
    df1, 
    df2, 
    on="Model", 
    how="inner" 
)  
print("\nMerged DataFrame:") 
print(merged_df) 
 
label_encoder = LabelEncoder() 
 
merged_df["Brand_Encoded"] = label_encoder.fit_transform( 
    merged_df["Brand"] 
) 
print("\nAfter Label Encoding:") 
print(merged_df) 
merged_df = pd.get_dummies( 
    merged_df, 
    columns=["Operating_System"], 
    dtype=int 
)  
print("\nFinal Transformed DataFrame:") 
print(merged_df)