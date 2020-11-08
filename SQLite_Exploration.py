"""This document is for my exploration with using SQLite in Python, with Pandas"""
""" All commands are confirmed working on 11/8/20"""
                        # Imports, including class from secondary file
import sqlite3
from employee import Employee

                                    #SQLite Setup Statments
                        # Statement to create a DB file in repository
#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')     #Creates a new DB every time program is ran in the memory - for testing purposes

                        # Creates object to run SQL commands on
c = conn.cursor()
                        # SQLite3 "Refresh DB" command -- usually unnessary, sometimes used after exec statments
#conn.commit()

                        # Example of creating a table, in the DB file specified above
c.execute("""CREATE TABLE employees (
            first TEXT,
            last TEXT,
            pay INTEGER
            )""")
                        # Example of SQLite3 syntax of inserting raw values
#c.execute("INSERT INTO employees VALUES ('Greg', 'Gompers', 85000)")

                        # Example of Inserting objects created in Python, into SQLite3 DB
# emp_1 = Employee ('John', 'Doe', 80000)
# emp_2 = Employee ('Jane', 'Doe', 90000)
#
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})


                        # Example of using queries in SQLite3
#c.execute("SELECT * FROM employees")
#print(c.fetchall())
# print(c.fetchone())     -- This acts like LIMIT 1 in SQL
# print(c.fetchmany(#))   -- This acts like LIMIT # in SQL


                        # Example of using Python functions to wrap these SQLite3 commands
def insert_emp(emp):
    with conn:
        c.execute("""INSERT INTO employees VALUES
                    (:first, :last, :pay)""",
                    {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})


def get_emps_by_name(lastname):
    c.execute("""SELECT * FROM employees
                   WHERE last=:last""", {'last': lastname})
    return c.fetchall()


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

print("employees with last name Doe")
print(get_emps_by_name('Doe'))

update_pay(emp_2, 95000)
remove_emp(emp_1)
print("employees with last name Doe (second time)")
print(get_emps_by_name('Doe'))

                        # SQLite3 teardown command
conn.close()

