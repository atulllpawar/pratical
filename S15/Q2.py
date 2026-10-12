 
import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori, association_rules 
transactions = [ 
    ["Basmati Rice", "Toor Dal", "Turmeric Powder", "Cooking Oil"], 
    ["Atta", "Sugar", "Tea", "Milk"], 
    ["Rice", "Moong Dal", "Salt", "Cooking Oil"], 
    ["Wheat Flour", "Chickpeas", "Turmeric Powder", "Cumin Seeds"], 
    ["Poha", "Peanuts", "Onions", "Cooking Oil"], 
    ["Basmati Rice", "Paneer", "Garam Masala", "Tomatoes"], 
    ["Atta", "Potatoes", "Onions", "Cooking Oil"] 
] 
te= TransactionEncoder() 
te_array = te.fit(transactions).transform(transactions) 
df = pd.DataFrame( 
    te_array, 
    columns=te.columns_ 
) 
print("\nOne-Hot Encoded Dataset:") 
print(df) 
 
print("\nMissing Values after Encoding:") 
print(df.isnull().sum()) 
df = df.fillna(False) 
support_values = [0.3, 0.4] 
for min_support in support_values: 
 
    print("\n=======") 
    print("Minimum Support =", min_support) 
    print("=========")
    frequent_itemsets = apriori( 
        df, 
        min_support=min_support, 
        use_colnames=True 
    ) 
    print("\nFrequent Itemsets:") 
    print(frequent_itemsets) 
    if len(frequent_itemsets) > 1: 
 
        rules = association_rules( 
            frequent_itemsets, 
            metric="confidence", 
            min_threshold=0.5 
        ) 
        print("\nAssociation Rules:") 
 
        if rules.empty: 
            print("No association rules found.") 
        else: 
            print( 
                rules[ 
                    [ 
                        "antecedents", 
                        "consequents", 
                        "support", 
                        "confidence", 
                        "lift" 
                    ] 
                ] 
            ) 
 
    else: 
        print("\nNo association rules found.") 