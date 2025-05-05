purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


#1 функция
def total_revenue(purchases):
    return f'Общая выручка: {sum([i["price"] * i["quantity"] for i in purchases])}'


#2 функция
def items_by_category(purchases):
    dic = {}
    for i in purchases:
        if i['category'] in dic:
            dic[i['category']].append(i['item'])
        else:
            dic[i['category']] = [i['item']]
    return f'Товары по категориям: {dic}'


#3 функция
def expensive_purchases(purchases, min_price):
    return f'Покупки дороже {min_price}: {[i for i in purchases if i['price'] > min_price]}'


# 4 функция
def average_price_by_category(purchases):
    dic = {}
    for i in purchases:
        if i['category'] in dic:
            dic[i['category']].append(i['price'])
        else:
            dic[i['category']] = [i['price']]

    for k, v in dic.items():
        dic[k] = sum(v) / len(v)

    return f'Средняя цена по категориям: {dic}'


#5 функция
def most_frequent_category(purchases):
    sorted_desc_purchases = sorted(purchases, key=lambda x: x['quantity'], reverse=True)
    return f'Категория с наибольшим количеством проданных товаров: {sorted_desc_purchases[0]['category']}'


print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1.0))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))



















# import psycopg2
#
# # Подключение к PostgreSQL
# class Psqlcon():
#     def __init__(self):
#         self.conn = None
#
#     def connect_postgres(self):
#         try:
#             self.conn = psycopg2.connect(
#                 host="localhost",
#                 port=5433,
#                 database="postgres",
#                 user="test",
#                 password="1"
#             )
#             print("Connected to PostgreSQL")
#         except Exception as e:
#             print(f"Error connecting to PostgreSQL: {e}")
#
# class Insert_data(Psqlcon):
#     def __init__(self):
#         super().__init__()
#         self.connect_postgres()
#
#     def indatas(self):
#         # Создание курсора
#         cur = self.conn.cursor()
#
#         # Создание таблицы
#         cur.execute('''
#                 CREATE TABLE IF NOT EXISTS employees (
#                     id SERIAL PRIMARY KEY,
#                     name VARCHAR(100),
#                     position VARCHAR(100),
#                     salary NUMERIC
#                 );
#                 ''')
#         print("Table 'employees' created")
#
#         # Вставка данных в таблицу
#         cur.execute('''
#                 INSERT INTO employees (name, position, salary)
#                 VALUES ('Alice', 'Manager', 70000),
#                        ('Bob', 'Developer', 60000),
#                        ('Charlie', 'Designer', 50000);
#                 ''')
#         print("Data inserted into 'employees' table")
#
#         # Сохранение изменений
#         self.conn.commit()
#         cur.close()
#         self.conn.close()
#         return "Operation completed successfully"
#
#
#
#
#     def select_data(self, x, y):
#         cur = self.conn.cursor()
#         cur.execute(f'''
#             SELECT {x} FROM {y};
#         ''')
#         rows = cur.fetchall()
#         for i in rows:
#             print(i)
#
#
# Insert_data().select_data(input('Введите имя поля: ___'), input('Введите имя таблицы: ___'))


# import clickhouse_connect
#
# # Подключение к ClickHouse
# def connect_clickhouse():
#     try:
#         # Установка соединения с ClickHouse
#         client = clickhouse_connect.get_client(host='localhost', port=8123)
#         print("Connected to ClickHouse")
#
#         # Создание таблицы
#         client.command('''
#         CREATE TABLE IF NOT EXISTS employees (
#             id UInt32,
#             name String,
#             position String,
#             salary Float32
#         ) ENGINE = MergeTree()
#         ORDER BY id;
#         ''')
#         print("Table 'employees' created in ClickHouse")
#
#         # Вставка данных в таблицу
#         client.command('''
#         INSERT INTO employees (id, name, position, salary) VALUES
#         (1, 'Alice', 'Manager', 70000),
#         (2, 'Bob', 'Developer', 60000),
#         (3, 'Charlie', 'Designer', 50000);
#         ''')
#         print("Data inserted into 'employees' table in ClickHouse")
#
#         # Выбор данных из таблицы
#         result = client.query('SELECT * FROM employees;')
#         rows = result.result_rows
#
#         # Вывод данных
#         for row in rows:
#             print(row)
#
#         print("ClickHouse connection closed")
#
#     except Exception as e:
#         print(f"Error connecting to ClickHouse: {e}")
#
#
# # Выполнение функции подключения
# connect_clickhouse()
