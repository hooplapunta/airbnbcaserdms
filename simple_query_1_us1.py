#-----------------------------------------------------------------
# Boilerplate stuff
#-----------------------------------------------------------------

import psycopg2
import sys
import datetime

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)

        
#------------------------------------------------------------
# QUERY DEFINITION GOES HERE
#------------------------------------------------------------    

def new_guest(username, first_name, last_name, email, password, date_of_birth, phone_number, address):
    
    dob_obj = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    tmpl = '''
        INSERT INTO "User" (username, first_name, last_name, email, password, date_of_birth, phone_number, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            
        INSERT INTO guest (username, banned)
            VALUES (%s, false);
    '''
    
    cmd = cur.mogrify(tmpl, (username, first_name, last_name, email, password, dob_obj, phone_number, address, username))
    print_cmd(cmd)
    cur.execute(cmd)
    
    tmpl = '''
        SELECT *
          FROM "User" as u;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    
    print("Done.") 
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 1

userstory_description = '''
A user interested in airbnb
I want to be able to sign up for Airbnb
So that I can start to use its services as a guest or host
'''

query_description = '''
This query creates a new guest user by inserting into the user table
and the guest table that inerits it.
You may need to change the username (first param) if the user is taken.
'''

print()
print('USER STORY: ', userstory_no)
print(userstory_description)
print(query_description)

# We are using the 'project' database
con = psycopg2.connect(database='project', user='isdb')  
con.autocommit = True
cur = con.cursor()

# CALL TO QUERY GOES HERE:
new_guest('queryguest', 'Qubert', 'Guest', 'quberty@gmail.com', 'password', '1990-05-05', '4126528011', 'Qwerty Lane Quampo USA')

cur.close()
con.close()
        
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------        








## SAMPLE QUERIES from last exercises below, feel free to reference
### delete after you are done writing!

    
#------------------------------------------------------------
# list_users
#------------------------------------------------------------

def list_users_menu():
    heading('List Users:')
    list_users()

def list_users():
    tmpl = '''
        SELECT *
          FROM Users as u;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        id, first, last, email = row
        print("%s. %s, %s (%s)" % (id, last, first, email))

#-----------------------------------------------------------------
# show_user
#-----------------------------------------------------------------

def show_user_menu():
    heading("Show User(s):")
    name = input('User name: ')
    show_user(name)
    
def show_user(name):
    tmpl = '''
        SELECT *
          FROM Users as u
         -- ILIKE is a case insensitive LIKE
         WHERE (first_name ILIKE %s ) or (last_name ILIKE %s );
    '''
    cmd = cur.mogrify(tmpl, ('%'+name+'%', '%'+name+'%'))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        id, first, last, email = row
        print("%s. %s, %s (%s)" % (id, last, first, email))


def show_user_by_id(id):
    pass

#-----------------------------------------------------------------
# new_user
#-----------------------------------------------------------------

def new_user_menu():
    heading("new_user")
    fname = input('First name: ')
    lname = input('Last name: ')
    email = input('Email: ')
    new_user(first_name=fname, last_name=lname, email=email)

def new_user(first_name, last_name, email):
    tmpl = '''
        INSERT INTO Users (first_name, last_name, email)
            VALUES (%s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (first_name, last_name, email))
    print_cmd(cmd)
    cur.execute(cmd)
    print("Done.")
    
    
#-----------------------------------------------------------------
# show_friends
#-----------------------------------------------------------------

def show_friends_menu():
    heading("Show friends")    
    uid = input("User id: ")
    show_friends(uid)

def show_friends(uid):
    tmpl = '''
        SELECT *
          FROM friends as f
         WHERE f.uid_1 = %s;
    '''
    cmd = cur.mogrify(tmpl, (uid))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        uid1, uid2 = row
        print(uid2)

#-----------------------------------------------------------------
# add_friend
#-----------------------------------------------------------------

def add_friend_menu():
    print("add_friend")
    uid_1 = input("Uid_1: ")
    uid_2 = input("Uid_2: ")
    add_friend(uid_1, uid_2)

def add_friend(uid_1, uid_2):
    tmpl = '''
        INSERT INTO friends
            VALUES (%s, %s);
    '''
    cmd = cur.mogrify(tmpl, (uid_1, uid_2))
    print_cmd(cmd)
    cur.execute(cmd)
    
    tmpl = '''
        INSERT INTO friends
            VALUES (%s, %s);
    '''
    cmd = cur.mogrify(tmpl, (uid_2, uid_1))
    print_cmd(cmd)
    cur.execute(cmd)
    print("Done.")
    
#-----------------------------------------------------------------
# show messages
#-----------------------------------------------------------------

def show_messages_menu():
    heading("show_messages")
    uid = input("User id: ")
    show_messages(uid)

def show_messages(uid):
    tmpl = '''
        SELECT *
          FROM messages as m
         WHERE m.posted_to = %s;
    '''
    cmd = cur.mogrify(tmpl, (uid))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        mid, postedTo, postedFrom, message, timeStamp = row
        print("Message from: " + str(postedTo));
        print("Sent on: " + timeStamp.strftime("%m/%d/%Y, %H:%M:%S"));
        print(message);
        print();

#-----------------------------------------------------------------
# post message
#-----------------------------------------------------------------

def post_message_menu():
    heading("post_message")
    posted_by = input('Posted by: ')
    posted_to = input("Posted to: ")
    message = input('Message: ')
    post_message(posted_by=posted_by, posted_to=posted_to, message=message)

def post_message(posted_by, posted_to, message):
    tmpl = '''
        INSERT INTO messages (posted_to, posted_by, message, time_stamp)
            VALUES (%s, %s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (posted_to, posted_by, message, datetime.datetime.now()))
    print_cmd(cmd)
    cur.execute(cmd)
    print("Done.")