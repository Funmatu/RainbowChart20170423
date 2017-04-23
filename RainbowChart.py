# coding: utf-8
#------RainbowChart2.py------
#RainbowChart(DATA, String='DATA')
#入力データはPandas.DataFrame型で時系列データの必要性
#代表的な周期性を仮定してトレンドをグラフ化
#DATA：時系列データ（DataFrame）
#String：系列名，グラフの保存ファイル名，デフォルトは「DATA」
#返り値としてデータを返す
#RainbowChart2(DATA, String='DATA')
#上記関数のサブプロットバージョン
#全データと直近1年のグラフを描画
#RainbowChart_shift(DATA, String='DATA')
#代表的な周期性を仮定してデータ末尾を揃えてトレンドをグラフ化
#DATA：時系列データ（DataFrame）
#String：系列名，グラフの保存ファイル名，デフォルトは「DATA」
#返り値としてデータを返す
#RainbowChart2_shift(DATA, String='DATA')
#上記関数のサブプロットバージョン
#全データと直近1年のグラフを描画
##########################################
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns


def sdecomp(DATA, String):
    DATA_007 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=7)
    DATA_011 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=11)
    DATA_021 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=21)
    DATA_025 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=25)
    DATA_051 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=51)
    DATA_075 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=75)
    DATA_120 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=120)
    DATA_200 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=200)
    DATA_365 = seasonal_decompose(DATA.interpolate(method='time').fillna(DATA.median()).values, freq=365)

    DATARainbow = pd.DataFrame({String: DATA.interpolate(method='time').fillna(DATA.median()),
                                                    String+'_007': DATA_007.trend,
                                                    String+'_011': DATA_011.trend,
                                                    String+'_021': DATA_021.trend,
                                                    String+'_025': DATA_025.trend,
                                                    String+'_051': DATA_051.trend,
                                                    String+'_075': DATA_075.trend,
                                                    String+'_120': DATA_120.trend,
                                                    String+'_200': DATA_200.trend,
                                                    String+'_365': DATA_365.trend}, index=DATA.index)

    return DATARainbow


def sdecomp_shift(DATA, String):
    DATARainbow = sdecomp(DATA, String)
    DATA_007_tail_nan = len(DATARainbow[String+'_007'][DATARainbow[String+'_007'].isnull()])//2
    DATA_011_tail_nan = len(DATARainbow[String+'_011'][DATARainbow[String+'_011'].isnull()])//2
    DATA_021_tail_nan = len(DATARainbow[String+'_021'][DATARainbow[String+'_021'].isnull()])//2
    DATA_025_tail_nan = len(DATARainbow[String+'_025'][DATARainbow[String+'_025'].isnull()])//2
    DATA_051_tail_nan = len(DATARainbow[String+'_051'][DATARainbow[String+'_051'].isnull()])//2
    DATA_075_tail_nan = len(DATARainbow[String+'_075'][DATARainbow[String+'_075'].isnull()])//2
    DATA_120_tail_nan = len(DATARainbow[String+'_120'][DATARainbow[String+'_120'].isnull()])//2
    DATA_200_tail_nan = len(DATARainbow[String+'_200'][DATARainbow[String+'_200'].isnull()])//2
    DATA_365_tail_nan = len(DATARainbow[String+'_365'][DATARainbow[String+'_365'].isnull()])//2

    DATA_007_shift = DATARainbow[String+'_007'].shift(DATA_007_tail_nan)
    DATA_011_shift = DATARainbow[String+'_011'].shift(DATA_011_tail_nan)
    DATA_021_shift = DATARainbow[String+'_021'].shift(DATA_021_tail_nan)
    DATA_025_shift = DATARainbow[String+'_025'].shift(DATA_025_tail_nan)
    DATA_051_shift = DATARainbow[String+'_051'].shift(DATA_051_tail_nan)
    DATA_075_shift = DATARainbow[String+'_075'].shift(DATA_075_tail_nan)
    DATA_120_shift = DATARainbow[String+'_120'].shift(DATA_120_tail_nan)
    DATA_200_shift = DATARainbow[String+'_200'].shift(DATA_200_tail_nan)
    DATA_365_shift = DATARainbow[String+'_365'].shift(DATA_365_tail_nan)

    DATA_shift = pd.DataFrame({String: DATARainbow[String],
                                               String+'_007': DATA_007_shift,
                                               String+'_011': DATA_011_shift,
                                               String+'_021': DATA_021_shift,
                                               String+'_025': DATA_025_shift,
                                               String+'_051': DATA_051_shift,
                                               String+'_075': DATA_075_shift,
                                               String+'_120': DATA_120_shift,
                                               String+'_200': DATA_200_shift,
                                               String+'_365': DATA_365_shift}, index=DATARainbow.index)
    
    return DATA_shift


def RainbowChart(DATA, String='DATA'):
    DATARainbow = sdecomp(DATA, String)

    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル
    DATARainbow.plot()
    plt.savefig(String+'_Rainbow.png', dpi=350)
    plt.show()
    
    return DATARainbow

def RainbowChart2(DATA, String='DATA'):
    DATARainbow = sdecomp(DATA, String)
    
    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル
    _, axarr = plt.subplots(2, figsize=(8, 6))
    DATARainbow.plot(ax = axarr[0])
    DATARainbow.tail(365).plot(ax = axarr[1])
    plt.savefig(String+'_Rainbow.png', dpi=350)
    plt.show()
    
    return DATARainbow


def RainbowChart_shift(DATA, String='DATA'):
    DATARainbow_shift = sdecomp_shift(DATA, String)
    
    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル
    DATARainbow_shift.plot()
    plt.savefig(String+'_Rainbow_shift.png', dpi=350)
    plt.show()
    
    return DATARainbow_shift


def RainbowChart2_shift(DATA, String='DATA'):
    DATARainbow_shift = sdecomp_shift(DATA, String)
    
    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル
    _, axarr = plt.subplots(2, figsize=(8, 6))
    DATARainbow_shift.plot(ax = axarr[0])
    DATARainbow_shift.tail(365).plot(ax = axarr[1])
    plt.savefig(String+'_Rainbow_shift.png', dpi=350)
    plt.show()
    
    return DATARainbow_shift


def RainbowChart_Ani(DATA, String='DATA'):
    DATARainbow = sdecomp(DATA, String)

    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル    
    def update(i):
        plt.cla()
        plt.plot(DATARainbow[i*30:(i+1)*30])

    fig = plt.figure(figsize=(8, 6))
    ani = animation.FuncAnimation(fig, update, frames = len(DATARainbow)//30,interval = 500)
    ani.save(String+'_Rainbow.gif', writer='imagemagick', fps=5)
    plt.show()
    
    return DATARainbow


def RainbowChart_shift_Ani(DATA, String='DATA'):
    DATARainbow_shift = sdecomp_shift(DATA, String)
    
    sns.set_style("whitegrid")#データ数が多い時にお薦めのスタイル
    def update(i):
        plt.cla()
        plt.plot(DATARainbow_shift[i*30:(i+1)*30])

    fig = plt.figure(figsize=(8, 6))
    ani = animation.FuncAnimation(fig, update, frames = len(DATARainbow_shift)//30,interval = 500)
    ani.save(String+'_Rainbow_shift.gif', writer='imagemagick', fps=5)
    plt.show()
    
    return DATARainbow_shift



if __name__ == '__main__':
    import pandas_datareader.data as web
    import datetime as dt
    #from mymodules import GglSprdSheet2 as GSS

    start = dt.datetime(1973, 1, 1)
    end  = dt.datetime(2017, 3, 17)

    F_USD = lambda x: 1/x

    #Get the Series into DataFrame
    #jpy = web.DataReader('JPY=X', 'yahoo', start, end)['Adj Close']
    #DATA = RainbowChart_shift_Ani(jpy, 'JPY')
    #DATA = RainbowChart2_shift(jpy, 'JPY')
    #DATA.to_csv('JPY_Rainbow.csv')
    #GSS.write(DATA, 'JPY_Rainbow') #Too Late!!!
    
    #eur = web.DataReader('EUR=X','yahoo', start, end)['Adj Close']
    #eur = F_USD(eur)
    #RainbowChart2_shift(eur, 'EURUSD')
    
    #aud = web.DataReader('AUD=X','yahoo', start, end)['Adj Close']
    #aud = F_USD(aud)
    #RainbowChart2_shift(aud, 'AUDUSD')
    
    #tnx  = web.DataReader('^TNX', 'yahoo', start, end)['Adj Close']
    #RainbowChart2_shift(tnx, 'CBOE Interest Rate 10 Year')
    
    #vix  = web.DataReader('^VIX', 'yahoo', start, end)['Adj Close']
    #RainbowChart2_shift(vix, 'VIX')
    
    #USDIX=web.DataReader('DX-Y.NYB', 'yahoo', start, end)['Adj Close']
    #RainbowChart2_shift(USDIX, 'US Dollar Index')
    
    #NIKKEI225 = web.DataReader('^N225', 'yahoo', start, end)['Adj Close']
    #RainbowChart2_shift(NIKKEI225, 'NIKKEI225')
    
    #DOW = web.DataReader('^DJI', 'yahoo', start, end)['Adj Close']
    #RainbowChart2_shift(DOW, 'Dow Jones')
    #Latest data from Yahoo, but no exist, by FRED
    GOLD = web.DataReader('GOLDAMGBD228NLBM', 'fred', start, end)['GOLDAMGBD228NLBM']
    RainbowChart2_shift(GOLD, 'GOLD')
    
    #WTI = web.DataReader('DCOILWTICO', 'fred', start, end)['DCOILWTICO']
    #RainbowChart2_shift(WTI, 'WTI')