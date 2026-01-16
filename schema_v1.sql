-- Buang table lama kalau dah wujud supaya tak error

-- 1. Buat Table Customers
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

-- 2. Buat Table Orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    price DECIMAL(10,2)
);

-- 3. Masukkan Data
INSERT INTO customers VALUES (1, 'Ali', 'KL'), (2, 'Abu', 'JB'), (3, 'Siti', 'Ipoh');
INSERT INTO orders VALUES (101, 1, 'Laptop', 3500.00), (102, 1, 'Mouse', 50.00), (103, 2, 'Keyboard', 150.00);

-- 4. Test tengok data ada tak
SELECT * FROM orders;

SELECT c.name, SUM(o.price) AS total_belanja
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE c.name = 'Ali'
GROUP BY c.name;

update orders
set product = 'Gaming Mouse', price = 150.00
where order_id= 102;

select*from orders where order_id = 102;

select c.name, o.product
from customers c
left join orders o on c.id = o.customer_id;

select count(*) from orders;

select product, price
from orders
where price > 100;

INSERT INTO orders VALUES (104, 99, 'Monitor', 500.00);