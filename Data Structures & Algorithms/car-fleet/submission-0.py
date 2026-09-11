class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort()
        time=[]
        for i in cars:
            p=i[0]
            s=i[1]
            time.append((target-p)/s)
        compare=time[-1]
        ans=1
        for i in range(len(time)-1,-1,-1):
            if(time[i]>compare):
                ans+=1
                compare=time[i]
        return ans
