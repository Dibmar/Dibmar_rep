import pandas as pd
import numpy as np


def null_count (df):
    """
                        ---What it does---
    Counts all the NaN values present in a given dataframe, then prints the resutls in a short report.

                        ---What it needs---
        - A dataframe object (df)
    """
    is_null = df.isnull().sum()
    print (f'Number of null in columns:\n{is_null}')
    
def general_info (df):
    """
                        ---What it does--
    This function checks the info, columns and shape of the df, printing them. Also it checks the presence of NaNs values on the df and prints them in case it founds them.

                        ---What it needs---
    A df object
    """

    # df columns info
    print('\t\tGeneral information of the dataframe')
    print(f'{df.info()}\n')

    print("\n\t\tColumn's names:")
    print(f'{df.columns}\n')
    
    print("\n\t\tDataframe's shape:")
    print(f'\t- Rows: {df.shape[0]}')
    print(f'\t- Columns: {df.shape[1]}\n')

    # Presence of NaNs in df
    print("\n\t\tNaN's in dataframe")
    nulls = df.isnull().any()

    if nulls > 0:
        null_count(df)
    
    else:
        print('No NaN values found in df at this time.')


def time_indexer (df):
    """
                        What it does
    Groups your data by the time scale that you want (Year, Month, Day...) creating a new column in the process

                        What it needs
    A dataframe and your input
    """

    t_input = ''
    while t_input <= 3 and type(t_input) == int:
        t_input = int(input("""Select time scale: 
            1) Year
            2) Month
            3)Day>
        
        Please type only the relevant number!!! """))

    if t_input == 1:
        df['year'] = df.index.year

    elif t_input == 2:
        df['month'] = df.index.month

    elif t_input == 3:
        df['day'] = df.index.day


def save_df (df):
    """
                        ---What it does---
    Saves your dataframe of choice to a .csv file in the same directory of the parent file

                        ---What it needs---
        - A dataframe object to be saved (df)
        - A name for the file (name, asked by the function)
    """
    name = input("Type the name of your df> ")
    name = name + ".csv"
    df.to_csv(name, sep = ',')


