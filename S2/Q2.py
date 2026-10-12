import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori, association_rules 
 
 
transactions = [ 
    ["Video Lecture", "Quiz"], 
    ["Video Lecture", "Assignment"], 
    ["Quiz", "Discussion Forum"], 
    ["Video Lecture", "Quiz", "Assignment"], 
    ["Assignment", "Discussion Forum"], 
    ["Video Lecture", "Certificate"], 
    ["Quiz", "Certificate"], 
    ["Video Lecture", "Quiz"], 
    ["Assignment", "Certificate"], 
    ["Video Lecture", "Quiz", "Certificate"] 
] 
 
te = TransactionEncoder() 
te_array = te.fit(transactions).transform(transactions) 
df = pd.DataFrame( 
    te_array, 
    columns=te.columns_ 
) 
 
print("\nOne-Hot Encoded Dataset:") 
print(df) 
 
support_values = [0.2, 0.3] 
for min_support in support_values: 
 
    print("\n==========================================") 
    print("Minimum Support =", min_support) 
    print("==========================================") 
    frequent_itemsets = apriori( 
        df, 
        min_support=min_support, 
        use_colnames=True 
    ) 
    print("\nFrequent Itemsets:") 
    print(frequent_itemsets) 
 
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