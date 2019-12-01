# If Airbnb used a RDMS

This database project implements a relational database for an Airbnb case study.

## Setup & Run

Given a PostgresSQL database with the user `isdb`, run the following:
`% psql -d postgres -U isdb -f project_reset.sql`

The database `project` will be created and loaded.

You can then run the various query files with python, for example:
`% python simple_query_1_us1.py`

