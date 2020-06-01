import os, re


with open ('C:/lista de bitola_.txt',"r") as file1:
        bitola=[]
        bitola=file1.readlines()
file1.close()

with open ('C:/lista de material_.txt',"r") as file2:
        material=[]
        material=file2.readlines()
file2.close()

with open ('C:/espacos_.txt',"r") as file3:
        espacos=[]
        espacos=file3.readlines()
file3.close()




directory = os.listdir('/caminhodosarquivos')
os.chdir('/caminhodosarquivos')
adicionaesp=0 
espaco= []

num_de_espacos=400
esp=' '
for i in range(1,num_de_espacos+1):
    espaco.append(esp*i) # criando a lista
    
comparador = []
perfil = []
texto = []
comparador1 = []
read_file = []
arq_x=[]
arq=[]
a=[]
aux=0
aux2=0
es=[0]*400
contalinha=0
i=0
j=0
l=0
add=0
m=0
ediferente=0
comparador_1=[]

for file in directory:
    open_file = open(file,'r')
    texto= open_file.readlines()
    aux=str(texto[26])
    aux2=texto[31]
    comparador.append(aux)
    comparador1.append(aux2)
    i+=1
open_file.close()

for j in range(0,i):
    for  k in range(0,75): 
        if ((comparador[j] == bitola[k]) and (comparador1[j] == material[k])):    
            arq_x.append(int(espacos[k]))
            l=l+1
print(arq_x)








for l in range(0,l):
    aux=arq_x[l]
    es[l]=espaco[aux] 
print(es)
for file in directory:
    open_file = open(file,'r')
    read_file = open_file.read()
    regex = re.compile('POS_PEZ:')
    read_file = regex.sub('POS_PEZ:'+(str(es[m])),read_file) # aqui deve alterar para espaço dinamico
    write_file = open(file,'w')
    write_file.write(read_file)
    m+=1


