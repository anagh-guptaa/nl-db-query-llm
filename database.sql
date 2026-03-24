CREATE DATABASE nl_database;

USE nl_database;

CREATE TABLE students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
subject VARCHAR(50),
marks INT
);

INSERT INTO students(name,subject,marks) VALUES
('Rahul','Math',85),
('Ananya','Physics',92),
('Riya','Chemistry',76),
('Arjun','Math',88),
('Priya','Physics',95);