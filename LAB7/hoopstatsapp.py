"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    
    def split_makes_attempts(col):
        makes = []
        attempts = []
        for value in df[col]:
            make, attempt = value.split('-')
            makes.append(int(make))
            attempts.append(int(attempt))
        return makes, attempts

    
    fg_makes, fg_attempts = split_makes_attempts('FG')
    threept_makes, threept_attempts = split_makes_attempts('3PT')
    ft_makes, ft_attempts = split_makes_attempts('FT')

    df.insert(df.columns.get_loc('FG') + 1, 'FGM', fg_makes)
    df.insert(df.columns.get_loc('FGM') + 1, 'FGA', fg_attempts)
    df.insert(df.columns.get_loc('3PT') + 1, '3PTM', threept_makes)
    df.insert(df.columns.get_loc('3PTM') + 1, '3PTA', threept_attempts)
    df.insert(df.columns.get_loc('FT') + 1, 'FTM', ft_makes)
    df.insert(df.columns.get_loc('FTM') + 1, 'FTA', ft_attempts)

    
    df.drop(columns=['FG', '3PT', 'FT'], inplace=True)

    return df

def main():
    """Creates the data frame and view and starts the app."""
    
    print("Loading raw data from rawbrogdonstats.csv")
    raw_frame = pd.read_csv("rawbrogdonstats.csv")
    print("Raw data loaded:")
    print(raw_frame.head())
    
    
    print("Cleaning the data")
    frame = cleanStats(raw_frame)
    print("Cleaned data:")
    print(frame.head())
    
    
    frame.to_csv('cleanbrogdonstats.csv', index=False)
    print("Cleaned data saved to cleanbrogdonstats.csv")
    
    
    print("Passing cleaned data to HoopStatsView")
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
