sqaurelambda = lambda x:x*x

l = [1,2,3,4,5,6,7,8,9,10]

square_nums=[]
    
for i in l:
    n = sqaurelambda(i)
    square_nums.append(n)

print(square_nums)
