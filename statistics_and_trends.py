"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x='IN', y='TL', data=df, ax=ax, alpha=0.5)
    ax.set_title("Scatter Plot of Total Length vs Internodes Count")
    ax.set_xlabel("Number of Internodes")
    ax.set_ylabel("Total Length")
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='TR', y='TL', data=df, ax=ax, estimator=np.mean, ci=None, palette='viridis')
    sns.stripplot(x='TR', y='TL', data=df, ax=ax, color='black', alpha=0.3, jitter=True)
    ax.set_title("Average Total Length by Treatment with Data Points")
    ax.set_xlabel("Treatment")
    ax.set_ylabel("Average Total Length")
    plt.xticks(rotation=45)
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(12, 8))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax, linewidths=0.5, vmin=-1, vmax=1)
    ax.set_title("Enhanced Correlation Heatmap")
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean =""
    stddev =""
    skew =""
    excess_kurtosis =""
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = '<your chosen column for analysis>'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
