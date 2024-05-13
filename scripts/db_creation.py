import pandas as pd
import mysql.connector as mysql

DB = mysql.connect(
  host="localhost",
  port=3306,
  user="user",
  password="password"
)
DB.close
