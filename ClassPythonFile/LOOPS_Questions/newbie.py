x = ['apple', 'banana', 'cherry']

# generates a iterator of tuples...
for d in enumerate(x):
    print(d)


# zip()

a = ('csk','mi','rcb','kkr')
b = (4,4,0,1)
print(zip(a,b))
print(list(zip(b,a)))