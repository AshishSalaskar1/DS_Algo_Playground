from queue import PriorityQueue
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.time = 0
        self.tweets = defaultdict(list) # userId: []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = [userId, *self.followers[userId]]
        feed = []
        print(followees)

        # (timestamp, tweetId, whoTweetedThis, indexOfTweet)
        pq = PriorityQueue()
        
        for followee_id in followees:
            # if this person had tweeted
            if followee_id in self.tweets and len(self.tweets[followee_id]) != 0: 
                last_tweet_idx = len(self.tweets[followee_id])-1 # get last idx
                timestamp, tweet = self.tweets[followee_id][last_tweet_idx]
                pq.put( (-timestamp, tweet, followee_id, last_tweet_idx))
        
        print(pq.queue)
        while not pq.empty() and len(feed) < 10:
            print(feed, pq.queue)
            latest = pq.get()
            feed.append(latest[1])

            # last_index-1, moving oldest <- latest
            last_tweet_idx = latest[3]-1

            print(last_tweet_idx)
            if last_tweet_idx >= 0:
                followee_id = latest[2]
                pq.put((
                    -self.tweets[followee_id][last_tweet_idx][0], # tweet timestamp
                    self.tweets[followee_id][last_tweet_idx][1],  # tweet id
                    followee_id, 
                    last_tweet_idx
                ))
        
        return feed


    def follow(self, userId: int, followedId: int) -> None:
        # USER follows FOLLOWEE
        self.followers[userId].add(followedId)
        

    def unfollow(self, userId: int, followeeId: int) -> None:
        # USER unfollows FOLLOWEE
        if followeeId in self.followers[userId]:
            self.followers[userId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)