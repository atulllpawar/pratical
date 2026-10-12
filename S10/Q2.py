import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
df = pd.read_csv("house_prices.csv") 
print("First 5 records:") 
print(df.head()) 
print("\nMissing Values:") 
print(df.isnull().sum()) 
X = df.drop("Price_INR", axis=1) 
y = df["Price_INR"] 
X = pd.get_dummies(X, columns=["Location"], drop_first=True) 
print("\nFeatures after encoding:") 
print(X.head()) 
X_train, X_test, y_train, y_test = train_test_split( 
X, 
y, 
test_size=0.20, 
random_state=42 
) 
model = RandomForestRegressor( 
n_estimators=200, 
random_state=42, 
n_jobs=-1 
) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
mae = mean_absolute_error(y_test, y_pred) 
mse = mean_squared_error(y_test, y_pred) 
rmse = np.sqrt(mse) 
r2 = r2_score(y_test, y_pred) 
print("MODEL PERFORMANCE") 
print(f"Mean Absolute Error (MAE): ₹{mae:,.2f}") 
print(f"Mean Squared Error (MSE): ₹{mse:,.2f}") 
print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.2f}") 
print(f"R² Score: {r2:.4f}") 
 
results = pd.DataFrame({ 
    "Actual Price": y_test.values, 
    "Predicted Price": y_pred 
})