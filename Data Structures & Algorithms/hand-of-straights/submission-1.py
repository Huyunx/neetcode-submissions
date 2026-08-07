class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize!=0):
            return False
        hand.sort()
        meettime={}
        for i in hand:
            meettime[i]=meettime.get(i,0)+1
        firstnums=[]
        nextfirstindex=0
        for i in range(len(hand)//groupSize):
            firstnums.append(hand[i])
        for a in hand:
            if(a in meettime):
                for i in range(a,a+groupSize):
                    if i in meettime:
                        meettime[i]-=1
                    else:
                        return False
                    if(meettime[i]==0):
                        del meettime[i]
        return True
