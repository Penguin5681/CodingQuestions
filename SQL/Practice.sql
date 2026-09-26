-- Active: 1790236230468@@localhost\@3306\@accenture_sql*

SELECT * FROM customer;

SELECT * FROM `account`;

SELECT customer.`First_Name`, customer.`Contact` FROM customer JOIN `account` ON customer.`Customer_ID` = `account`.`Customer_ID`;