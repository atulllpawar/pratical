import matplotlib.pyplot as plt 
from matplotlib_venn import venn2 
 
only_netflix = 40 
only_amazon = 25 
both = 20 
plt.figure(figsize=(6,6)) 
venn2(subsets=(only_netflix, only_amazon, both), 
      set_labels=("Netflix", "Amazon Prime")) 
 
plt.title("Customer Usage of Netflix and Amazon Prime") 
plt.show() 
labels = ["Only Netflix", "Only Amazon Prime", "Both"] 
values = [only_netflix, only_amazon, both] 
 
plt.pie(values, labels=labels, autopct="%1.1f%%", 
        colors=["red", "orange", "purple"]) 
plt.title("Customer Distribution") 
plt.show() 