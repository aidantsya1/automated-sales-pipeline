-- Buang table lama
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

-- Buat balik guna SERIAL supaya ID naik sendiri
CREATE TABLE customers (
    id SERIAL PRIMARY KEY, -- SERIAL maksudnya dia auto-tambah 1, 2, 3...
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id), -- Kita tambah link ke table customers
    product VARCHAR(100),
    price DECIMAL(10,2)
);

select*from customers limit 10; --tengok semua data

select sum(price) as total_revenue from orders; -- total revenue

select product, count(*) as jumlah_jualan   -- top 5 produk palinf laku
from orders 
group by product
order by jumlah_jualan desc
limit 5;

select * from orders;

create or replace view v_customer_summary as
select
	c.name, c.city,
	sum(o.price) as total_spent,
	case
		when sum(o.price) > 2000 then 'VIP'
		else 'Normal'
	end as customer_status
from customers c
left join orders o on c.id = o.customer_id
group by c.name, c.city;

select*from v_customer_summary
order by total_spent desc;

select*from v_customer_summary
where customer_status='VIP' ;

SELECT * FROM orders WHERE price <= 0;

DELETE FROM orders WHERE price <= 0;

alter table orders
add constraint check_price_positive check (price > 0);

SELECT * FROM customers;
select*from v_customer_summary;

select * from orders where product ='Laptop';
update orders set price = price * 0.9 where product = 'Laptop';

select product, sum(price) as total_jualan
from orders
group by product
order by total_jualan desc;
