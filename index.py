from data_cleaning import clean_data
from data_analysis import analyze_data
from data_visualisation import visualize_data

raw_file_path = 'data/movie_dataset.csv'
cleaned_file_path = 'data/cleaned_movie_dataset.csv'

df_cleaned = clean_data(raw_file_path, cleaned_file_path)
print("Data Cleaning Completed")
print(df_cleaned.head())

description, top_movies_by_vote_count = analyze_data(cleaned_file_path)
print("\nBasic Statistics:")
print(description)
print("\nTop 5 Movies by Vote Count:")
print(top_movies_by_vote_count)

visualize_data(cleaned_file_path)
print("Data Visualization Completed")