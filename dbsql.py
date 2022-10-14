from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PRASHANTG-LP\SQLEXPRESS;'
                      'Database=Practice;'
                      'Trusted_Connection=yes;')
print("Success")

cursor = conn.cursor()
cursor.execute('''Insert into Persons values ( 3,'Singh','Braga','DOM','POM')''');
cursor.execute('SELECT * FROM Persons')

for i in cursor:
    print(i)
'''conn.commit()'''






