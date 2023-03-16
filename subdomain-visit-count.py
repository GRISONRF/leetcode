"""A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com".
When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself."""


# Input: cpdomains = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]

# create a dict where I'm gonna store the number of times the domain was visited + domain
# iterate through the domains
# split the number and the domain
# split the domains on dots
# iterate through domain
# store in the dictionary: each peace of the domain + number 
# return the information in the dictionary but as a string, using an f{}.
import collections 

def subdomainVisits(cpdomains):
 
    # counts = collections.defaultdict(int)  # works as a counting. when I pass a key into counts, and do += 1, it will sum up to the value at every same key.

    # for domain in cpdomains:   #domain = 9001 discuss.leetcode.com
    #     # print(domain)
    #     count, domain = domain.split()  # '9001', 'discuss.leetcode.com', assigning first split to count, second split to domain
    #    # print((count))
    #     # print(domain)
    #     count = int(count)   #[9001]
    #     domain = domain.split('.')  # ['discuss', 'leetcode', 'com']
    #     # print(domain)

    #     #need to iterate through the domain to check each fragment of the domain and add to the dictionary with respective count.

    #     #to itetrate adding one domain at a atime, just goin with the domain at changing index
    #     for i in range(len(domain)):
    #         if '.'.join(domain[i:]) in counts:
    #             counts['.'.join(domain[i:])] += count
    #         else: 
    #             counts['.'.join(domain[i:])] = count

       

    # return [f"{count} {domain}" for domain, count in counts.items()] # list comprehension. "expression for item in list" in this case, : print count and domain for each key and value of the dict. 

####################################################################################

    # create a dict
    counts = collections.defaultdict()

    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        domain = domain.split(".")
        print(count, domain)

        for i in range(len(domain)):
            if ".".join(domain[i:]) not in counts:
                counts[".".join(domain[i:])] = count
            else:
                counts[".".join(domain[i:])] += count
        
        print(counts)
        ans = []
        for domain, count in counts.items():
            ans.append(f'{count} {domain}')
        return ans
            

        









print(subdomainVisits(["9001 discuss.leetcode.com", "10 google.leetcode.com"]))


#https://www.youtube.com/watch?v=pF7jZ8YL6Rs
#https://pythontutor.com/render.html#mode=display
#https://docs.python.org/3/library/collections.html