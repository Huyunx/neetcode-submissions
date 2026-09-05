class Twitter:

    def __init__(self):
        self.followlist={}#a:list
        self.tweetof={}#a:maxheap
        self.t=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetof[userId] = self.tweetof.get(userId, [])
        self.tweetof[userId].append((self.t, tweetId))
        self.tweetof[userId].sort()
        self.tweetof[userId].reverse()
        self.t += 1
        return 

    def getNewsFeed(self, userId: int) -> List[int]:
        thefollowlist=self.followlist.get(userId,[])
        #print("get", userId , thefollowlist, file=sys.stderr)
        #thefollowlist.append(userId)
        index={a:0 for a in thefollowlist+[userId]}#the indexes pointing to the front of the tweetlists of each followee
        pick=[]#maxheap
        ans = [] #list
        for f in thefollowlist+[userId]:
            if(not f in self.tweetof):
                continue
            tweets=self.tweetof[f]
            i=index[f]
            #print("tweet of", f,i , tweets, file=sys.stderr)
            if(i>=len(tweets)):
                continue
            time=tweets[i][0]#time created
            id=tweets[i][1]
            followee=f
            heapq.heappush_max(pick,(time,id,followee))
        while len(ans)!=10:
            
            if(not pick):
                break
            time,id,followee=heapq.heappop_max(pick)#this time the most recent 
            ans.append(id)
            index[followee]+=1
            i=index[followee]
            tweets = self.tweetof[followee]
            if(i<len(tweets)):
                time=tweets[i][0]#time created
                id=tweets[i][1]
                heapq.heappush_max(pick,(time,id,followee))

        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId==followeeId):
            return
        self.followlist[followerId] = self.followlist.get(followerId, [])

        if followeeId not in self.followlist[followerId]:
            self.followlist[followerId].append(followeeId)
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId not in self.followlist[followerId]):
            return 
        self.followlist[followerId].remove(followeeId)
        return
