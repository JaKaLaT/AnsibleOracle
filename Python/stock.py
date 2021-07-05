"""
This is a MVP for task 1 of homework for Infrastructure Engineer (automation developer)

"""
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cx_Oracle

# Sets the API key for retrieving stock data
with open('./AlphaV.txt', 'r') as file:
    api_key = file.read()

def get_stock_data(ticker):
    ts = TimeSeries(key=api_key, output_format='pandas', indexing_type='integer')
    data_ts, meta_data_ts = ts.get_daily(symbol=ticker, outputsize='full')
    data_ts = data_ts.sort_index(axis=0, ascending=True)
    data_ts.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    return(data_ts)

def query_db(query):
    cur.execute(query)
    rows = cur.fetchall()
    return rows

# Establish connection to db
dsn = cx_Oracle.makedsn("localhost", 1521,sid = "cdb2")
connection = cx_Oracle.connect(
    user = 'SYSTEM',
    password = '#BadPractice6',
    dsn = dsn,
    encoding = 'UTF-8')
cur = connection.cursor()

# Retrieve historic data about AAPL
stock = get_stock_data('aapl')

# Stores OHLC data in db
sql=""
for i in stock.index:
    sql="INSERT INTO stocks_candle (DAY, P_OPEN, P_HIGH, P_LOW, P_CLOSE, VOLUME) VALUES (DATE \'"+str(stock.loc[i, 'date'])+"\', "+str(stock.loc[i, 'open'])+", "+str(stock.loc[i, 'high'])+", "+str(stock.loc[i, 'low'])+", "+str(stock.loc[i, 'close'])+", "+str(stock.loc[i, 'volume'])+")"
    cur.execute(sql)
    connection.commit()
    print(sql)

# Displays row count in database
report = ("Amount of stored data (rows): " + str(query_db("SELECT COUNT(*) FROM stocks_candle"))+"\n")
# Displays the day price rose the most in %
report += ("Best % gain in a day (best day & percent gain):" + str(query_db("SELECT DAY, round(((P_CLOSE-P_OPEN)/P_OPEN)*100,2) pct_gain FROM stocks_candle ORDER BY pct_gain DESC FETCH FIRST 1 ROWS ONLY"))+"\n")
# Displays the day price fell the most in %
report += ("Worst % loss in a day (worst day & percent loss):" + str(query_db("SELECT DAY, round(((P_CLOSE-P_OPEN)/P_OPEN)*100,2) pct_gain FROM stocks_candle ORDER BY pct_gain ASC FETCH FIRST 1 ROWS ONLY")))
print(report)
with open('stock_report', 'w') as f:
    f.write(report)

if connection:
    connection.close()

# Time constraints, used the initial retrieved dataframe to plot daily close price chart instead of sql query data
stock['close'].plot(label = 'close')

# Tried to use best practice and binding variables when adding data to db, but failed to finalize due to time constraint
# sql="INSERT INTO stocks_candle(DAY, P_OPEN, P_HIGH, P_LOW, P_CLOSE, VOLUME) VALUES(DATE :1, :2, :3, :4, :5, :6)"
# for i in stock.index:
#     list=stock.loc[i, :].tolist()
#     cur.execute(sql, list)
#     connection.commit()
