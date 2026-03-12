-- write a SQL query to list the titles of all movies released in 2008

SELECT title
FROM movies
WHERE year = 2008

-- CREATE TABLE transactions (
--     user_id INTEGER NOT NULL,
--     transaction_id INTEGER NOT NULL UNIQUE,
--     symbol TEXT NOT NULL,
--     qtd INTEGER NOT NULL,
--     date TEXT NOT NULL,
--     FOREIGN KEY(user_id) REFERENCES users(id)
-- );

-- CREATE TABLE total (
--     user_id INTEGER NOT NULL,
--     company_id INTEGER NOT NULL UNIQUE,
--     symbol TEXT NOT NULL UNIQUE,
--     total_shares INTEGER,
--     FOREIGN KEY(user_id) REFERENCES users(id)
-- );

-- CREATE TABLE directors (
--     movie_id INTEGER NOT NULL,
--     person_id INTEGER NOT NULL,
--     FOREIGN KEY(movie_id) REFERENCES movies(id),
--     FOREIGN KEY(person_id) REFERENCES people(id)
-- );
-- CREATE TABLE movies (
--     id INTEGER,
--     title TEXT NOT NULL,
--     year NUMERIC,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE people (
--     id INTEGER,
--     name TEXT NOT NULL,
--     birth NUMERIC,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE ratings (
--     movie_id INTEGER NOT NULL,
--     rating REAL NOT NULL,
--     votes INTEGER NOT NULL,
--     FOREIGN KEY(movie_id) REFERENCES movies(id)
-- );
-- CREATE TABLE stars (
--     movie_id INTEGER NOT NULL,
--     person_id INTEGER NOT NULL,
--     FOREIGN KEY(movie_id) REFERENCES movies(id),
--     FOREIGN KEY(person_id) REFERENCES people(id)
-- );
