import matplotlib.pyplot as plt
import numpy as np

'''def scatter_plot(data):
    plt.scatter(data['Release Year'], data['Rating'])
    plt.xlabel('Release Year')
    plt.ylabel('Rating')
    plt.title('Rating vs Release Year')
    plt.show()'''
    
def histogram(data):
    
    plt.hist(data['Rating'], bins=20, edgecolor='black')
   
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title("Album Rating Distribution")
    
    plt.grid(axis = "y", alpha=0.75)
    
    plt.show()