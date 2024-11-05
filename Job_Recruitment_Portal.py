import mysql.connector as mycon

# Establish connection
con = mycon.connect(host='localhost', user='root', password="Mouni@123")
cur = con.cursor()

# Create database and tables if they don't exist
cur.execute("CREATE DATABASE IF NOT EXISTS job_recruitment")
cur.execute("USE job_recruitment")

# Creating tables with relationships
cur.execute("""
    CREATE TABLE IF NOT EXISTS job (
        job_id INT PRIMARY KEY,
        title VARCHAR(50),
        description TEXT,
        salary INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS job_seeker (
        seeker_id INT PRIMARY KEY,
        name VARCHAR(50),
        skills TEXT,
        experience INT,
        job_id INT,
        FOREIGN KEY (job_id) REFERENCES job(job_id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        empno INT PRIMARY KEY,
        name VARCHAR(20),
        dept VARCHAR(20),
        salary INT,
        job_id INT,
        FOREIGN KEY (job_id) REFERENCES job(job_id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INT PRIMARY KEY,
        username VARCHAR(20),
        password VARCHAR(20)
    )
""")

con.commit()

def add_record():
    table = input("Enter the table name (job, job_seeker, employee, admin): ")
    if table == "job":
        job_id = int(input("Enter Job ID: "))
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        salary = int(input("Enter Salary: "))
        query = "INSERT INTO job VALUES ({}, '{}', '{}', {})".format(job_id, title, description, salary)
    elif table == "job_seeker":
        seeker_id = int(input("Enter Job Seeker ID: "))
        name = input("Enter Name: ")
        skills = input("Enter Skills: ")
        experience = int(input("Enter Experience: "))
        job_id = int(input("Enter Job ID (or 0 if not applying for any job): "))
        if job_id == 0:
            job_id = 'NULL'
        query = "INSERT INTO job_seeker VALUES ({}, '{}', '{}', {}, {})".format(seeker_id, name, skills, experience, job_id)
    elif table == "employee":
        empno = int(input("Enter Employee Number: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = int(input("Enter Salary: "))
        job_id = int(input("Enter Job ID (or 0 if not assigned any job): "))
        if job_id == 0:
            job_id = 'NULL'
        query = "INSERT INTO employee VALUES ({}, '{}', '{}', {}, {})".format(empno, name, dept, salary, job_id)
    elif table == "admin":
        admin_id = int(input("Enter Admin ID: "))
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        query = "INSERT INTO admin VALUES ({}, '{}', '{}')".format(admin_id, username, password)
    else:
        print("Invalid table name.")
        return
    cur.execute(query)
    con.commit()
    print("## Data Saved ##")

def display_record():
    table = input("Enter the table name (job, job_seeker, employee, admin): ")
    query = "SELECT * FROM {}".format(table)
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(row)

def delete_record():
    table = input("Enter the table name (job, job_seeker, employee, admin): ")
    column = input("Enter the column name of the primary key: ")
    id = input("Enter the ID of the record to delete: ")
    query = "DELETE FROM {} WHERE {} = {}".format(table, column, id)
    cur.execute(query)
    con.commit()
    print("## Record Deleted ##")

def update_record():
    table = input("Enter the table name (job, job_seeker, employee, admin): ")
    column = input("Enter the column name of the primary key: ")
    id = input("Enter the ID of the record to update: ")
    update_col = input("Enter the column name to update: ")
    new_value = input("Enter the new value: ")
    query = "UPDATE {} SET {} = '{}' WHERE {} = {}".format(table, update_col, new_value, column, id)
    cur.execute(query)
    con.commit()
    print("## Record Updated ##")

choice = None
while choice != 0:
    print("1. ADD RECORD")
    print("2. DISPLAY RECORD")
    print("3. DELETE RECORD")
    print("4. UPDATE RECORD")
    print("0. EXIT")
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        display_record()
    elif choice == 3:
        delete_record()
    elif choice == 4:
        update_record()
    elif choice == 0:
        con.close()
        print("## Bye!! ##")
    else:
        print("## INVALID CHOICE ##")
