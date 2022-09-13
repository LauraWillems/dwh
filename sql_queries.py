import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events cascade"
staging_songs_table_drop = "DROP TABLE IF EXISTS taging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

### Not sure how this fits in
#CREATE SCHEMA IF NOT EXISTS songs;
#SET search_path TO songs;
###

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
artist varchar,
auth varchar,
firstName varchar,
gender varchar,
ItemInSession int,
lastName varchar,
length float,
level varchar,
location varchar,
method varchar,
page varchar,
registration float,
sessionId int,
song varchar,
status int,
ts timestamp,
userAgent varchar,
userId int NOT NULL
)
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
num_songs int,
artist_id varchar,
artist_latitude float,
artist_longitude float,
artist_location float,
artist_name varchar,
song_id varchar NOT NULL,
title varchar NOT NULL,
duration numeric NOT NULL,
year int
)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
songplay_id int IDENTITY(0,1), 
start_time timestamp NOT NULL, 
user_id int NOT NULL, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id int, 
location varchar, 
user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id int, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar, 
title varchar NOT NULL, 
artist_id varchar NOT NULL, 
year int, 
duration numeric NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar, 
name varchar NOT NULL, 
location varchar, 
latitude float, 
longitude float
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time timestamp, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int
)
""")

# STAGING TABLES

#staging_events_copy = ("""
#copy staging_events from 's3://udacity-dend/log_data'  
#iam_role '"arn:aws:iam::574680955753:role/dwhRole"'
#FORMAT as JSON 's3://udacity-dend/log_json_path.json'
#gzip region 'us-west-2';
#""").format(config.get('IAM_ROLE','ARN'))

staging_events_copy = ("""
    COPY staging_events FROM {}
    credentials 'aws_iam_role={}'
    gzip region 'us-west-2'
    FORMAT as json {};
""").format(config.get('S3','LOG_DATA'), config.get('IAM_ROLE','ARN'),config.get('S3','LOG_JSONPATH'))

staging_songs_copy = ("""
    copy staging_songs from 's3://udacity-dend/song_data' 
    credentials 'aws_iam_role={}'
    gzip region 'us-west-2';
""").format(*config['IAM_ROLE'].values())


# FINAL TABLES

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

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
