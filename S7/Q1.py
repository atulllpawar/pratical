import matplotlib.pyplot as plt 
courses = ["BCA", "BBA", "B.Com", "B.Sc", "BA"] 
students = [60, 45, 75, 50, 35] 
plt.figure(figsize=(8, 6)) 
plt.bar( 
courses, 
students, 
color=["black", "blue", "green", "orange", "yellow"] 
) 
plt.title("Number of Students Enrolled in Different Courses") 
plt.xlabel("Courses") 
plt.ylabel("Number of Students") 
plt.grid(axis="y", linestyle="--", alpha=0.5) 
plt.show() 