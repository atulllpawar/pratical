import pandas as pd 
import plotly.express as px 
import matplotlib.pyplot as plt 
import squarify 
 
df = pd.read_csv("worldcities.csv") 
 
print("World Cities Dataset:") 
print(df.head()) 
 
print("\nMissing Values:") 
print(df.isnull().sum()) 
 
df = df.dropna( 
    subset=[ 
        "city", 
        "country", 
        "latitude", 
        "longitude", 
        "population" 
    ] 
) 
fig = px.scatter_geo( 
    df, 
    lat="latitude", 
    lon="longitude", 
    size="population", 
    color="country", 
    hover_name="city", 
    hover_data=["population"], 
    title="World Cities - Population Visualization", 
    projection="natural earth" 
) 
 
fig.show() 
 
top_cities = df.nlargest(20, "population") 
 
plt.figure(figsize=(12, 7)) 
 
squarify.plot( 
    sizes=top_cities["population"], 
    label=top_cities["city"], 
    color=["red","blue","green", "orange","purple","cyan","yellow","pink","brown", 
           "lime","coral","teal","gold","violet","navy","magenta","gray","olive","skyblue","salmon"], 
    alpha=0.8 
) 
 
plt.title("Population Distribution of Top 20 World Cities") 
plt.axis("off") 
plt.show() 