'''
12
MS
Analytical 2
Customer service representative
I want to find the percentage of times a host cancels the booked place / experience within 24 hours
So that I can identify fraudulent or untrustworthy owners
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

def average_price():
	tmpl = '''
		SELECT s.neighborhood, SUM(sd.price_per_night)/COUNT(sd.price_per_night)
		  FROM "stay" as s
		  	   JOIN "staydateprice" as sd on s.stay_bookable_id = sd.stay_bookable_id
		 GROUP BY s.neighborhood
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

userstory_no = 12

userstory_description = '''
I am a potential guest
I want to find the average price of a stay by neighborhood
So that I can choose where to stay based on my budget
'''

query_description = '''
We return the average prices of all stays grouped by neighborhood.
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
average_price()

cur.close()
con.close()