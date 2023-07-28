-- https://datalemur.com/questions/sql-histogram-tweets


-- Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket.
-- In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group.

-- tweets Table:
-- Column Name	Type
-- tweet_id	integer
-- user_id	integer
-- msg	string
-- tweet_date	timestamp

-- tweet_bucket	users_num
-- 1	2
-- 2	1
-- Explanation:
-- Based on the example output, there are two users who posted only one tweet in 2022, and one user who posted two tweets in 2022. The query groups the users by the number of tweets they posted and displays the number of users in each group.


with cnt_table AS (
  SELECT 
    user_id,
    count(*) AS tweet_count
  FROM tweets 
  WHERE EXTRACT(YEAR FROM tweet_date) = 2022
  GROUP BY user_id
)
SELECT 
  tweet_count AS tweet_bucket,
  count(*) AS users_num
FROM cnt_table
GROUP BY tweet_count
;