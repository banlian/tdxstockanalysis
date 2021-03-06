from quant.quant_select_stock_base import *
from stockbase.stock_core import cfg

from calendar import monthrange


def get_month_days(year, month):
    num_days = monthrange(year, month)[1]

    date = datetime.datetime(year, month, 1)

    days = []
    for i in range(num_days):
        day = date + datetime.timedelta(days=i)
        days.append(day)

    return days
    pass


class MaxPctMonth(SelectFuncObj):
    def __init__(self, month=12, threshold=50):
        super(MaxPctMonth, self).__init__()
        self.month = month
        self.threshold = threshold
        self.desc = f'maxpct_{self.month}_by_{self.threshold}'

    def run(self, df, stock, dayoffset):
        self.desc = f'maxpct_{self.month}_by_{self.threshold}'

        # mv = marketvalue(stock)
        # if not 50 < mv < 5000:
        #     return False

        days = get_month_days(2021, self.month)
        days = [d.strftime('%Y-%m-%d') for d in days]

        df = df.loc[df['date'].isin(days)]
        if df.empty:
            return False

        p1 = float(df.iloc[-1, cfg.p_index])
        p0 = float(df.iloc[0, cfg.p_index])

        percent = (p1 - p0) / p0 * 100

        if percent > self.threshold:
            self.ret = 'pct:{:.2f} p0:{:.2f} p1:{:.2f}'.format(percent, p0, p1)
            return True
        return False


import unittest

#
# class Test_MaxPSelect(unittest.TestCase):
#
#     def test_select(self):
#         df = pd.read_pickle(r'..\rawdata\sh.000001.pkl')
#
#         f = MaxPctMonth()
#
#         r = f.run(df, 1, 0)
#         print(r)
#         print(f.ret)
#
#         pass
#
#     def test_enum_months(self):
#         for i in range(6, 12):
#             t = '2011-{:0>2d}'.format(i)
#             algo = MaxPctMonth()
#             algo.month = i
#             algo.threshold = 75
#             results = quant_run_select_stocks([algo], 0, 'month_pct')
#


if __name__ == '__main__':

    for i in range(10, 13):
        t = '2021-{:0>2d}'.format(i)
        print(t)
        algo = MaxPctMonth(i, 50)

        results = quant_run_select_stocks([algo], 0, 'month_pct')

        stocks = [int(r[0]) for r in results]
        print(stocks)
