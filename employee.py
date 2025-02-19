import mysql.connector
from mysql.connector import Error

# Establishing connection to the MySQL database
def create_connection():
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="Password123", database="emp"
        )
        if con.is_connected():
            print("Connected to MySQL database")
            return con
    except Error as err:
        print(f"Error: {err}")
        return None

# Check if employee exists
def check_employee(con, employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor = con.cursor(buffered=True)
    data = (employee_id,)
    
    cursor.execute(sql, data)
    employee = cursor.fetchone()
    cursor.close()
    return employee is not None

# Add employee to employee management system
def add_employee(con):
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id already exists
    if check_employee(con, Id):
        print("Employee already exists. Please try again.")
        return
    
    Name = input("Enter Employee Name: ")
    Age = input("Enter Employee Age: ")
    Department = input("Enter Employee Department: ")
    Salary = input("Enter Employee Salary: ")

    sql = 'INSERT INTO employees (name, age,department, salary) VALUES (%s, %s, %s, %s)'
    data = (Name, Age, Department, Salary)
    cursor = con.cursor()

    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
    finally:
        cursor.close()

# Remove employee
def remove_employee(con):
    Id = input("Enter Employee Id: ")

    if not check_employee(con, Id):
        print("Employee does not exist. Please try again.")
        return
    
    sql = 'DELETE FROM employees WHERE id=%s'
    data = (Id,)
    cursor = con.cursor()

    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
    finally:
        cursor.close()

# Promote employee
def promote_employee(con):
    Id = input("Enter Employee's Id: ")

    if not check_employee(con, Id):
        print("Employee does not exist. Please try again.")
        return
    
    try:
        Amount = float(input("Enter increase in Salary: "))
        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()

        cursor.execute(sql_select, data)
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        data_update = (new_salary, Id)
        
        cursor.execute(sql_update, data_update)
        con.commit()
        print("Employee Promoted Successfully")
    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()
    finally:
        cursor.close()

# Display employees
def display_employees(con):
    cursor = con.cursor()
    
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()

        if not employees:
            print("No employees found.")
            return

        for employee in employees:
            print("Employee Id:", employee[0])
            print("Employee Name:", employee[1])
            print("Employee Department:", employee[2])
            print("Employee Salary:", employee[3])
            print("------------------------------------")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Main menu loop
def menu():
    con = create_connection()
    if not con:
        return

    while True:
        print("\nWelcome to Employee Management System")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            add_employee(con)
        elif ch == '2':
            remove_employee(con)
        elif ch == '3':
            promote_employee(con)
        elif ch == '4':
            display_employees(con)
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
    
    # Close the connection when exiting
    con.close()

# Call the menu function to run the program
menu()
