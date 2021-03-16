#Ticker,1hour,4hour,8hour,12hour,24hour
#GME,1123,4534,10342,35042,56432
#AMC,

import pandas as pd

#######Label top of CSVs with Ticker,Xhour
#This program reads two csv files and merges them based on a common key column.

def mergecsvs(csv1,csv2,csv3,csv4,csv5,finalcsv):
    # Read the files into two dataframes.
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)
    df3 = pd.read_csv(csv3)
    df4 = pd.read_csv(csv4)
    df5 = pd.read_csv(csv5)
    # Merge the two dataframes, using _ID column as key
    df6 = pd.merge(df1, df2, on = 'Ticker')
    df7 = pd.merge(df6, df3, on = 'Ticker')
    df8 = pd.merge(df7, df4, on = 'Ticker')
    df9 = pd.merge(df8, df5, on = 'Ticker')
    # Set Ticker as key index
    df9.set_index('Ticker', inplace = True)
    # Write it to a new CSV file
    df9.to_csv(finalcsv)

csv1 = '/home/Tickerdigest/Mentions/1hourmentions.csv'
csv2 = '/home/Tickerdigest/Mentions/4hourmentions.csv'
csv3 = '/home/Tickerdigest/Mentions/8hourmentions.csv'
csv4 = '/home/Tickerdigest/Mentions/12hourmentions.csv'
csv5 = '/home/Tickerdigest/Mentions/24hourmentions.csv'
finalcsv = '/home/Tickerdigest/Conversions/finalcsv.csv'

mergecsvs(csv1,csv2,csv3,csv4,csv5,finalcsv)

###Convert Finalcsv to FinalJSON
