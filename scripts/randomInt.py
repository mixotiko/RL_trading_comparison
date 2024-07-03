import random
import numpy as np
import pandas as pd


def randomAgent(df, hmax=100, initial_value=100000, start_val="2019-04-01", end_val="2021-09-14", commission=0.0001):
    # TODO
    allow_cash = initial_value
    stocks_num = len(df.tic.unique())
    _stocks = np.zeros(stocks_num)
    dates = df[(df['date'] <= end_val) & (df['date'] >= start_val)].date
    mylist = list(dict.fromkeys(dates))
    #dfObj = pd.DataFrame(columns=['date', 'account_value'])
    hystorical_account_value = []
    lst_to_df = []
    for date in mylist:
        df_day = np.array(data[data['date'] == date].close)
        sumatory = 99999999999999
        comission_operation = 0
        countdown = 0
        while (allow_cash <= sumatory+comission_operation):
            aux_stock = np.zeros(stocks_num)
            for ticker in range(stocks_num):
                aux_stock[ticker] = random.randint(
                    max(-hmax, -_stocks[ticker]), hmax-countdown)
            sumatory = np.sum(df_day*aux_stock)
            comission_operation = np.sum(
                np.absolute(df_day*aux_stock*commission))
            if(countdown < hmax):
                countdown += 5
        _stocks += aux_stock

        allow_cash -= sumatory
        allow_cash -= comission_operation
        account_value = allow_cash+np.sum(df_day*_stocks)
        hystorical_account_value.append(account_value)
        lst_to_df.append([date, account_value])
    dfObj = pd.DataFrame(data=lst_to_df, columns=[
                         'date', 'account_value'])
    print(dfObj.shape)
    return dfObj


result = random.randint(-1, 1)  # decide si se compra, se mantiene o se vende
print(result)
data = pd.read_csv(r'C:\\Users\\tony_\Downloads\\processed_data.csv')
print(data.head())

print(data[(data['date'] <= "2021-09-14") &
           (data['date'] >= "2019-04-01")].date)
summary_random = randomAgent(df=data)
print(summary_random.tail())
summary_random.to_csv(r'C:\\Users\\tony_\Downloads\\random_account_8.csv')
