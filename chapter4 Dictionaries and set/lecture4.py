# #dictionary

# info={
#     "key":"value",
#     "name":"vansh mehta",
#     "subjects":["jave","c","python"],
#     "topics":("dict","set"),
#     "learning":"coding",
#     "age": 35,
#     "is adult": True,
#     "marks": 90,
# }
# print(info)
# print(info["name"])
# print(info["topics"])
# info["name"]="Vansh"
# print(info)

# null_dict={}
# null_dict["name"]="Vansh"
# print(null_dict)

#Nested Disctionary

# student={
#         "name": "Vansh",
#         "score": {
#             "chem": 98,
#             "phy":95,
#             "math":94,
#         }
#     }
# print(student)
# print(student["score"]["math"])


#dictnaries methods

# student={
#         "name": "Vansh",
#         "score": {
#             "chem": 98,
#             "phy":95,
#             "math":94,
#         }
#     }

# print(student.keys())# dict_keys(['name', 'score'])
# #type casting to list
# # print(list(student.keys()))
# print(student.values())# dict_values(['Vansh', {'chem': 98, 'phy': 95, 'math': 94}])
# print(student.items()) #returns tuples  # dict_items([('name', 'Vansh'), ('score', {'chem': 98, 'phy': 95, 'math': 94})])
# print(student.get("name1")) #no error as it returns none. if we noramally access using print(student["name"]) this will generate error

# new_dict={
#     "city": "new dehli"
# }
# student.update(new_dict) # {'name': 'Vansh', 'score': {'chem': 98, 'phy': 95, 'math': 94}, 'city': 'new dehli'}
# print(student)



#SET In Python


# collection={1,2,2,2,3,4,"Vansh"}

# print(collection)
# print(type(collection))
# print(len(collection)) #length of set


# collection= set() #empty set
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# #collection.remove(7)#error as it does not exist in the set
# collection.add("vansh")
# collection.add((1,2,3))
# # collection.add([1,2,3]) #TypeError: unhashable type: 'list' as list is mutable
# print(len(collection))
# collection.clear()
# print(len(collection))
# print(collection)

# collection={"hello","vansh","world","coding","python"}
# print(collection.pop())
# print(collection.pop())#rendom values


set1={1,2,3}
set2={2,3,4}

print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{2,3}

