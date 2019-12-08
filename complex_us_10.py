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

# IMPORTANT!! FOR THIS TO WORK THERE HAS TO BE A USERNAME 'SUPPORT'

#Extracts the host usernames associated with trips that received a rating
#of less than two stars using joins and a subquery
def sub_two_reviews_contact():
    tmpl_reviews = '''
    SELECT host_username
        FROM Bookable as b
            JOIN Reservation as r on r.bookable_id = b.bookable_id
            JOIN HostReview as h on h.confirmation_id = r.confirmation_id
                 AND h.confirmation_id in (SELECT confirmation_id
                                             FROM HostReview
                                            WHERE 2 > ((checkin_score +
                                                        location_score +
                                                        value_score + 
                                                        communication_score +
                                                        accuracy_score + 
                                                       cleanliness_score) / 6));
'''
    cmd = cur.mogrify(tmpl_reviews)
    print_cmd(cmd)
    cur.execute(cmd)
    
    #Stores all the sub-two-star hosts in a variable
    hostnames = cur.fetchall()
    
    #Goes through each of the stored problematic hostnames and sends a message
    #To each one. If a host gets bad reviews on more than one property, then
    #They'll get more than one message.
    for hostname in hostnames:
        tmpl = '''
            INSERT INTO Message (sent_to, sent_by, message_text, datetime_sent)
                 VALUES (%s, 'support', 'Please contact us', CURRENT_TIMESTAMP);
        '''
        cmd = cur.mogrify(tmpl, (hostname))
        print_cmd(cmd)
        cur.execute(cmd)
    
    print("Done.") 
    
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 10

userstory_description = '''
As a customer service representative
I want to identify all sub-2-star reviews from guests
So I can identify possible customer issues and address them
'''

query_description = ''' 
Get the username of the problem hosts by joining Bookable, Reservation,
and HostReview, and using a subquery to find reservations that match the
sub-two stars criteria, and then storing those hosts in a variable.
A second query takes that variable and sends a message to each host.
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
sub_two_reviews_contact()

cur.close()
con.close()  
    
#------------------------------------------------------------
# END OF USER STORY QUERY
#------------------------------------------------------------    