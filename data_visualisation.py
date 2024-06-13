import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(input_file):

    df = pd.read_csv(input_file)

    plt.figure(figsize=(10, 6))
    plt.hist(df['popularity'], bins=30, color='blue', edgecolor='black')
    plt.title('Distribution of Movie Popularity')
    plt.xlabel('Popularity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    top_10_movies = df.nlargest(10, 'vote_count')
    plt.figure(figsize=(12, 8))
    plt.barh(top_10_movies['title'], top_10_movies['vote_count'], color='green')
    plt.xlabel('Vote Count')
    plt.title('Top 10 Movies by Vote Count')
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.show()
