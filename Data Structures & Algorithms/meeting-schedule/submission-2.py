"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda s:(s.start,s.end))
        if(len(intervals)==0):
            return True
        prevend=intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start<prevend:
                return False
            else:
                prevend=intervals[i].end
        return True