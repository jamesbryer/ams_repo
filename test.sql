/* i have 2 tables, a ratings table with the foreign key 
movie_id linking to the movies table. I want to retrieve 
all movie titles (column called title) and their ratings 
from the ratings table (column called rating) so long as 
the rating is 4 or higher and also list how many ratings 
each movie has.

THEN 

i want to only have 1 record for each movie, with the average rating from the ratings table and the number of ratings count

I have to change the some of the column names to make it work as chatGPT didn't know what they were called. 
 */

SELECT m.title, ROUND(AVG(r.rating), 2) AS average_rating, COUNT(r.rating) AS rating_count
FROM movies AS m
JOIN ratings AS r ON m.id = r.movie_id
GROUP BY m.title
ORDER BY average_rating DESC;