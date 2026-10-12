import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("sales.csv") 
print("Sales Data:") 
print(df) 
plt.figure(figsize=(10, 6)) 
plt.boxplot( 
    df["Sales"].dropna(), 
    patch_artist=True, 
    boxprops=dict(facecolor="skyblue", color="blue"), 
    medianprops=dict(color="red", linewidth=2), 
    whiskerprops=dict(color="black"), 
    capprops=dict(color="black"), 
    flierprops=dict( 
        marker="o", 
        markerfacecolor="red", 
        markeredgecolor="black", 
        markersize=8 
    ) 
) 
plt.title("Daily Sales Distribution and Outliers", fontsize=16) 
plt.xlabel("Sales", fontsize=12) 
plt.ylabel("Sales Amount", fontsize=12) 
 
plt.grid(axis="y", linestyle="--", alpha=0.7) 
plt.show() 