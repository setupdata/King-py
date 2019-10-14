import tushare as ts
import pandas as pd
import pprint

pro = ts.pro_api('your token')


def get_info(ts_code):
    # df = pro.index_monthly(ts_code=ts_code, start_date='20130101', end_date='20171231', fields='ts_code,trade_date,close')
    # df = pro.monthly(ts_code=ts_code, start_date='20070101', end_date='20071231', fields='ts_code,trade_date,close')
    # df = ts.pro_bar(ts_code=ts_code, freq='M', adj='hfq', start_date='20130101', end_date='20171231')
    df = pro.daily(ts_code=ts_code, start_date='20171201',
                   end_date='20180101', fields='ts_code,trade_date,close,vol,amount')
    # df = pro.hk_hold(ts_code=ts_code,trade_date='20151231', exchange='SH')
    return df


def pd2excel(df):
    df.to_excel('output.xlsx', na_rep='', index=False)
    return


if __name__ == '__main__':
    ts_code = "600177.SH"
    df = get_info(ts_code)
    pprint.pprint(df)
    pd2excel(df)
