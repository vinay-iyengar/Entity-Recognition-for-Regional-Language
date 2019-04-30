# path='C:/Users/Venu/Desktop/fyproject/data/kannada.txt'
path_file="./data/kannada_testing.txt"

list=[':',',','?','.','"','\'','(',')','[',']','!','@','#','$','%','^','&','*','+','-','=','/',';','{','}','<','>']
    
# f=open(path,"r")
# f1=f.read()

# for i in list:
#     f1=f1.replace(i,'')
# a=f1
# f.close()

# b=open(path,"w")
# b.write(a)
# b.close()

p=open(path_file,"r")
p1=p.read()

for i in list:
    p1=p1.replace(i,'')
c=p1
p.close()

p=open(path_file,'w')
p.write(c)
p.close()
    
    #print(msg1[:-1])

#print("\nStop Word removal:",msg1)
#print("\nTokentization:",msg1.split())
#f1=f1.split()
#print("tokenization:")
#print(f1)
#print(b)
 

