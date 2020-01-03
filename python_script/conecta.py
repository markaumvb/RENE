import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'username',
  'password': '*******',
  'host': 'server IP (127.0.0.1) to localhost',
  'database': 'databasename',
}

try:
    
  cnx = mysql.connector.connect(**config)
  print('Connected')
  c = cnx.cursor()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


