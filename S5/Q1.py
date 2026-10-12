import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
customer_DataFrame = pd.DataFrame({ 
    "Customer_ID": [101, 102, 103, 104, 105], 
    "Gender": ["Male", "Female", "Male", "Female", "Male"], 
    "City": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Ahmedabad"], 
    "Membership_Type": ["Gold", "Silver", "Platinum", "Gold", "Silver"] 
}) 
print("DataFrame Before Label Encoding:") 
print(customer_DataFrame) 
label_encoder = LabelEncoder() 
for column in ["Gender", "City", "Membership_Type"]: 
    customer_DataFrame[column] = label_encoder.fit_transform( 
        customer_DataFrame[column] 
    ) 
print("\nDataFrame After Label Encoding:") 
print(customer_DataFrame) 