import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="coc"
)

def connexion(username, password):
    mycursor = mydb.cursor()
    sql = "SELECT count(*) FROM Users where username = %s and password = %s"
    argument=(username, password, )
    mycursor.execute(sql, argument)
    
    myresult = mycursor.fetchall()
    if myresult[0][0]==1:
        return True
    return False

def user_already_existe(username):
    mycursor = mydb.cursor()
    sql = "SELECT count(*) FROM Users where username = %s"
    argument=(username, )
    mycursor.execute(sql, argument)
    
    myresult = mycursor.fetchall()
    if myresult[0][0]==1:
        return True
    return False

def inscription(username, password):
      if user_already_existe(username):
          return "error01"
      else:
          mycursor = mydb.cursor()

          sql = "INSERT INTO Users (username, password) VALUES (%s, %s)"
          val = (username, password, )
          mycursor.execute(sql, val)

          mydb.commit()
          if mycursor.rowcount != 1:
                return "error02"
          else:
                return "sucess"
                
            
      

class Users:
    def __init__(self, username):
        self.username = username
