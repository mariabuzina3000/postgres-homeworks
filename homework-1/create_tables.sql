-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id varchar(100) PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id varchar(100) PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id varchar(100) REFERENCES employees(employee_id)
);

SELECT * FROM employees
SELECT * FROM customers
SELECT * FROM orders