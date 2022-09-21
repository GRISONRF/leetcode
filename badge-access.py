"""We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.
"""

""" input =>
badge_records_1 = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"]
["Paul", "enter"],
["Curtis", "exit"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Martha", "exit"],
]

output = > ["Curtis", "Paul"], ["Martha", "Curtis"]

"""



def get_bad_access(records):

    # var didnt_enter
    # var didnt_exit
    # var room
    forgot_enter = set()
    forgot_exit = set()
    room = set()

    for name, status in records:
        # if the person entered
        if status == "enter":
            #if already in the room #means they forgot to exit
            if name in room:
                #add the person to the didnt_exit
                forgot_exit.add(name)
            #if the person not in te room, 
                #add person in the room
            else:
                room.add(name)

        # if the person exited
        elif status == "exit":
            # if person in the room #means they entered
            if name in room:
                # take them out of the room
                room.discard(name)
            # if person is not in the room #means they forgot to enter 
                #add to the didnt_enter
            else:
                forgot_enter.add(name)

    #if there is someone in the room,
    for person in room:
        forgot_exit.add(person)
            
        # add to the didnt_exit
    return list(forgot_exit), list(forgot_enter)

    
    
print(get_bad_access([
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "exit"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Martha", "exit"],
]))




