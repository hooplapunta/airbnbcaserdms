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

#Creates a new stay by inserting it into both the Bookable and Stay tables
def new_stay_listing(city, hostname, name, stay_category_id, guest_num, 
                     bedrooms_num, beds_num, neighborhood, description):
                         
    #Inserts the details into Bookable first and then gets the bookable_id
    #of the new listing (so that it matches in Stay)
    tmpl_book = '''
        INSERT INTO Bookable(city, host_username, bookable_type)
             VALUES (%s, %s, 'stay');
        SELECT max(bookable_id) FROM Bookable;
    '''
    cmd = cur.mogrify(tmpl_book, (city, hostname))
    print_cmd(cmd)
    cur.execute(cmd)
    #The id of the new listing is stored here and inserted into the new stay
    new_bookable_id = cur.fetchall()[0][0]
    
    #Inserts the details of the listing into Stay next
    tmpl_stay = '''
        INSERT INTO Stay(stay_bookable_id, name, stay_category_id, guest_num, 
                         bedrooms_num, beds_num, neighborhood, 
                         description)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl_stay, (new_bookable_id, name, stay_category_id,
                             guest_num, bedrooms_num, beds_num, neighborhood,
                             description))
    print_cmd(cmd)
    cur.execute(cmd)
    print("Done.") 
    
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 6

userstory_description = '''
As a new potential host
I want to list my property on Airbnb
So that I can host and earn money from it
'''

query_description = '''
Insert the listing into Bookable first and selects the id of the most
recently added item and stores it in a variable.
Then uses that id and other parameters and inserts the listing into Stay.
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
new_stay_listing("New York City", "demohost", "Demo", 2, 6, 3, 4, "Queens",
                 "It's a pretty nice place")

cur.close()
con.close()  
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------    

