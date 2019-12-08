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

SHOW_CMD = False
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)
        
#------------------------------------------------------------
# QUERY DEFINITION GOES HERE
#------------------------------------------------------------    

#Gets the number of reservations made in a specific city
def get_city_reservation_count(city):
    tmpl = '''
        SELECT count(r.confirmation_id)
          FROM Reservation as r
               JOIN Bookable as b on r.bookable_id = b.bookable_id
         WHERE b.city = '%s';
        '''
    cmd = cur.mogrify(tmpl % city)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print("Done.") 
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 13

userstory_description = '''
As a customer service representative
I want to find the number of reservations for stays/experiences
in a specific city
So that I can recommend the top cities to visit
'''

query_description = '''
Joining Reservations and Bookable to get reservations booked
In each city and then finding the count of a given city
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
get_city_reservation_count("Pittsburgh")

cur.close()
con.close()  
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------    