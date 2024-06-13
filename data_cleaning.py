import pandas as pd

def clean_data(input_file, output_file):

    df = pd.read_csv(input_file)

    # Drop columns with a high number of missing values or irrelevant columns
    df_cleaned = df.drop(columns=['Unnamed: 0'], errors='ignore')

    # Fill or drop rows with missing data
    df_cleaned = df_cleaned.dropna()

    # Resetting index after cleaning
    df_cleaned.reset_index(drop=True, inplace=True)

    # Save the cleaned data to a new CSV file
    df_cleaned.to_csv(output_file, index=False)

    return df_cleaned