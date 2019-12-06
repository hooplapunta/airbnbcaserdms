'''
5
MS
simple
A guest/host
I want to be able to leave a review about the booking
So that I can warn others if I have a bad experience
'''#-----------------------------------------------------------------
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

def new_review(host_review_id, confirmation_id, checkin_score, location_score, value_score, communication_score, accuracy_score, cleanliness_score, review_text, review_datetime):
    
    dob_obj = datetime.datetime.strptime(review_datetime, '%Y-%m-%d')
    
    tmpl = '''
        INSERT INTO "hostreview" (host_review_id, confirmation_id, checkin_score, location_score, value_score, communication_score, accuracy_score, cleanliness_score, review_text, review_datetime)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    
    cmd = cur.mogrify(tmpl, (host_review_id, confirmation_id, checkin_score, location_score, value_score, communication_score, accuracy_score, cleanliness_score, review_text, review_datetime))
    print_cmd(cmd)
    cur.execute(cmd)
    
    tmpl = '''
        SELECT *
          FROM "hostreview" as h;
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

userstory_no = 5

userstory_description = '''
I am a guest.
I want to be able to leave a review about the booking
so that I can warn others if I have a bad experience
'''

query_description = '''
This query creates a new review by inserting into the guestreview table.
You may need to change the review_id (first param) if the review_id is already
in the database.
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
new_review('6', '1', '1', '1', '1', '1', '1', '1', 'bad!!!', '1990-05-05')

cur.close()
con.close()