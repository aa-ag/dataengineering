############------------ IMPORTS ------------############
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def process_song_file(cursor, filepath):
    '''
     access song & song's artist data
     from a file via its path, prepare
     such data to be inserted into the db
     and then insert it
    '''
    # open song file
    df = ''

    # insert song record
    song_data = ''
    cursor.execute(
        song_table_insert, 
        song_data
    )
    
    # insert artist record
    artist_data = ''
    cursor.execute(
        artist_table_insert, 
        artist_data
    )


def process_log_file(cursor, filepath):
    # open log file
    df = ''

    # filter by NextSong action
    df = ''

    # convert timestamp column to datetime
    t = ''
    
    # insert time data records
    time_data = ''
    column_labels = ''
    time_df = ''

    for i, row in time_df.iterrows():
        cursor.execute(
            time_table_insert, 
            list(row)
        )

    # load user table
    user_df = ''

    # insert user records
    for i, row in user_df.iterrows():
        cursor.execute(
            user_table_insert, 
            row
        )

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cursor.execute(
            song_select, 
            (row.song, row.artist, row.length)
        )
        results = cursor.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = ''
        cursor.execute(
            songplay_table_insert, 
            songplay_data
        )


def process_data(cursor, connection, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cursor, datafile)
        connection.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    connection = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cursor = connection.cursor()

    process_data(
        cursor, 
        connection, 
        filepath='data/song_data', 
        func=process_song_file
    )
    process_data(
        cursor, 
        connection, 
        filepath='data/log_data', 
        func=process_log_file
    )

    connection.close()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    main()