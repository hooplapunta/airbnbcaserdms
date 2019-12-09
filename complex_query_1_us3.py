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

def new_reservation_stay(bookable_id, start_datetime, end_datetime, guest_username, paymentoption):
    
    now_obj = datetime.datetime.now()
    
    tmpl = '''
        INSERT INTO Reservation (confirmation_datetime, start_datetime, end_datetime, bookable_id, guest_username)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING confirmation_id;
    '''
    
    cmd = cur.mogrify(tmpl, (now_obj, start_datetime, end_datetime, bookable_id, guest_username))
    print_cmd(cmd)
    cur.execute(cmd)
    confirmation_id = cur.fetchone()
    
    start_obj = start_datetime.strftime('%Y-%m-%d')
    end_obj = end_datetime.strftime('%Y-%m-%d')
    
    tmpl = '''
        SELECT sum(price_per_night)
          FROM StayDatePrice as sdp
         WHERE stay_bookable_id = %s
               AND date >= %s
               AND date <= %s;
    '''
    cmd = cur.mogrify(tmpl, (bookable_id, start_obj, end_obj))
    print_cmd(cmd)
    cur.execute(cmd)
    cost = cur.fetchone()
    print()
    print("Total cost for this reservation:")
    print(cost)
    
    tmpl = '''
        INSERT INTO Payment (paymentoption_id, confirmation_id, amount, transaction_datetime)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
    '''
    
    cmd = cur.mogrify(tmpl, (paymentoption, confirmation_id, cost, now_obj))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    
    print("Done.") 
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 3

userstory_description = '''
A guest
I want to make a booking and pay for my stay (not experience)
So that I can finally go for that dream trip!
'''

query_description = '''
This query makes insertions into the Reservation and Payment table,
using information from the Bookable and Stay (and related) tables,
using the provided place to reserve, dates to reserve, guest who is staying, and the payment method.

In this case, the application knows that it is booking a stay, so it only looks up the Stay table.
Otherwise, bookable.bookable_type would inform what kind of thing is being booked
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
new_reservation_stay(1, datetime.datetime(2019, 12, 23), datetime.datetime(2019, 12, 26), 'demoguest', 2)

cur.close()
con.close()
        
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------        


