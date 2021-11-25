from plot_multi_stocks import plot_stocks
from stock_core import get_days, cfg
from stock_db import db_id_to_name
from stock_reader import get_kdf_from_pkl


def track_to_csv(title, stocks, ndays):
    days = get_days(ndays)
    with open('analysis_stock_track_{}.csv'.format(title), 'w', encoding='utf8') as csv:

        csv.write('stock,name,' + ','.join([d.strftime('%Y-%m-%d') for d in days]) + '\n')
        for s in stocks:
            df = get_kdf_from_pkl(s, False)
            if df is None:
                print('read df error', s)
                continue

            csv.write('{},{}'.format(s,db_id_to_name(s)))
            df = df.tail(len(days) + 1)

            for d in days:
                datestr = d.strftime('%Y-%m-%d')
                print(datestr)

                f = df.loc[df['date'] == datestr]
                if not f.empty:
                    close = f['close'].values[0]
                    pc = f['pctChg'].values[0]
                    print(close, pc)
                    csv.write(',{}'.format(close))
                else:
                    close = 0
                    pc = 0
                    csv.write(',')
            csv.write('\r\n')

            csv.write(',')

            for d in days:
                datestr = d.strftime('%Y-%m-%d')
                print(datestr)

                f = df.loc[df['date'] == datestr]
                if not f.empty:
                    close = f['close'].values[0]
                    pc = f['pctChg'].values[0]
                    print(close, pc)
                    csv.write(',{:.2f}'.format(pc))
                else:
                    close = 0
                    pc = 0
                    csv.write(',')
            csv.write('\r\n')

        csv.flush()



def track_to_plot(title, stocks, ndays):
    cfg.ndays = ndays
    cfg.savepath = '.'
    plot_stocks(stocks, title='analysis_stock_track_{}'.format(title))

