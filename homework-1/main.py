"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv
from pathlib import Path

PATH_CUSTOMERS = Path("north_data", "customers_data.csv")
PATH_EMPLOYEES = Path("north_data", "employees_data.csv")
PATH_ORDERS = Path("north_data", "orders_data.csv")

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1234')
try:
    with conn:
        with conn.cursor() as cur:
            with open(PATH_CUSTOMERS, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                # Пропускаем первую строку
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO customers VALUES (%s, %s)', (row[0], row[1]))
                    cur.execute('SELECT * FROM customers')
            
            with open(PATH_EMPLOYEES, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                # Пропускаем первую строку
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s)', (row[0], row[1], row[2]))
                    cur.execute('SELECT * FROM employees')

            with open(PATH_ORDERS, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                # Пропускаем первую строку
                next(reader)
                for row in reader:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s)', (row[0], row[1], row[2]))
                    cur.execute('SELECT * FROM orders')

finally:
    conn.close()