from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)  # userId -> [(time, tweetId), ...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = set(self.following[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx - 1))

        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId, uid, next_idx = heapq.heappop(heap)
            feed.append(tweetId)

            if next_idx >= 0:
                time, next_tweetId = self.tweets[uid][next_idx]
                heapq.heappush(heap, (-time, next_tweetId, uid, next_idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
