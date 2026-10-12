import pandas as pd 
 
data = { 
    "Book_ID": ["B001","B002","B003","B004","B005","B006","B007","B008","B009","B010"], 
    "Book_Price": [100,550,200,250,1000,350,100,450,500,150] 
} 
book_records = pd.DataFrame(data) 
 
print("Original Book Records:") 
print(book_records) 
 
book_records["Price_Category"] = pd.cut( 
    book_records["Book_Price"], 
    bins=3, 
    labels=[ 
        "Low", 
        "Medium", 
        "High" 
    ] 
) 
print("\nDiscretized Book Records:") 
print(book_records) 