-- Creates a table called second_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS `second_table`(
    id INTEGER,
    name VARCHAR(256),
    score INTEGER
);
INSERT INTO second_table (id, name, score) 
VALUE 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);