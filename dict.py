xs=[1,1,1,2,3,3,4,5,5]

my_dict = {}

for i in range(len(xs)):
    
    my_dict[xs[i]] = xs.count(xs[i])
    
print(my_dict)
