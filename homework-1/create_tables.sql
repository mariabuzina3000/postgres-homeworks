-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id)
);

SELECT * FROM employees
SELECT * FROM customers
SELECT * FROM orders