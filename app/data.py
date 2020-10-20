import sqlite3

con = sqlite3.connect("students.db")

cur = con.cursor()
con.execute('''Create table student_data(id_number text primary key, first_name text, last_name text, course text)''')

