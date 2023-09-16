# marks = [50,20,90,65,98,98]
# print(marks)
friends = ['hari','sai','kiran','nitin','vineeth']
# print(friends)
# # empty list - list with out any items
# dislikers  = []
# print(len(dislikers))
# # can we keep list inside another list ?
# bioDatalist=[27,"2222222","address",friends]
# print(bioDatalist[3][2])
# print(bioDatalist)
# print('second friend',friends[-1])
# # -----------------------------------------------------
# # slicing same as string
# # -----------------------------------------------------
# # Mutable - update
# marks[1] = 98
# print(marks)
# # concatatiion & repeating same as string
# print(marks+friends)
# print(friends*2)
# # -----------------------------------------------
# # add new  items - append()- single item ,extend() - more items
# friends.append("robin")
# print(friends)
# friends.extend(["hello","World","kajol"]) # while using extend use squre brackec
# print(friends)
# # how to specific position  - use - insert
# friends.insert(1,"haresh")
# print(friends)
# # ----slicing - to add muliple values
# friends[1:1] = ["a","b",'c']
# print(friends)
# # --------------------------------Delete----
# del friends[1]
# print(friends)
# del friends
# # del friends[1:3]
# ------------------------------remove,pop,pop(index)
# remove - use to remove an item from the list
# pop(index) - remove and return item at specified index
# pop() - remove and return last item from the list
friends.remove('sai')
print(friends)
print(friends.pop(1))
print(friends.pop())
print(friends.clear())

