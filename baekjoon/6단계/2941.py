word = input()
croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatia_list:
    word = word.replace(c, '*')
    
print(len(word))