import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_wine 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import ( 
    accuracy_score, 
    confusion_matrix, 
    classification_report 
) 
 
wine = load_wine() 
X = wine.data 
y = wine.target 
df = pd.DataFrame(X, columns=wine.feature_names) 
df["target"] = y 
 
print("\nFirst 5 rows:") 
print(df.head()) 
print("\nMissing values:") 
print(df.isnull().sum().sum()) 
X_train, X_test, y_train, y_test = train_test_split( 
    X, 
    y, 
    test_size=0.20, 
    random_state=42, 
    stratify=y 
) 
scaler = StandardScaler() 
X_train_scaled = scaler.fit_transform(X_train) 
X_test_scaled = scaler.transform(X_test) 
k_values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
results = [] 
for k in k_values: 
    knn = KNeighborsClassifier(n_neighbors=k) 
  
    knn.fit(X_train_scaled, y_train) 
 
    y_pred = knn.predict(X_test_scaled) 
 
    accuracy = accuracy_score(y_test, y_pred) 
 
    results.append({ 
        "K": k, 
        "Accuracy": accuracy 
    }) 
results_df = pd.DataFrame(results) 
print("\nPerformance for different K values:") 
print(results_df.to_string(index=False)) 
 
best_row = results_df.loc[ 
    results_df["Accuracy"].idxmax() 
] 
best_k = int(best_row["K"]) 
best_accuracy = best_row["Accuracy"] 
 
print("\nBest K:", best_k) 
print("Best Test Accuracy:", round(best_accuracy, 4)) 
plt.figure(figsize=(8, 5)) 
plt.plot( 
    results_df["K"].to_numpy(), 
    results_df["Accuracy"].to_numpy(), 
    marker="o", 
    linewidth=2 
) 
 
plt.xlabel("Value of K") 
plt.ylabel("Test Accuracy") 
plt.title("KNN Performance for Different Values of K") 
plt.xticks(k_values) 
plt.grid(True) 
plt.show() 
final_knn = KNeighborsClassifier( 
    n_neighbors=best_k 
) 
 
final_knn.fit( 
    X_train_scaled, 
    y_train 
) 
 
y_pred = final_knn.predict(X_test_scaled) 
 
print("\nFinal Model Evaluation") 
print("----------------------") 
print("K =", best_k) 
print( 
    "Accuracy =", 
    accuracy_score(y_test, y_pred) 
) 
print("\nConfusion Matrix:") 
print( 
    confusion_matrix( 
        y_test, 
        y_pred 
    ) 
) 
print("\nClassification Report:") 
print( 
    classification_report( 
        y_test, 
        y_pred, 
        target_names=wine.target_names 
    ) 
)