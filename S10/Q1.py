import matplotlib.pyplot as plt  
transport = ["Bus", "Train", "Car", "Bike", "Bicycle"] 
employees = [120, 80, 60, 90, 30] 
colors = ["gold", "lightblue", "lightgreen", "orange", "violet"] 
plt.figure(figsize=(7,7)) 
plt.pie( 
employees, 
labels=transport, 
autopct='%1.1f%%', 
colors=colors, 
startangle=90, 
shadow=True 
) 
plt.title("Preferred Mode of Transportation Among Employees") 
plt.axis('equal')    
plt.show()