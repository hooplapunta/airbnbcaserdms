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
