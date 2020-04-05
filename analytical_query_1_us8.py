'''
8
MS
analytical
A budget conscious host of a property
I want to see how much I will earn this month from the current bookings
So I can plan out my finances with my earnings

'''

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

def monthly_earnings(username, month, year):
	tmpl = '''
		SELECT sum(sd.price_per_night)
		  FROM "User" as u
			   JOIN "bookable" as b on b.host_username = u.username
			   JOIN "reservation" as r on b.bookable_id = r.bookable_id
			   JOIN "stay" as s on b.bookable_id = s.stay_bookable_id
			   JOIN "staydateprice" as sd on s.stay_bookable_id = sd.stay_bookable_id
		 WHERE u.username = %s and 
		 	   EXTRACT(MONTH FROM sd.date) = %s and 
		 	   EXTRACT(YEAR FROM sd.date) = %s;
	'''
	
	cmd = cur.mogrify(tmpl, (username, month, year))
	print_cmd(cmd)
	cur.execute(cmd)
	rows = cur.fetchall()
	print_rows(rows)
	
	print("Done.") 
	
		
#------------------------------------------------------------
# Connect to database
#------------------------------------------------------------

userstory_no = 8

userstory_description = '''
I am a budget conscious host of a property
I want to see how much I will earn this month from the current bookings
So I can plan out my finances with my earnings
'''

query_description = '''
This query analyzes all bookings for a host, taking in the username, 
month (number), and year (number) and calculuates the sum of prices 
and addons from each night.
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
monthly_earnings('demohost', '12', '2019')

cur.close()
con.close()