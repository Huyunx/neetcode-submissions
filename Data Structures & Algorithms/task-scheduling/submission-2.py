class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        mapp={}
        coolling=deque([])
        for i in tasks:
            mapp[i]=mapp.get(i,0)+1
        for i in mapp:
            heapq.heappush(heap,-mapp[i])
        currtime=0
        while coolling or heap:
            currtime+=1
            if(coolling and currtime>=coolling[0][0]):
                heapq.heappush(heap,coolling[0][1])
                coolling.popleft()
            if(heap):
                currfreq=heapq.heappop(heap)
                if(currfreq!=-1):
                    coolling.append((currtime+n+1,currfreq+1))
            else:
                currtime = coolling[0][0]-1
        return currtime