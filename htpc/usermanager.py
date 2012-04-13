import os
import sqlite3

dbFile= os.path.abspath(os.path.join(os.path.dirname(__file__), "../userdata", 'users.db'))

def createUserDB():
    '''Creates the user database.  If one already exists in the userdata folder, 
    the function returns false, otherwise returns true
    
    The database has the form:
    Table Name: users
    Field 1 (PRIMARY KEY):
        name: username
        type: text
    Field 2:
        name: password
        type: text'''

    # Check if user db already exists.  If so, exit
    if os.path.exists(dbFile):
        return False
    
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    
    # Create the user table
    c.execute('''CREATE TABLE users
    (username text PRIMARY KEY, password text)''')
    
    conn.commit()
    c.close()
    conn.close()
    return True

def addUser(username, password):
    '''Attempts to add the user with the specified username and password to the
    database.  If a user with the username already exists, returns False, but 
    returns True if successful.'''
    
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    
    try:
        c.execute("""INSERT INTO users
        VALUES (?, ?)""", (username, password))
    except:
        return False
    
    conn.commit()
    c.close()
    conn.close()
    return True

def deleteUser(username):
    '''Attempts to delete the user with the specified username from the 
    database.  If the user with the username does not exist, returns False, but 
    returns True if the operation is successful.'''
    
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    
    try:
        c.execute("""DELETE FROM users
        WHERE username=?""",(username,))
    except:
        return False
    
    conn.commit()
    c.close()
    conn.close()
    return True

def getUserData(username):
    '''Returns a tuple containing all data fields (including username) of the 
    user with the specified username.  If no user exists with username, 
    returns None'''
    
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    conn.text_factory = str
    
    c.execute("""select * from users
    where username=?""",(username,))
    data = c.fetchone()
    
    c.close()
    conn.close()
    return data

def getAllUserData():
    '''Returns a list of tuples containing all data fields of all users.  If 
    no users exist, returns an empty list.'''
    
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    conn.text_factory = str
    
    c.execute("""select * from users""")
    data = c.fetchall()
    
    c.close()
    conn.close()
    return data

    
print createUserDB()
#print addUser("bill", "pooeeed")
print getUserData("kill")
print getAllUserData()

