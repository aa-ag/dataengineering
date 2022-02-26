### DROP TABLES #####################################################
songplay_table_drop = """
DROP TABLE IF EXISTS songplays;
"""

user_table_drop = """
DROP TABLE IF EXISTS users;
"""

song_table_drop = """
DROP TABLE IF EXISTS songs;
"""

artist_table_drop = """
DROP TABLE IF EXISTS artists;
"""

time_table_drop = """
DROP TABLE IF EXISTS time;
"""


### CREATE TABLES #####################################################
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(songplay_id bigint PRIMARY KEY, start_time timestamp, FOREIGN KEY(user_id bigint), level int, 
FOREIGN KEY(song_id bigint), FOREIGN KEY(artist_id bigint), FOREIGN KEY(session_id bigint), 
location text, user_agent);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(user_id bigint PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level int);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(song_id bigint PRIMARY KEY, title text, artist_id bigint, year timestamp, duration numeric);
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

### INSERT RECORDS #####################################################
songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")


### FIND SONGS ###################################################
song_select = ("""
""")


### QUERY LISTS ###################################################
create_table_queries = [
    songplay_table_create, user_table_create, song_table_create, 
    artist_table_create, time_table_create
]

drop_table_queries = [
    songplay_table_drop, user_table_drop, song_table_drop, 
    artist_table_drop, time_table_drop
]