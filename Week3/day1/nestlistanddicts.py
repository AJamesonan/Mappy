x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1)
x[1][0] = 15
print(x)

# 2)
students[0]["last_name"] = 'Bryant'
print(students[0]["last_name"])

# 3)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

#4)
z[0]['y'] = 30
print(z[0]['y'])

# part 2
def iterateDictionary(some_list):
    for list in some_list:
        for key, val in list.items():
            print(key, '-',val)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    i = 0
    for dics in some_list:
        print(some_list[i][key_name])
        i += 1


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# # Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict.keys():
        print(len(some_dict[key]), key)
        for val in some_dict[key]:
            print(val)
            

printInfo(dojo)