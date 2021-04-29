import sqlite3


def connect():
    return sqlite3.connect('money-manager.db')


def delete(connection):
    connection.execute("DROP TABLE user4")
    connection.commit()
    connection.execute("DELETE FROM users where id=4")
    connection.commit()


def create_create_main_table(connection):
    connection.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT(50) UNIQUE NOT NULL, password TEXT NOT NULL)")


def username_exists(connection, username):
    data = connection.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if not data:
        return False
    else:
        return True


def check_username(connection, username):
    data = connection.execute("SELECT id, password FROM users WHERE username = ?", (username,)).fetchone()
    if data is None:
        return False
    else:
        return True


def check_password(connection, username, password):
    data = connection.execute("SELECT id, password FROM users WHERE username = ?", (username,)).fetchone()
    if password != data[1]:
        return "False"
    else:
        return f"user{data[0]}"


def add_user(connection, username, password):
    with connection:
        data = connection.execute('SELECT * FROM users').fetchall()
        if not data:
            id = 1
        else:
            id = data[-1][0] + 1
        connection.execute("INSERT INTO users(id, username, password) VALUES(?, ?, ?)", (id, username, password))
        connection.commit()
        connection.execute(f"CREATE TABLE user{id}(id INTEGER UNIQUE, priority INTEGER, date INTEGER, category VARCHAR(20), amount INTEGER, balance INTEGER, income INTEGER)")


def get_data(connection, table, month, year):
    data = connection.execute(f"SELECT balance, income FROM {table} WHERE date LIKE '{year}_{month}%'").fetchall()
    return data


def add_income(connection, table, date, amount):
    month = date.split("-")[1]
    year = date.split("-")[0]
    data = connection.execute(f"SELECT id, date, balance, income from {table}").fetchall()
    month_rows_0 = connection.execute(f"SELECT id, date, balance, income from {table} WHERE date LIKE '{year}_{month}%' AND priority=0").fetchall()
    month_rows_all = connection.execute(f"SELECT id, date, balance, income from {table} WHERE date LIKE '{year}_{month}%'").fetchall()
    if not data:
        connection.execute(f"INSERT INTO {table}(id, priority, date, balance, income) VALUES(?, ?, ?, ?, ?)", (1, 0, date, amount, amount))
        connection.commit()
    elif not month_rows_0:
        connection.execute(f"INSERT INTO {table}(id, priority, date, balance, income) VALUES(?, ?, ?, ?, ?)", (data[-1][0]+1, 0, date, amount, amount))
        connection.commit()
    else:
        last_row_amount = month_rows_all[-1][3]
        total_amount = int(amount)+last_row_amount
        connection.execute(f"INSERT INTO {table}(id, priority, date, balance, income) VALUES(?, ?, ?, ?, ?)", (data[-1][0]+1, 0, date, month_rows_all[-1][2]+int(amount), total_amount))
        connection.commit()


def add_expense(connection, table, date, amount, category):
    month = date.split("-")[1]
    year = date.split("-")[0]
    data = connection.execute(f"SELECT id, date, balance, income from {table}").fetchall()
    month_rows = connection.execute(f"SELECT id, date, balance, income from {table} WHERE date LIKE '{year}-{month}%'").fetchall()
    if not data or not month_rows:
        return False
    else:
        connection.execute(f"INSERT INTO {table} VALUES(?, ?, ?, ?, ?, ?, ?)", (data[-1][0]+1, 1, date, category, amount, month_rows[-1][2]-int(amount), month_rows[-1][3]))
        connection.commit()
        return True


def delete_transaction(connection, table, id):
    data = connection.execute(f"SELECT * FROM {table} WHERE id={id}").fetchone()
    if not data:
        return False
    else:
        connection.execute(f"DELETE FROM {table} WHERE id={id}")
        connection.commit()
        connection.execute(f"UPDATE {table} SET id=id-1 WHERE id>{id}")
        connection.commit()
        return True


def get_bar(connection, month, year, table):
    with connection:
        data = connection.execute(f"SELECT category, SUM(amount) FROM {table} WHERE priority=1 AND date LIKE '{year}_{month}%' GROUP BY category;").fetchall()
        return data


def get_pie(connection, month, year, table):
    with connection:
        data = connection.execute(f"SELECT category,SUM(amount) FROM {table} WHERE priority=1 AND date LIKE '{year}_{month}%' GROUP BY category;").fetchall()
        return data


def get_transaction_table(connection, table):
    with connection:
        return connection.execute(f"SELECT id,date,category,amount,balance,income FROM {table} ORDER BY id desc;").fetchall()


def get_delete_table(connection, table):
    with connection:
        return connection.execute(f"SELECT id,date,category,amount,balance,income FROM {table} ORDER BY id DESC;").fetchall()
