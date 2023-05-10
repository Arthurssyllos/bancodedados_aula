import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="dbaula.c7yoa1780lci.us-east-1.rds.amazonaws.com",
    user="admin",
    password="aulanoiteFaculdad3",
    database="aula"
  )
  return mydb
