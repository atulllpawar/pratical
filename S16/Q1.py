import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
data = { 
    "Study Hours": [2, 3, 4, 5, 6, 7, 8, 9], 
    "Attendance": [65, 70, 75, 80, 82, 88, 92, 95], 
    "Assignment Score": [55, 60, 65, 72, 75, 82, 88, 92], 
    "Exam Score": [50, 58, 63, 70, 74, 80, 87, 94] 
} 
df = pd.DataFrame(data) 
 
print("Student Performance Dataset:") 
print(df) 
correlation_matrix = df.corr() 
print("\nCorrelation Matrix:") 
print(correlation_matrix) 
plt.figure(figsize=(8, 6)) 
sns.heatmap( 
    correlation_matrix, 
    annot=True, 
    cmap="coolwarm", 
    fmt=".2f", 
    linewidths=0.5 
) 
 
plt.title("Correlation Heat Map of Student Performance") 
plt.show()