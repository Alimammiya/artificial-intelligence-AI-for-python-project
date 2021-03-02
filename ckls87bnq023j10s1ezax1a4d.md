## Most Asked SQL Interview Questions and Answers

In this tutorial, We are going to learn 20 Most Asked SQL Interview Questions and Answers.

## 1. What is Database?
A database is an organized collection of data, stored and retrieved digitally from a remote or local computer system. Databases can be vast and complex, and such databases are developed using fixed design and modeling approaches.

## 2. What is DBMS?
DBMS stands for Database Management System. DBMS is a system software responsible for the creation, retrieval, updation, and management of the database. It ensures that our data is consistent, organized, and is easily accessible by serving as an interface between the database and its end-users or application software.

## 3. What is RDBMS? How is it different from DBMS?
RDBMS stands for Relational Database Management System. The key difference here, compared to DBMS, is that RDBMS stores data in the form of a collection of tables, and relations can be defined between the common fields of these tables. Most modern database management systems like MySQL, Microsoft SQL Server, Oracle, IBM DB2, and Amazon Redshift are based on RDBMS.

## 4. What is SQL?
SQL stands for Structured Query Language. It is the standard language for relational database management systems. It is especially useful in handling organized data comprised of entities (variables) and relations between different entities of the data.

## 5. What is the difference between SQL and MySQL?
SQL is a standard language for retrieving and manipulating structured databases. On the contrary, MySQL is a relational database management system, like SQL Server, Oracle or IBM DB2, that is used to manage SQL databases.

## 6. What are Tables and Fields?
A table is an organized collection of data stored in the form of rows and columns. Columns can be categorized as vertical and rows as horizontal. The columns in a table are called fields while the rows can be referred to as records.

## 7. What are Constraints in SQL?
Constraints are used to specify the rules concerning data in the table. It can be applied for single or multiple fields in an SQL table during the creation of the table or after creating using the ALTER TABLE command. The constraints are:
- NOT NULL – Restricts NULL value from being inserted into a column.
- CHECK – Verifies that all values in a field satisfy a condition.
- DEFAULT – Automatically assigns a default value if no value has been specified for the field.
- UNIQUE – Ensures unique values to be inserted into the field.
- INDEX – Indexes a field providing faster retrieval of records.
- PRIMARY KEY – Uniquely identifies each record in a table.
- FOREIGN KEY – Ensures referential integrity for a record in another table.

## 8. What is a Primary Key?
The PRIMARY KEY constraint uniquely identifies each row in a table. It must contain UNIQUE values and has an implicit NOT NULL constraint.

A table in SQL is strictly restricted to have one and only one primary key, which is comprised of single or multiple fields (columns).

```
CREATE TABLE Students ( 	 /* Create table with a single field as primary key */
    ID INT NOT NULL
    Name VARCHAR(255)
    PRIMARY KEY (ID)
);

CREATE TABLE Students ( 	 /* Create table with multiple fields as primary key */
    ID INT NOT NULL
    LastName VARCHAR(255)
    FirstName VARCHAR(255) NOT NULL,
    CONSTRAINT PK_Student
    PRIMARY KEY (ID, FirstName)
);

ALTER TABLE Students 	 /* Set a column as primary key */
ADD PRIMARY KEY (ID);

ALTER TABLE Students 	 /* Set multiple columns as primary key */
ADD CONSTRAINT PK_Student 	 /*Naming a Primary Key*/
PRIMARY KEY (ID, FirstName);
```


## 9. What is a UNIQUE constraint?
A UNIQUE constraint ensures that all values in a column are different. This provides uniqueness for the column(s) and helps identify each row uniquely. Unlike primary key, there can be multiple unique constraints defined per table. The code syntax for UNIQUE is quite similar to that of PRIMARY KEY and can be used interchangeably.
```
CREATE TABLE Students ( 	 /* Create table with a single field as unique */
    ID INT NOT NULL UNIQUE
    Name VARCHAR(255)
);

CREATE TABLE Students ( 	 /* Create table with multiple fields as unique */
    ID INT NOT NULL
    LastName VARCHAR(255)
    FirstName VARCHAR(255) NOT NULL
    CONSTRAINT PK_Student
    UNIQUE (ID, FirstName)
);

ALTER TABLE Students 	 /* Set a column as unique */
ADD UNIQUE (ID);

ALTER TABLE Students 	 /* Set multiple columns as unique */
ADD CONSTRAINT PK_Student 	 /* Naming a unique constraint */
UNIQUE (ID, FirstName);
```

## 10. What is a Foreign Key?
A FOREIGN KEY comprises of single or collection of fields in a table that essentially refers to the PRIMARY KEY in another table. Foreign key constraint ensures referential integrity in the relation between two tables.

The table with the foreign key constraint is labeled as the child table, and the table containing the candidate key is labeled as the referenced or parent table.
```
CREATE TABLE Students ( 	 /* Create table with foreign key - Way 1 */
    ID INT NOT NULL
    Name VARCHAR(255)
    LibraryID INT
    PRIMARY KEY (ID)
    FOREIGN KEY (Library_ID) REFERENCES Library(LibraryID)
);

CREATE TABLE Students ( 	 /* Create table with foreign key - Way 2 */
    ID INT NOT NULL PRIMARY KEY
    Name VARCHAR(255)
    LibraryID INT FOREIGN KEY (Library_ID) REFERENCES Library(LibraryID)
);


ALTER TABLE Students 	 /* Add a new foreign key */
ADD FOREIGN KEY (LibraryID)
REFERENCES Library (LibraryID);
```
## 11. What is a Join? List its different types.
The SQL Join clause is used to combine records (rows) from two or more tables in a SQL database based on a related column between the two.

- (INNER) JOIN: Retrieves records that have matching values in both tables involved in the join. This is the widely used join for queries.
- SELECT * FROM Table_A JOIN Table_B; SELECT * FROM Table_A INNER JOIN Table_B;
- LEFT (OUTER) JOIN: Retrieves all the records/rows from the left and the matched records/rows from the right table.SELECT * FROM Table_A A LEFT JOIN Table_B B ON A.col = B.col;
- RIGHT (OUTER) JOIN: Retrieves all the records/rows from the right and the matched records/rows from the left table.SELECT * FROM Table_A A RIGHT JOIN Table_B B ON A.col = B.col;
- FULL (OUTER) JOIN: Retrieves all the records where there is a match in either the left or right table.SELECT * FROM Table_A A FULL JOIN Table_B B ON A.col = B.col;

## 12. What is a Self-Join?
A self JOIN is a case of regular join where a table is joined to itself based on some relation between its own column(s). Self-join uses the INNER JOIN or LEFT JOIN clause and a table alias is used to assign different names to the table within the query.

```
SELECT A.emp_id AS "Emp_ID",A.emp_name AS "Employee",
B.emp_id AS "Sup_ID",B.emp_name AS "Supervisor"
FROM employee A, employee B
WHERE A.emp_sup = B.emp_id;
```

##13. What is a Cross-Join?
Cross join can be defined as a cartesian product of the two tables included in the join. The table after join contains the same number of rows as in the cross-product of number of rows in the two tables. If a WHERE clause is used in cross join then the query will work like an INNER JOIN.

```
SELECT stu.name, sub.subject 
FROM students AS stu
CROSS JOIN subjects AS sub;
```

## 14. What is an Index? Explain its different types.
A database index is a data structure that provides quick lookup of data in a column or columns of a table. It enhances the speed of operations accessing data from a database table at the cost of additional writes and memory to maintain the index data structure.
```
CREATE INDEX index_name 	 /* Create Index */
ON table_name (column_1, column_2);

DROP INDEX index_name; 	 /* Drop Index */
```
## 15. What is the difference between Clustered and Non-clustered index?
As explained above, the differences can be broken down into three small factors –

- Clustered index modifies the way records are stored in a database based on the indexed column. Non-clustered index creates a separate entity within the table which references the original table.
- Clustered index is used for easy and speedy retrieval of data from the database, whereas, fetching records from the non-clustered index is relatively slower.
- In SQL, a table can have a single clustered index whereas it can have multiple non-clustered indexes.

## 16. What is Data Integrity?
Data Integrity is the assurance of accuracy and consistency of data over its entire life-cycle, and is a critical aspect to the design, implementation and usage of any system which stores, processes, or retrieves data. It also defines integrity constraints to enforce business rules on the data when it is entered into an application or a database.

## 17. What is a Query?
A query is a request for data or information from a database table or combination of tables. A database query can be either a select query or an action query.

```
SELECT fname, lname 		 /* select query */
FROM myDb.students
WHERE student_id = 1;
```
```
UPDATE myDB.students 		 /* action query */
SET fname = 'Captain', lname = 'America'
WHERE student_id = 1;
```
## 18. What is a Subquery? What are its types?
A subquery is a query within another query, also known as nested query or inner query . It is used to restrict or enhance the data to be queried by the main query, thus restricting or enhancing the output of the main query respectively. For example, here we fetch the contact information for students who have enrolled for the maths subject:

```
SELECT name, email, mob, address
FROM myDb.contacts
WHERE roll_no IN (
	 SELECT roll_no
	 FROM myDb.students
	 WHERE subject = 'Maths');
```
There are two types of subquery – Correlated and Non-Correlated.

- A correlated subquery cannot be considered as an independent query, but it can refer the column in a table listed in the FROM of the main query.
- A non-correlated subquery can be considered as an independent query and the output of subquery is substituted in the main query.

## 19. What is the SELECT statement?
SELECT operator in SQL is used to select data from a database. The data returned is stored in a result table, called the result-set.
```
SELECT * FROM myDB.students;
```

## 20. What are some common clauses used with SELECT query in SQL?
Some common SQL clauses used in conjunction with a SELECT query are as follows:

- WHERE clause in SQL is used to filter records that are necessary, based on specific conditions.
- ORDER BY clause in SQL is used to sort the records based on some field(s) in ascending (ASC) or descending order (DESC).SELECT * FROM myDB.students WHERE graduation_year = 2019 ORDER BY studentID DESC;
- GROUP BY clause in SQL is used to group records with identical data and can be used in conjuction with some aggregation functions to produce summarized results from the database.
- HAVING clause in SQL is used to filter records in combination with the GROUP BY clause. It is different from WHERE, since WHERE clause cannot filter aggregated records.SELECT COUNT(studentId), country FROM myDB.students WHERE country != “INDIA” GROUP BY country HAVING COUNT(studentID) > 5;
- Each SELECT statement within the clause must have the same number of columns
- The columns must also have similar data types
- The columns in each SELECT statement should necessarily have the same order
- DECLARE a cursor after any variable declaration. The cursor declaration must always be associated with a SELECT Statement.
- Open cursor to initialize the result set. The OPEN statement must be called before fetching rows from the result set.
- FETCH statement to retrieve and move to the next row in the result set.
- Call the CLOSE statement to deactivate the cursor.
- Finally use the DEALLOCATE statement to delete the cursor definition and release the associated resources.
- One-to-One – This can be defined as the relationship between two tables where each record in one table is associated with the maximum of one record in the other table.
- One-to-Many & Many-to-One – This is the most commonly used relationship where a record in a table is associated with multiple records in the other table.
- Many-to-Many – This is used in cases when multiple instances on both sides are needed for defining a relationship.
Self Referencing Relationships – This is used when a table needs to define a relationship with itself.

---

Originally posted on [techyniel.com](https://www.techyniel.com/30-sql-interview-questions/)

---

## Further Reading
1. [C Programming Course for Free](https://usemynotes.com/c-programming/)
2. [Java programming Course for Free](https://usemynotes.com/java-programming/)
3. [Python for Beginners Course](https://usemynotes.com/python/)
4. [Cryptography & Network Security](https://usemynotes.com/cryptography/)
5. [C Programming Interview Questions](https://usemynotes.com/c-programming-interview-questions/)

---- 
Personally, I love Coffee. 
<a href="https://www.buymeacoffee.com/alimammiya" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
