"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

def plot_relational_plot(df):
    """Generates a scatter plot showing the relationship between TL and IN."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='IN', y='TL', alpha=0.5, ax=ax)
    plt.title('Total Length vs. Internodes')
    plt.xlabel('Number of Internodes')
    plt.ylabel('Total Length')
    plt.savefig('relational_plot.png')
    plt.close()

def plot_categorical_plot(df):
    """Generates a categorical plot showing the count of samples per TREE type."""
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='TREE', order=df['TREE'].value_counts().index, ax=ax)
    plt.title('Sample Count by Tree Type')
    plt.xticks(rotation=45)
    plt.savefig('categorical_plot.png')
    plt.close()

def plot_statistical_plot(df):
    """Generates a histogram for the distribution of TL (Total Length)."""
    fig, ax = plt.subplots()
    sns.histplot(df['TL'], bins=30, kde=True, ax=ax)
    plt.title('Distribution of Total Length')
    plt.savefig('statistical_plot.png')
    plt.close()

def statistical_analysis(df, col: str):
    """Calculates statistical moments (mean, std, skewness, kurtosis) for a given column."""
    data = df[col].dropna()
    mean = np.mean(data)
    stddev = np.std(data)
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    """Preprocesses the data by handling missing values and converting types."""
    df.replace("?", np.nan, inplace=True)
    df['TL'] = pd.to_numeric(df['TL'], errors='coerce')
    df['IN'] = pd.to_numeric(df['IN'], errors='coerce')
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df

def writing(moments, col):
    """Displays statistical analysis results."""
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    skew_desc = 'right-skewed' if moments[2] > 0 else 'left-skewed' if moments[2] < 0 else 'not skewed'
    kurt_desc = 'leptokurtic' if moments[3] > 0 else 'platykurtic' if moments[3] < 0 else 'mesokurtic'
    print(f'The data was {skew_desc} and {kurt_desc}.')

def main():
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("Error: The file 'data.csv' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return
    
    df = preprocessing(df)
    col = 'TL'  # Chosen numerical column for analysis
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    
if __name__ == '__main__':
    main()