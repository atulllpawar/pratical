import pandas as pd 
import matplotlib.pyplot as plt 
 
data = { 
    "Fuel_Efficiency": [18, 22, 20, 25,80], 
    "Engine_Power": [120, 150, 135, 180, 500], 
    "Vehicle_Weight": [1200, 1400, 1300, 1500, 1600], 
    "Engine_Size": [1.5, 1.8, 1.6, 2.0, 12.5], 
    "Acceleration": [10.5, 9.2, 10.0, 8.5, 6.0] 
} 
 
df = pd.DataFrame(data) 
 
print("Vehicle DataFrame:") 
print(df) 
 
plt.figure(figsize=(10, 5)) 
 
plt.subplot(1, 2, 1) 
plt.boxplot(df["Fuel_Efficiency"]) 
plt.title("Box Plot - Fuel Efficiency") 
plt.ylabel("Fuel Efficiency") 
 
plt.subplot(1, 2, 2) 
plt.boxplot(df["Engine_Power"]) 
plt.title("Box Plot - Engine Power") 
plt.ylabel("Engine Power") 
 
plt.tight_layout() 
plt.show() 
 
 
def find_outliers(column): 
    Q1 = df[column].quantile(0.25) 
    Q3 = df[column].quantile(0.75) 
 
    IQR = Q3 - Q1 
 
    lower_limit = Q1 - 1.5 * IQR 
    upper_limit = Q3 + 1.5 * IQR 
 
    outliers = df[ 
        (df[column] < lower_limit) | 
        (df[column] > upper_limit) 
    ][column] 
 
    return Q1, Q3, lower_limit, upper_limit, outliers 
 
 
q1, q3, lower, upper, outliers = find_outliers("Fuel_Efficiency") 
 
print("\nFuel Efficiency:") 
print("Q1 =", q1) 
print("Q3 =", q3) 
print("Lower Limit =", lower) 
print("Upper Limit =", upper) 
print("Outliers =", list(outliers)) 
 
q1, q3, lower, upper, outliers = find_outliers("Engine_Power") 
 
print("\nEngine Power:") 
print("Q1 =", q1) 
print("Q3 =", q3) 
print("Lower Limit =", lower) 
print("Upper Limit =", upper) 
print("Outliers =", list(outliers)) 
