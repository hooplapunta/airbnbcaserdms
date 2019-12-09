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

def send_message(to_user, from_user, message):
    
    timestamp_obj = datetime.datetime.now()
    
    tmpl = '''
        INSERT INTO Message (sent_to, sent_by, message_text, datetime_sent)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
    '''
    
    cmd = cur.mogrify(tmpl, (to_user, from_user, message, timestamp_obj))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    
    print("Done.") 
    
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 9

userstory_description = '''
A potential guest of a property
I want to send a message to the host
So that I can ask questions about the property
'''

query_description = '''
This query simply inserts the meesage into the Message table with the current timestamp.
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
send_message("demohost", "demoguest", "Hi, is your house wheelchair accessible?")

cur.close()
con.close()
        
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------        



