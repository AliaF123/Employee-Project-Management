-- Create Database
CREATE DATABASE IF NOT EXISTS emp;
USE emp;

-- Create Employee Table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(255),
    salary FLOAT NOT NULL
);

-- Insert Sample Data (Optional)
INSERT INTO employees (name, age, department, salary) VALUES 
('Alice Johnson', 30, 'HR', 50000),
('Bob Smith', 28, 'IT', 60000),
('Charlie Brown', 35, 'Finance', 70000);
