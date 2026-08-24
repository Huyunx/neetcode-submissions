class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums2)==0):
            if(len(nums1)%2==1):
                return nums1[len(nums1)//2]
            else:
                return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        if(len(nums1)==0):
            if(len(nums2)%2==1):
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2
        
        npm=len(nums1)+len(nums2)
        numleft=npm//2
        i=0
        j=0
        l=0
        r=len(nums2)
        rightmin=0
        leftmin=0
        while True:
            m=(l+r)//2-1
            
           
            j=m+1
            i=numleft-j
            if(i<0):
                r=j
                continue
            m1=i-1
            print(f"m is {m}", file=sys.stderr)
            print(f"m1 is {m1}", file=sys.stderr)
            if((i>=len(nums1) or m<0 or nums2[m]<=nums1[i]) and (j>=len(nums2) or m1<0 or nums1[m1]<=nums2[j])):
                a=-1e6
                b=-1e6
                if(m1>=0):
                    a=nums1[m1]
                if(m>=0):
                    b=nums2[m]
                leftmax=max(a,b) #min(nums1[m1],nums2[m])
               
                a=1e6
                b=1e6
                if(i<len(nums1)):
                    a=nums1[i]
                if(j<len(nums2)):
                    b=nums2[j]
                rightmin=min(a,b)
                
                break
            if(i<len(nums1) and m>=0 and nums1[i]<nums2[m]):
                r=j-1
            if(j<len(nums2) and m1>=0 and nums2[j]<nums1[m1]):
                l=j+1
    
        if(npm%2==1):
            return rightmin
        else:
            a=(leftmax+rightmin)/2
            return a


