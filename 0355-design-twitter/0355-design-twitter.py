class Twitter:

    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        idx = len(self.tweets)-1
        while idx >= 0 and len(res) < 10:
            if (self.tweets[idx][0] in self.graph[userId]) or (self.tweets[idx][0] == userId):
                res.append(self.tweets[idx][1])
            idx -= 1
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


"""


"""