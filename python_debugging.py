#using the pdb python debugger
import pdb
#setting up where you begin your debugging it might be from the top as in this case
pdb.set_trace()
a = 'aaa'
b = 'bbb'
c = 'ccc'
final = a+b+c
print(final)