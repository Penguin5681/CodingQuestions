*-- Active: 1790236230468@@localhost\@3306\@accenture_sql*


-- Transaction ID, amount and type of all transactions where type is "Debit" and amount is > 10000 but < 50000. Output:
-- TRANSACTION_ID | AMOUNT | TRANSACTION_TYPE

SELECT * FROM transaction;

SELECT transaction.`Transaction_ID`, transaction.`Amount`, transaction.`Transaction_Type` FROM transaction WHERE transaction.`Transaction_Type` = 'Debit' AND transaction.`Amount`> 10000 AND transaction.`Amount` < 50000;