import sqlite3


def db_name_to_id(name):
    """
    find stock id from db name-id dict
    """
    with sqlite3.connect('stocks.db') as conn:

        db = conn.execute(
            '''select NUMBER from stocks where NAME = '{0}' '''.format(name))

        res = db.fetchall()

        if len(res) > 0:
            return res[0][0]
        else:
            return None



def db_id_to_industry(id):
    """
    find stock id from db name-id dict
    """
    if isinstance(id, str):
        return id

    with sqlite3.connect('stocks.db') as conn:
        db = conn.execute('''select ind2 from STOCKBASIC where symbol = {0} '''.format(id))
        res = db.fetchall()

        if len(res) > 0:
            return res[0][0]
        else:
            return ''

def db_id_to_name(id):
    """
    find stock id from db name-id dict
    """
    if isinstance(id, str):
        return id

    with sqlite3.connect('stocks.db') as conn:
        db = conn.execute('''select NAME from stocks where NUMBER = {0} '''.format(id))
        res = db.fetchall()

        if len(res) > 0:
            return res[0][0]
        else:
            return str(id)


def db_select_stocks():
    with sqlite3.connect('stocks.db') as conn:
        db = conn.execute('''select name from STOCKBASIC'''.format(id))
        res = db.fetchall()
    return [r[0] for r in res]

def db_select_stockids():
    with sqlite3.connect('stocks.db') as conn:
        db = conn.execute('''select symbol from STOCKBASIC'''.format(id))
        res = db.fetchall()
    return [r[0] for r in res]

def db_select_marketval(s):
    with sqlite3.connect('stocks.db') as conn:
        db = conn.execute('''select marketvalue from STOCKBASIC where symbol = '{}' '''.format(s))
        res = db.fetchall()
    return res[0][0] if len(res) > 0 else 0


def select_industry_stocks(industry):
    conn = sqlite3.connect('stocks.db')

    ret = conn.execute('''select name,symbol from stockbasic where industry = '{0}' '''.format(industry)).fetchall()

    return [r[1] for r in ret]

    pass