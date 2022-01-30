import MySQLdb
import numpy as np


def test_pymysql():
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='xxp'
    )

    cur = conn.cursor()
    cur.execute('''
            SELECT
              BTCUSD
            FROM
              price
            WHERE
              timestamp < now() - interval 60 minute
    ''')

    BTCUSD = np.array(cur.fetchall())
    print(BTCUSD.max(), BTCUSD.min())

    conn.close()


test_pymysql()