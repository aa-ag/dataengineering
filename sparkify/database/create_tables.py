############------------ IMPORTS ------------#######################
import psycopg2
import sql_queries


############------------ GLOBAL VARIABLE(S) ------------############
create_table_queries = sql_queries.create_table_queries
drop_table_queries = sql_queries.drop_table_queries


############------------ FUNCTION(S) ------------###################
def create_database():
    """
     - Creates and connects to the sparkifydb
     - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    connection = psycopg2.connect(
        "host=127.0.0.1 dbname=studentdb user=student password=student"
    )
    connection.set_session(autocommit=True)
    cursor = connection.cursor()
    
    # create sparkify database with UTF8 encoding
    cursor.execute(
        "DROP DATABASE IF EXISTS sparkifydb"
    )
    cursor.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"
    )

    # close connection to default database
    connection.close()    
    
    # connect to sparkify database
    connection = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    )
    cursor = connection.cursor()
    
    return cursor, connection


def drop_tables(cursor, connection):
    """
     Drops each table using the queries 
     in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cursor.execute(query)
        connection.commit()


def create_tables(cursor, connection):
    """
     Creates each table using the queries 
     in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cursor.execute(query)
        connection.commit()


def main():
    """
     - Drops (if exists) and Creates 
     the sparkify database. 
    
     - Establishes connection with 
     the sparkify database and gets
     cursor to it.  
    
     - Drops all the tables.  
    
     - Creates all tables needed. 
    
     - Finally, closes the connection. 
    """
    cursor, connection = create_database()
    
    drop_tables(cursor, connection)
    create_tables(cursor, connection)

    connection.close()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    main()