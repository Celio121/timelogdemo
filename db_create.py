from app import db_create, time_in, time_out

# Call db_create() first
db_create()

# Then call the other functions
time_in('testin', 'testinsur')
time_out('testout', 'testoutsur')
