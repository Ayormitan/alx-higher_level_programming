# SQL - Introduction

## Resources
- What is Database & SQL?
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- What makes the big difference between a backtick and an apostrophe?
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax
- Installing MySQL in Ubuntu 20.04

## Author
- Omotayo Ayomitan

## Tasks
1. A script that lists all databases of your MySQL server.
2. A script that creates the database hbtn_0c_0 in your MySQL server.
   - If the database hbtn_0c_0 already exists, your script should not fail.
   - You are not allowed to use the SELECT or SHOW statements.
3. A script that deletes the database hbtn_0c_0 in your MySQL server.
   - If the database hbtn_0c_0 doesn’t exist, your script should not fail.
   - You are not allowed to use the SELECT or SHOW statements.
4. A script that lists all the tables of a database in your MySQL server.
   - The database name will be passed as an argument of mysql command (in the following example: mysql is the name of the database).
5. A script that creates a table called first_table in the current database in your MySQL server.
   - first_table description:
     - id INT
     - name VARCHAR(256)
   - The database name will be passed as an argument of the mysql command.
   - If the table first_table already exists, your script should not fail.
   - You are not allowed to use the SELECT or SHOW statements.
6. A script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
   - The database name will be passed as an argument of the mysql command.
   - You are not allowed to use the DESCRIBE or EXPLAIN statements.
7. A script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
   - All fields should be printed.
   - The database name will be passed as an argument of the mysql command.
8. A script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
   - New row:
     - id = 89
     - name = Best School
   - The database name will be passed as an argument of the mysql command.
9. A script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
   - The database name will be passed as an argument of the mysql command.

