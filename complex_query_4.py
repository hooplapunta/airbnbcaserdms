'''
11
MS
complex
Customer service representative
I want to be able to refund a user
So that I can facilitate a return between host and guest
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

def return_fn(confirmation_id):
	#given confirmation id
	#reverse and insert all items in the payment and payout tables with that confirmation id
	tmpl = '''
		CREATE VIEW Temp AS
		SELECT * 
		  FROM "payout"
		 WHERE "confirmation_id" = %s;

		INSERT INTO "payout" (paymentoption_id, amount, transaction_datetime)
		(SELECT paymentoption_id, amount, transaction_datetime
		   FROM "payment"
		  WHERE "confirmation_id" = %s);

		INSERT INTO "payout" (paymentoption_id, amount, transaction_datetime)
		(SELECT paymentoption_id, amount, transaction_datetime
		   FROM Temp
		  WHERE "confirmation_id" = %s);

		DROP VIEW Temp;
	'''
	#cmd = cur.mogrify(tmpl, (confirmation_id, confirmation_id, confirmation_id))
	#print_cmd(cmd)
	#cur.execute(cmd)

	tmpl = '''
		SELECT *
		  FROM "payout" as p
		 WHERE "confirmation_id" = %s;
	'''
	tup = tuple([confirmation_id])
	cmd = cur.mogrify(tmpl, tup)
	print_cmd(cmd)
	cur.execute(cmd)
	rows = cur.fetchall()
	print_rows(rows)

	tmpl = '''
		SELECT *
		  FROM "payment" as p
		 WHERE "confirmation_id" = %s;
	'''
	cmd = cur.mogrify(tmpl, tup)
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
I am a customer service representative.
I want to be able to refund a user
So that I can facilitate a return between host and guest
'''

query_description = '''
When given the confirmation_id of the reservation, we will switch 
the payment and payout tables for a given reservation such that 
the amount is refunded.
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
return_fn(1)

cur.close()
con.close()