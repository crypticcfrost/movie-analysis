import pandas as pd

def analyze_data(input_file):
    # Load the cleaned dataset
    df = pd.read_csv(input_file)

    # Example analysis: Describe the data to get basic statistics
    description = df.describe()

    # Example analysis: Top 5 movies by vote count
    top_movies_by_vote_count = df.nlargest(5, 'vote_count')[['title', 'vote_count']]

    return description, top_movies_by_vote_count
