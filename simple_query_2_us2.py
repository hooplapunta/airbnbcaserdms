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

def get_stay_with_amenities(amenities):
    
    tmpl = '''
        SELECT s.stay_bookable_id, s.name
          FROM Stay as s
         WHERE '''
     
    for a in amenities: 
        tmpl +=''' EXISTS ( SELECT sa.stay_bookable_id 
                       FROM StayHasAmenity as sa
                      WHERE sa.amenity_id = %s AND s.stay_bookable_id = sa.stay_bookable_id ) AND '''
    tmpl = tmpl[:-4]
    tmpl += ';' 
    
    cmd = cur.mogrify(tmpl, amenities)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print_rows(rows)
    
    print("Done.") 
    
        
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 1

userstory_description = '''
A guest who is a parent
I want to find a property with a washer and kitchen
So that I can keep my baby clean and fed during my trip
'''

query_description = '''
This query finds the appropraite property by checking if the Stay
has the required StayHasAmenity rows and filtering them if they have all of it.

I assume the application queries with amenity 1 and 3 for the Kitchen and Dryer,
so there is no need to join the amenity table.
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
get_stay_with_amenities([1,3])

cur.close()
con.close()
        
    
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------        



