# **What is PostgreSQL?**

PostgreSQL (often called Postgres) is a powerful, open-source relational database management system **(RDBMS)**. It is known for its stability, extensibility, and compliance with SQL standards.

### SQL (Structured Query Language) – The Language
- ✅ Data Querying (SELECT)
- ✅ Data Manipulation (INSERT, UPDATE, DELETE)
- ✅ Data Definition (CREATE TABLE, ALTER TABLE)
- ✅ Access Control (GRANT, REVOKE)

### PostgreSQL – A Specific RDBMS That Uses SQL

PostgreSQL (Postgres) is a relational database management system (RDBMS) that uses SQL to store, retrieve, and manipulate data. PostgreSQL extends SQL with extra features like:

- ✅ Support for JSON & NoSQL-style data - instead of databases only storing data in tables, PostgresSQL allows semi-structured data (like txt documents) using JSON
- ✅ Advanced indexing (GIN, BRIN, B-tree, etc.) - makes searching data much faster.
- ✅ Stored procedures with multiple languages (PL/pgSQL, Python, etc.) - lets you write functions(stored procedures) in multiple languages, not just SQL
- ✅ Concurrency control with MVCC (Multi-Version Concurrency Control(If multiple users are accessing the database at the same time))MVCC helps keeping multiple versions of the data. Users can read old data while new data is being updated—so there are no delays or conflicts.
- ✅ Custom data types & extensions - Normal databases have fixed types like INTEGER, TEXT, BOOLEAN. PostgreSQL lets you create your own types!

---

### Useful psql commands (PostgreSQL Command-Line Interface)

| Command                   | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| `\l`                      | List all databases                                        |
| `\i <path_to_sql_script>` | To read a an SQL file                                     |
| `\c database_name`        | Connect to a specific database                            |
| `\dt`                     | List all tables in the current database                   |
| `\d table_name`           | Show table structure (columns, types, constraints)        |
| `\du`                     | List all users and roles                                  |
| `\conninfo`               | Show current connection info (user, database, host, port) |
| `\q`                      | Quit `psql`                                               |



### Table management (DDL - Data Definition Language)(ALTER-CREATE & DROP TABLE, etc)

| Command                                                       | Description                          |
| ------------------------------------------------------------- | ------------------------------------ |
| `CREATE DATABASE db_name;`                                    | Create a new database                |
| `DROP DATABASE db_name;`                                      | Delete a database (**irreversible**) |
| `ALTER DATABASE db_name RENAME TO new_name;`                  | Rename a database                    |
| `CREATE TABLE table_name (id SERIAL PRIMARY KEY, name TEXT);` | Create a new table                   |
| `DROP TABLE table_name;`                                      | Delete a table (**irreversible**)    |
| `ALTER TABLE table_name ADD COLUMN column_name TYPE;`         | Add a new column                     |
| `ALTER TABLE table_name DROP COLUMN column_name;`             | Remove a column                      |
| `ALTER TABLE table_name RENAME TO new_table_name;`            | Rename a table                       |
| `TRUNCATE TABLE table_name;`                                  | Remove all rows from a table         |



### User & role management (DCL - Data Control Language)(GRANT, REVOKE, ALTER, ect)

| Command                                                  | Description                         |
| -------------------------------------------------------- | ----------------------------------- |
| `GRANT ALL PRIVILEGES ON DATABASE db_name TO user;`      | Grant full privileges to a user     |
| `REVOKE ALL PRIVILEGES ON DATABASE db_name FROM user;`   | Revoke privileges                   |
| `CREATE USER user_name WITH PASSWORD 'your_password';`   | Create a new user                   |
| `DROP USER user_name;`                                   | Delete a user                       |
| `ALTER USER user_name WITH SUPERUSER;`                   | Grant superuser privileges          |
| `ALTER USER user_name WITH PASSWORD 'new_password';`     | Change user password                |
| `GRANT CONNECT ON DATABASE db_name TO user_name;`        | Allow user to connect to a database |
| `GRANT USAGE ON SCHEMA public TO user_name;`             | Allow user to use public schema     |
| `GRANT ALL PRIVILEGES ON TABLE table_name TO user_name;` | Grant all privileges on a table     |



### Query data (DQL - Data Query Language)(SELECT, JOIN, ORDER BY)

| Command                                                    | Description                             |
| ---------------------------------------------------------- | --------------------------------------- |
| `SELECT * FROM table_name;`                                | Select all data from a table            |
| `SELECT column1, column2 FROM table_name WHERE condition;` | Select specific columns with conditions |
| `SELECT COUNT(*) FROM table_name;`                         | Count number of rows                    |
| `SELECT DISTINCT column_name FROM table_name;`             | Select distinct values                  |
| `SELECT * FROM table_name ORDER BY column_name ASC/DESC;`  | Sort results                            |



### Updating & deleting data (DML - Data Manipulation Language)(DELETE, INSERT, UPDATE)

| Command                                                              | Description                            |
| -------------------------------------------------------------------- | -------------------------------------- |
| `INSERT INTO table_name (column1, column2) VALUES (value1, value2);` | Insert new data                        |
| `UPDATE table_name SET column1 = value WHERE condition;`             | Update existing data                   |
| `DELETE FROM table_name WHERE condition;`                            | Delete specific rows                   |
| `DELETE FROM table_name;`                                            | Delete all rows (**use with caution**) |

---