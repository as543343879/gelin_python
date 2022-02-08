import MySQLdb


def test_pymysql():
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='xxp'
    )

    cur = conn.cursor()
    # cur.execute('''
    #         CREATE TABLE price (
    #             timestamp TIMESTAMP NOT NULL,
    #             BTCUSD FLOAT(8,2),
    #             PRIMARY KEY (timestamp)
    #         );
    #     ''')
    cur.execute('''
            INSERT INTO price VALUES(
                "2019-07-14 14:12:18",
                11234.56
            );
        ''')

    cur.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cur.execute(r"insert into user values ('A-001', 'Adam', 95)")

    conn.commit()
    conn.close()


test_pymysql()