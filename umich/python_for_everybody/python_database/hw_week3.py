import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('hw3.sqlite')
cur = conn.cursor()

# Create some tables in the database
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# Read the XML file
fname = 'data/Library.xml'

def lookup(d, key):
    '''
    Parameters
    ----------
    d : dictionary

    key : string
    '''
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# Create XML ET object
stuff = ET.parse(fname)

# Find all dictionary tags (nested as well)
all = stuff.findall('dict/dict/dict')

print('Dict count:', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or genre is None or album is None:
        continue

    print(name, artist, genre, album, count, rating, length)

    # Artist name must be unique. If exist, ignore
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, )
    )

    # Get the artist id of the previously inserted/not inserted data
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # Genre must be unique. If exist, ignore
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre, ))

    # Get the genre id of the track
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    # If exist, it will be an update. This only exist in sqlite
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count))

    conn.commit()
