class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=0
        y=len(numbers)-1
        while True:
            if(x>=y):
                break
            suma=numbers[x]+numbers[y]
            if(suma<target):
                x+=1
                continue
            if(suma>target):
                y-=1
                continue
            if(suma==target):
                return [x+1,y+1]
