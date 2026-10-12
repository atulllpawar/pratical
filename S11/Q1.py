import matplotlib.pyplot as plt 
departments = ["HR", "Finance", "IT", "Sales", "Marketing"] 
employees = [20, 30, 50, 40, 25] 
 
plt.figure(figsize=(8, 6)) 
 
plt.bar( 
    departments, 
    employees, 
    color=["red", "blue", "green", "orange", "purple"] 
) 
plt.title("Distribution of Employees Among Departments") 
plt.xlabel("Departments") 
plt.ylabel("Number of Employees") 
plt.grid(axis="y", linestyle="--", alpha=0.5) 
plt.show() 