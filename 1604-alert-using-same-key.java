class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        

        //create a dict to map name and times
        Map<String, List<Integer>> workers = new HashMap<>();
        //for the times->store them as int, converting them into minutes
        for (var i = 0; i < keyName.length; i ++){
            String name = keyName[i];
            String time = keyTime[i];

            String[] splitTime = time.split(":");
            int h = Integer.parseInt(splitTime[0]);
            int m = Integer.parseInt(splitTime[1]);
                     
            if (!workers.containsKey(name)){
                workers.put(name, new ArrayList<>());
            }
            workers.get(name).add(h * 60 + m);
        }
       

        //initialize result list
        List<String> result = new ArrayList<>();

        //sort workers name and time
        Map<String, List<Integer>> sortedWorkers = new TreeMap<>(workers);


        //iterate over dict
        for (String name : sortedWorkers.keySet()){
            
            //initialize i and j as 0 to keep track of the window we want to check for the key usages
            int j = 0;
            int i = 0;
            
            //while j <= len of times
            while (j < sortedWorkers.get(name).size()){
                //check if time at j - time at i is less than 1h
                List<Integer> times = sortedWorkers.get(name);
                Collections.sort(times);
                if (times.get(j) - times.get(i) <= 60){   
                    //if it is, we update j +=1
                    j+=1;
                    //want to check if we're in the 3rd iteration 
                    if (j - i >= 3){
                        //if we are, means this person used the key 3x in 1h -> add name into the result list
                        result.add(name);
                        //break the loop to go to the next person
                        break;
                    }
                    //else: if user didnt use the key within 1h
                } else {
                    // if (times.get(j) - times.get(i) <= -1440){
                    //     s
                    // }
                    //update j and i
                    i+=1;
                }
            }
        }
        //return result
        return result;
        


       
    }
}