### DROP TABLES #####################################################
### drops songsplays table
songplay_table_drop = """
DROP TABLE IF EXISTS songplays;
"""

### drops users table
user_table_drop = """
DROP TABLE IF EXISTS users;
"""

### drops songs table
song_table_drop = """
DROP TABLE IF EXISTS songs;
"""

### drops artists table
artist_table_drop = """
DROP TABLE IF EXISTS artists;
"""

### drops time table
time_table_drop = """
DROP TABLE IF EXISTS time;
"""


### CREATE TABLES ###################################################
### creates songplays table
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id bigint PRIMARY KEY, 
    start_time timestamp, 
    user_id bigint, 
    level varchar,
    song_id bigint, 
    artist_id bigint,
    session_id bigint,
    location text,
    user_agent text
        CONSTRAINT fk_user_id
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
""")
# \COPY songplays FROM '...'
# this one will be created after all others,

### creates users table
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id bigint PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar(1),
    level varchar
);
""")

### creates songs table
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id text PRIMARY KEY,
    title text,
    artist_id text,
    year integer,
    duration numeric
);
""")

### creates artists table
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id text PRIMARY KEY,
    name text,
    location text,
    latitude numeric,
    longitude numeric
);
""")

### creates time table
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp,
    hour timestamp,
    day timestamp,
    week timestamp,
    month timestamp,
    year timestamp,
    weekday timestamp
);
""")
# hour SELECT EXTRACT(HOUR FROM TIMESTAMP start_time),
# day SELECT EXTRACT(DAY FROM TIMESTAMP start_time),
# week SELECT EXTRACT(WEEK FROM TIMESTAMP start_time),
# month SELECT EXTRACT(MONTH FROM TIMESTAMP start_time),
# year SELECT EXTRACT(YEAR FROM TIMESTAMP start_time),
# weekday SELECT EXTRACT(DOW FROM TIMESTAMP start_time)

### INSERT RECORDS ##################################################
### inserts record into songplays table
songplay_table_insert = ("""
INSERT INTO songplays (
    songplay_id PRIMARY KEY, 
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

### inserts record into users table
user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level
) VALUES (%s, %s, %s, %s, %s);
""")

### inserts record into songs table
song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
) VALUES (%s, %s, %s, %s, %s);
""")

### inserts record into artists table
artist_table_insert = ("""
INSERT INTO songs (
    artist_id, 
    name,
    location, 
    latitude, 
    longitude
) VALUES (%s, %s, %s, %s, %s);
""")

### inserts record into time table
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
### lists queries that create tables
create_table_queries = [
    songplay_table_create, user_table_create, song_table_create, 
    artist_table_create, time_table_create
]

### lists queries that delete tables
drop_table_queries = [
    songplay_table_drop, user_table_drop, song_table_drop, 
    artist_table_drop, time_table_drop
]