import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage 
from sklearn.preprocessing import StandardScaler 
data = { 
"Product": [" A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
"Price": [20, 25, 80, 75, 18, 100, 30, 90, 22, 95], 
"Rating": [4.2, 4.5, 4.8, 4.7, 4.1, 4.9, 4.3, 4.8, 4.2, 4.9], 
"Sales": [500, 650, 1200, 1100, 450, 1500, 700, 1400, 550, 1450] 
} 
df = pd.DataFrame(data) 
X = df[["Price", "Rating", "Sales"]] 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
linked = linkage(X_scaled, method='ward') 
plt.figure(figsize=(10, 6)) 
dendrogram(linked, 
labels=df["Product"].values, 
leaf_rotation=90) 
plt.title("Dendrogram of Products") 
plt.xlabel("Products") 
plt.ylabel("Euclidean Distance") 
plt.show() 