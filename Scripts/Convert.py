import pandas as pd

def mergecsvs(csv1,csv2,csv3,csv4,csv5,finalcsv,finaljson):
    # Read the files into 5 dataframes.
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)
    df3 = pd.read_csv(csv3)
    df4 = pd.read_csv(csv4)
    df5 = pd.read_csv(csv5)
    # Merge the 5 dataframes, using Ticker column as key
    df6 = pd.merge(df1, df2, on = 'Ticker', how = 'left').fillna(0)
    df7 = pd.merge(df6, df3, on = 'Ticker', how = 'left').fillna(0)
    df8 = pd.merge(df7, df4, on = 'Ticker', how = 'left').fillna(0)
    df9 = pd.merge(df8, df5, on = 'Ticker', how = 'left').fillna(0)
    # Set Ticker as key index
    df9.set_index('Ticker', inplace = True)

    # Convert floats to ints
    df10 = df9['24hour'].astype(int)
    df11 = df9['12hour'].astype(int)
    df12 = df9['8hour'].astype(int)
    df13 = df9['4hour'].astype(int)
    df14 = df9['1hour'].astype(int)

    # Re-Merge int collumns
    df15 = pd.merge(df10, df11, on = 'Ticker', how = 'left').fillna(0)
    df16 = pd.merge(df15, df12, on = 'Ticker', how = 'left').fillna(0)
    df17 = pd.merge(df16, df13, on = 'Ticker', how = 'left').fillna(0)
    df18 = pd.merge(df17, df14, on = 'Ticker', how = 'left').fillna(0)

    # Write it to a new CSV file
    df18.to_csv(finalcsv)
    df18.to_json(finaljson)

#Csv paths
csv5 = '/home/Tickerdigest/Mentions/1hourmentions.csv'
csv4 = '/home/Tickerdigest/Mentions/4hourmentions.csv'
csv3 = '/home/Tickerdigest/Mentions/8hourmentions.csv'
csv2 = '/home/Tickerdigest/Mentions/12hourmentions.csv'
csv1 = '/home/Tickerdigest/Mentions/24hourmentions.csv'

finalcsv = '/home/Tickerdigest/Conversions/finalcsv.csv'
finaljson = '/home/Tickerdigest/Conversions/finaljson.json'

mergecsvs(csv1,csv2,csv3,csv4,csv5,finalcsv,finaljson)
