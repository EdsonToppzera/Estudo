--write a SQL query to list the id and names of all people who starred in a movie released in 2004, ordered by birth year

-- Select names
SELECT id, name
FROM people
WHERE id IN (
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id IN (
        SELECT id
        FROM movies
        WHERE year=2004
    )
)
ORDER BY birth;

