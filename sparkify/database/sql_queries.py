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


### CREATE TABLES ###################################################
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id bigint PRIMARY KEY, 
    start_time timestamp, 
    FOREIGN KEY(user_id bigint), 
    level int,
    FOREIGN KEY(song_id bigint), 
    FOREIGN KEY(artist_id bigint),
    FOREIGN KEY(session_id bigint),
    location text,
    user_agent
);
""")
# \COPY songplays FROM '...'
# this one will be created after all others,

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id bigint PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar(1),
    level int
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id bigint PRIMARY KEY,
    title text,
    artist_id bigint,
    year timestamp,
    duration numeric
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id bigint PRIMARY KEY,
    name text,
    location text,
    latitude numeric,
    longitude numeric
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp,
    hour SELECT EXTRACT(HOUR FROM TIMESTAMP start_time),
    day SELECT EXTRACT(DAY FROM TIMESTAMP start_time),
    week SELECT EXTRACT(WEEK FROM TIMESTAMP start_time),
    month SELECT EXTRACT(MONTH FROM TIMESTAMP start_time),
    year SELECT EXTRACT(YEAR FROM TIMESTAMP start_time),
    weekday SELECT EXTRACT(DOW FROM TIMESTAMP start_time)
);
""")

### INSERT RECORDS ##################################################
songplay_table_insert = ("""
INSERT INTO songplays (
    songplay_id, 
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location,
    user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")


user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level
) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
INSERT INTO songs (
    artist_id, 
    name,
    location, 
    latitude, 
    longitude
) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO songs (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")


### FIND SONGS ######################################################
# find the song ID and artist ID 
# based on the title, artist name, and duration of a song.
song_select = ("""
SELECT 
    song_id, artist_id
FROM
    songs
JOIN artists ON songs.artist_id = artists.artist_id
WHERE title = %s
AND name = %s
AND duration = %s
""")


### QUERY LISTS #####################################################
create_table_queries = [
    songplay_table_create, user_table_create, song_table_create, 
    artist_table_create, time_table_create
]

drop_table_queries = [
    songplay_table_drop, user_table_drop, song_table_drop, 
    artist_table_drop, time_table_drop
]