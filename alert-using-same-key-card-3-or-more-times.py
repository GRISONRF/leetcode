"""LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period."""
import collections 
import queue

from email.policy import default


def alertNames(keyName, keyTime):

    n = len(keyName)

    times = collections.defaultdict(list)

    for i in range(n):
        name = keyName[i]
        time = keyTime[i]

        t = time.split(':')
        h = int(t[0])
        m = int(t[1])

        times[name].append(h*60+m)

    ans = []

    for name in times:
        time_list = sorted(times[name])

        queue = queue.deque()

        for time in time_list:
            queue.append(time)

            while time - queue[0] > 60:
                queue.popleft()

            if len(queue) >= 3:
                ans.append(name)
                break
    return sorted(ans)





print(alertNames(["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]))


