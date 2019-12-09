#-----------------------------------------------------------------
# Boilerplate stuff
#-----------------------------------------------------------------

import psycopg2
import sys
import datetime
from decimal import Decimal

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

def new_reservation_stay(bookable_id, start_datetime, end_datetime, guest_username, paymentoption, addons):
    
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
    
    addoncost = 0
    for addon in addons:
        tmpl = '''
        SELECT price
          FROM Addon as a
         WHERE bookable_id = %s
               AND addon_id = %s;
        '''
        cmd = cur.mogrify(tmpl, (bookable_id, addon))
        print_cmd(cmd)
        cur.execute(cmd)
        addoncost += Decimal(cur.fetchone()[0][1:])
        
        tmpl = '''
        INSERT INTO Reservation_Addons(confirmation_id, addon_id)
            VALUES (%s, %s);
        '''
        cmd = cur.mogrify(tmpl, (confirmation_id, addon))
        print_cmd(cmd)
        cur.execute(cmd)
        
    print()
    print("Total cost of addons:")
    print(addoncost)
    
    
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
    cost = Decimal(cur.fetchone()[0][1:])
    print()
    print("Total cost for this reservation:")
    print(cost+addoncost)
    
    tmpl = '''
        INSERT INTO Payment (paymentoption_id, confirmation_id, amount, transaction_datetime)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
    '''
    
    cmd = cur.mogrify(tmpl, (paymentoption, confirmation_id, cost+addoncost, now_obj))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    
    print("Done.") 
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 4

userstory_description = '''
A guest
Select add-ons for my stay
So I can have additional amenities like cooked meals during my stay
'''

query_description = '''
This query is similar to US3, but makes additional reads to the AddOns for this bookable,
insertions to associate the reservation with addons, and computes the total price with addons.
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
new_reservation_stay(1, datetime.datetime(2019, 12, 23), datetime.datetime(2019, 12, 26), 'demoguest', 2, [3, 4])

cur.close()
con.close()
        
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------        


