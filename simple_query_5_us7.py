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

#Base function that does the actual inserting into StayDatePrice
def apd_base(stay_id, date, price):
    tmpl_sdp = '''
        INSERT INTO StayDatePrice(stay_bookable_id, date, price_per_night)
             VALUES (%s, %s, %s)
    '''
    cmd = cur.mogrify(tmpl_sdp, (stay_id, date, price))
    print_cmd(cmd)
    cur.execute(cmd)
    print("Done.") 
    
#Wrapper function that takes a start-date and end-date and finds all of
#the days between them, and then it calls on the base function to actually
#insert the details
def add_property_dates(stay_id, sdate, edate, price):
    days_lst = []
    #Takes the inputted date string parameter and formats it into
    #the datetime.date type
    start = sdate.split("-")
    end = edate.split("-")
    date_start = datetime.date(int(start[0]), int(start[1]), 
                                int(start[2]))
    date_end = datetime.date(int(end[0]), int(end[1]), 
                                int(end[2]))
    
    #Finds the difference between the start and end dates and
    #Uses that as an increment in a loop
    #It also adds the corresponding date to days_lst
    delta = abs(date_start - date_end)
    for i in range(delta.days + 1):
        print(i)
        day = date_start + datetime.timedelta(days=i)
        days_lst.append(day)

    #Goes through all of the days and inserts each into the StayDatePrice
    #table
    for day in days_lst:
        apd_base(stay_id, day, price)
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 7

userstory_description = '''
As an organized host of a property
I want to set specific dates when my property is available
So I can use the property for personal uses on occasion
'''

query_description = ''' 
The wrapper function takes the input from the user and
parses it into something helpful. Then in a loop, it takes
those paramaters and inserts a new entry into StayDatePrice
that corresponds with each selected day
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
add_property_dates(1, "2019-05-23", "2019-05-30", '$80.00')

cur.close()
con.close()  
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------    