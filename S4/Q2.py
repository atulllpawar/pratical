import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
df = pd.read_csv("Ecommerce Customers.csv") 
print("E-commerce Customer Dataset:") 
print(df) 
 
df = df.dropna() 
 
X = df[ 
    [ 
        "Avg. Session Length", 
        "Time on App", 
        "Time on Website", 
        "Length of Membership", 
        "Yearly Amount Spent" 
    ] 
] 
print("\nSelected Numerical Features:") 
print(X) 
 
kmeans = KMeans( 
    n_clusters=3, 
    random_state=42, 
    n_init=10 
) 
clusters = kmeans.fit_predict(X) 
centroids = kmeans.cluster_centers_ 
print("\nCluster Labels:") 
print(clusters) 
 
print("\nCluster Centroids:") 
print(centroids) 
df["Cluster"] = clusters 
print("\nDataset with Cluster Labels:") 
print(df) 
plt.figure(figsize=(8, 6)) 
plt.scatter( 
    X.iloc[clusters == 0, 0], 
    X.iloc[clusters == 0, 1], 
    c="red", 
    label="Cluster 1" 
) 
 
plt.scatter( 
    X.iloc[clusters == 1, 0], 
    X.iloc[clusters == 1, 1], 
    c="blue", 
    label="Cluster 2" 
) 
plt.scatter( 
    X.iloc[clusters == 2, 0], 
    X.iloc[clusters == 2, 1], 
    c="green", 
    label="Cluster 3" 
) 
plt.scatter( 
    centroids[:, 0], 
    centroids[:, 1], 
    c="black", 
    marker="X", 
    s=200, 
    label="Centroids" 
) 
plt.xlabel("Avg. Session Length") 
plt.ylabel("Time on App") 
plt.title("K-Means Clustering of E-commerce Customers (K=3)") 
plt.legend() 
plt.grid(True) 
plt.show() 