class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.median=0
        self.even=True

    def addNum(self, num: int) -> None:
        
        if(self.even):
            self.even = False

        else:

            self.median+=1
            self.even=True

        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        if(self.even):
            return (self.arr[self.median]+self.arr[self.median-1])/2
        else:
            return self.arr[self.median]
        