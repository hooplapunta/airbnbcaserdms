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

def return_fn(invoice_number):
	#given reservation id
	#reverse all items in the payment and payout tables
	tmpl = '''
		CREATE VIEW Temp AS
		SELECT * 
		  FROM "payout"
		 WHERE "invoice_number" = %s;

		DELETE FROM "payout"
		 WHERE "invoice_number" = %s;

		INSERT INTO "payout" (amount, transaction_datetime)
		(SELECT * FROM "payment"
				 WHERE "invoice_number" = %s);

		DELETE FROM "payment" 
		 WHERE "invoice_number" = %s;

		INSERT INTO "payout" (amount, transaction_datetime)
		(SELECT * FROM Temp
		  WHERE "invoice_number" = %s);
	'''
	cmd = cur.mogrify(tmpl, (invoice_number, invoice_number, invoice_number, invoice_number, invoice_number))
	print_cmd(cmd)
	cur.execute(cmd)

	tmpl = '''
		SELECT *
		  FROM "payout" as p;
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
I am a customer service representative.
I want to be able to refund a user
So that I can facilitate a return between host and guest
'''

query_description = '''
We will switch the payment and payout tables for a given reservation
such that the amount is refunded.
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