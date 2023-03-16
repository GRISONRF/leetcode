# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

#Input: [[0,30],[5,10],[15,20]]
#Output: false

#Input: [[7,10],[2,4]]
#Output: true






# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#---------------------------#
# ****lambda is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression. -> 'lambda arguments : expression'

# in this question we need to first sort the intervals to make sure the start times are in order, and then compare the end time of the 1st interval to the start time to the 2nd interval and so on.

# to do this, we will use lambda to assign a variable 'key' as the start time and sort by that key.
# iterate through the values of the range of interval
# set up the 2 intervals we want to compare against each other.
# say if the end of first interval is greater than start of second interval, return false.
# else return true

# def canAttendMeetings(self, intervals):
    
#    intervals.sort(key = lambda i : i.start)   # sorting intervals by the start time of each obj

#    for i in range(1, len(intervals)): # starts at 1 because I want to compare the first agains the second
#         i1 = i[i-1] # 1 - 1 = 0 // thats the first interval
#         i2 = i[i]

#         if i2.start < i1.end:
#             return False
#         return True


""" 
input: list
ouput: boolean

are the intervals crossing one another? 
is the starting time of an interval greater than the end time of another interval?

sort the intervals by the starting time [s]  #[2,4][7,10]
iterate through intervals and check if interval[e] > interval+1[s] return false. if not, return true      # if 4>7, return true

"""

def intervals(intervals):
    
    sorted_intervals = sorted(intervals, key = lambda i : i[0])

    for i in range(len(sorted_intervals) - 1):
        if sorted_intervals[i][1] > sorted_intervals[i+1][0]:       
            return False
    return True



print(intervals([[0,30],[5,10],[15,20]]))





































