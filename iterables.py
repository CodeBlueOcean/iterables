user = {
    'name':'Golem',
    'age': 5006,
    'can_swim': False
}

# for item in user.items():
#     print(item)

# for item in user.items():
#     key, value = item;
#     print(key, value)

## above another shorthand
for key, value in user.items():
    print(key, value)

## above another shorthand
for k, v in user.items():
    print(key, value)

for item in 50:
    print(item)
#line 22 not working because
#iterable - list, dicitionary, tuple, set, string

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
#         print(1, 'c')
        
#iterable - list, dicitionary, tuple, set, string
#iterate -> one by one check each item
#in the collection. 