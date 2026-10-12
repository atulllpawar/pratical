import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib_venn import venn2 
from wordcloud import WordCloud 
data = { 
    "Book Title": [ 
        "The Great Gatsby", 
        "To Kill a Mockingbird", 
        "1984", 
        "The Hobbit", 
        "Pride and Prejudice", 
        "Harry Potter", 
        "The Alchemist", 
        "The Book Thief", 
        "The Kite Runner", 
        "The Silent Patient" 
    ], 
 
    "Author": [ 
        "F. Scott Fitzgerald", 
        "Harper Lee", 
        "George Orwell", 
        "J.R.R. Tolkien", 
        "Jane Austen", 
        "J.K. Rowling", 
        "Paulo Coelho", 
        "Markus Zusak", 
        "Khaled Hosseini", 
        "Alex Michaelides" 
    ], 
 
    "Publication Year": [ 
        1925, 
        1960, 
        1949, 
        1937, 
        1813, 
        1997, 
        1988, 
        2005, 
        2003, 
        2019 
    ], 
 
    "Average Rating": [ 
        4.2, 4.3, 4.2, 4.3, 4.3, 
        4.5, 3.9, 4.4, 4.3, 4.1 
    ], 
 
    "Number of Ratings": [ 
        500000, 600000, 700000, 800000, 900000, 
        1000000, 500000, 400000, 600000, 300000 
    ] 
} 
 
 
df = pd.DataFrame(data) 
 
print("Book Dataset:") 
print(df) 
 
authors_before_2000 = set( 
    df[df["Publication Year"] < 2000]["Author"] 
) 
authors_after_2000 = set( 
    df[df["Publication Year"] >= 2000]["Author"] 
) 
print("\nAuthors before 2000:") 
print(authors_before_2000) 
print("\nAuthors from 2000 onwards:") 
print(authors_after_2000) 
plt.figure(figsize=(8, 6)) 
 
venn2( 
    [authors_before_2000, authors_after_2000], 
    set_labels=("Before 2000", "2000 and After") 
) 
plt.title("Comparison of Authors by Publication Period") 
plt.show() 
titles = " ".join(df["Book Title"].astype(str)) 
wordcloud = WordCloud( 
width=800, 
height=400, 
background_color="white" 
).generate(titles) 
plt.figure(figsize=(10, 5)) 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.title("Word Cloud of Book Titles") 
plt.show()