immutable_var=(2, 'apple', True)
print(immutable_var)
#immutable_var[0]=1
#print(immutable_var)# в данном кортеже нет изменяемых элементов, как например (2,['apple'], True
mutable_list=[2,3,4,"тэндер", False]
mutable_list[0]=0
mutable_list[2]='колосья'
print(mutable_list)