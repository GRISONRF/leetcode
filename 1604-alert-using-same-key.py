class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        #keyname
        #ketime
        
        #-> track who used the card 3 or more times within 1h period
        # daniel : [time, time time] -> convert time from string to minutes (hour * 60 + min)

        # using a sliding window keep track of how many times they used the key within 60min


        #create a dict 
        workers = {}
        #zip name and time together to map them converting time to minutes
        for name, times in zip(keyName, keyTime):
            if name not in workers:
                workers[name] = []
            h, m = times.split(":")
            workers[name].append(int(h) * 60 + int(m))

        
        #sort workers name
        worker_names = list(workers.keys())
        worker_names.sort()
        
        result = []
        #iterate over names and sort times
        for name in worker_names:
            time = workers[name]
            time.sort()
        
            j, i = 0, 0
            while j < len(time):
                #check if time j - i within 1h
                if time[j] - time[i] <= 60:   
                    j += 1
                    if j - i >= 3: #if all 3 numbers between j and i happened between 1h
                        #append name in result
                        result.append(name)
                        break                   
                else:
                    #keep going
                    i += 1
                    j += 1
            
        return result    