""" Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

  """

def merge(intervals):
    

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    current_interval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            current_interval = interval
            result.append(current_interval)

    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))