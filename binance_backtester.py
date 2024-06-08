#!/usr/bin/env python3

# import your_strategy as strategy
# Set your interval and balance in your trading strategy
import your_strategy as strategy
import pandas as pd

# Read the binance data from the csv file
# open_time, open, high, low, close, volume, close_time, quote_volume, count, taker_buy_volume, taker_buy_quote_volume, ignore
def read_binance_data(file_path):
    df = pd.read_csv(file_path)
    return df

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def days_in_month(month, leap_year):
    if month == 1:  # January
        return 31
    elif month == 2:  # February
        return 29 if leap_year else 28
    elif month == 3:  # March
        return 31
    elif month == 4:  # April
        return 30
    elif month == 5:  # May
        return 31
    elif month == 6:  # June
        return 30
    elif month == 7:  # July
        return 31
    elif month == 8:  # August
        return 31
    elif month == 9:  # September
        return 30
    elif month == 10:  # October
        return 31
    elif month == 11:  # November
        return 30
    elif month == 12:  # December
        return 31

if __name__ == "__main__":
    print('Backtesting from 2022 to 2023')
    # Get your initial balance in your trading strategy on global variable
    start_balance = strategy.balance
    for year in [2022, 2023]:
        leap_year = is_leap_year(year)
        for month in range(1, 13):
            for day in range(1, days_in_month(month, leap_year) + 1):
                file_path = f"./data/BTCUSDT-1m-{year}-{month:02d}-{day:02d}.csv"
                df = read_binance_data(file_path)
                # Batch size means how many candles you want to process at once
                # if batch_size = 20, then you will process 20 minutes at once
                batch_size = 20
                for index in range(len(df) - batch_size + 1):
                    row = df.iloc[index:index + batch_size]
                    # You can call your trading strategy here
                    # You can access the data by row['open_time'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['close_time'],
                    #                            row['quote_volume'], row['count'], row['taker_buy_volume'], row['taker_buy_quote_volume'], row['ignore']
                    # strategy.interval means the time interval to call your trading strategy
                    if index % strategy.interval == 0:
                        try:
                            # Call your trading strategy here
                            strategy.main(row)
                        except:
                            pass
    end_balance = strategy.balance
    profit = (end_balance - start_balance) / start_balance * 100
    print(f"Binance backtesting from 2022 to 2023: {end_balance - start_balance}({profit}%) profit")