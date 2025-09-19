show databases;
create database MoMo_data;
use momo_data;
show tables;
describe system_logs;
select *
from System_Logs;

-- DDL statements to create all tables with proper constraints
CREATE TABLE transactions (
  transaction_id int auto_increment primary key,
  amount DECIMAL(15,2),
  fee  INT,
  new_balance DECIMAL(15,2),
  transaction_date DATETIME,
  category VARCHAR(50),
  category_id int,
  user_id int,
  FOREIGN KEY (category_id) REFERENCES categories(category_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  KEY(transaction_id, transaction_date),
  KEY(category_id, transaction_date),
  KEY(user_id, transaction_date)
);

CREATE TABLE categories (
  category_id INT auto_increment PRIMARY KEY,
  category_name VARCHAR(50),
  KEY (category_name, category_id)
);

CREATE TABLE users (
  user_id INT auto_increment PRIMARY KEY,
  name varchar(255),
  KEY (name, user_id)
);

CREATE TABLE System_Logs (
  log_id INT auto_increment primary key,
  log_timestamp DATETIME,
  transaction_id INT,
  foreign key(transaction_id) references transactions(transaction_id),
  KEY (log_id, transaction_id)
);

-- End of DDL statements (all tables created with proper constraints)

-- Sample DML statements to insert test data (at least 5 records per main table)
-- USERS
INSERT INTO users (name) VALUES
('Ayomide'),
('Neza'),
('Rowan'),
('Duke'),
('Habeeb');

-- CATEGORIES
INSERT INTO categories (category_name) VALUES
('Debit'),
('Credit'),
('Electricity'),
('Airtime'),
('Food');

-- TRANSACTIONS
INSERT INTO transactions (amount, fee, new_balance, transaction_date, category, category_id, user_id) VALUES
(1000.00, 100, 5000.00, '2025-09-18 09:00:00', 'Debit', 1, 1),
(2000.00, 100, 2950.00, '2025-09-18 10:00:00', 'Credit', 2, 2),
(500.00, 50, 1500.00, '2025-09-18 11:00:00', 'Electricity', 3, 3),
(1200.00, 100, 3800.00, '2025-09-18 12:00:00', 'Airtime', 4, 4),
(750.00, 50, 4250.00, '2025-09-18 13:00:00', 'Food', 5, 5);

-- This is just for the mock table data insertion. For large scale purposes, the category name and id would be mapped using a dictionary or a more efficient method would be used.

-- SYSTEM_LOGS
INSERT INTO System_Logs (log_timestamp, transaction_id) VALUES
('2025-09-18 09:01:00', 1),
('2025-09-18 10:01:00', 2),
('2025-09-18 11:01:00', 3),
('2025-09-18 12:01:00', 4),
('2025-09-18 13:01:00', 5);

-- End of Sample DML statements to insert test data


SELECT t.transaction_id, u.name AS user_name, c.category_name, 
       t.amount, t.fee, t.new_balance, t.transaction_date
FROM transactions t
JOIN users u ON t.user_id = u.user_id
JOIN categories c ON t.category_id = c.category_id;

SELECT c.category_name, COUNT(t.transaction_id) AS total_transactions
FROM categories c
JOIN transactions t ON c.category_id = t.category_id
GROUP BY c.category_name;

ALTER TABLE transactions
ADD CONSTRAINT chk_amount_positive CHECK (amount > 0);

ALTER TABLE transactions
ADD CONSTRAINT chk_balance_nonnegative CHECK (new_balance >= 0);

ALTER TABLE categories
ADD CONSTRAINT uq_category_name UNIQUE (category_name);

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'transactions';

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'categories';
