import json
import requests

print ('Nombre de los usuarios que desea consultar:')
nombre = input()
nombre1= input()
#Funcion Score Events
def Tipe(n):
    P="PushEvent"
    Cr="CreateEvent"
    I="IssuesEvent"
    Co="CommitCommentEvent"
    score=0
    i=0
    
    URL='https://api.github.com/users/'+n+'/events'
    resp = requests.get(URL)
    data=json.loads(resp.content)

    for i in range(len(data)):
        a=data[i]["type"]
     
        if P == a:            
            score=score+5
        elif Cr==a:            
            score=score+4
        elif Co==a:            
            score=score+2
        elif I==a:
            score=score+3            
        else:
            score=score+1
    return score

#Funcion Followers
def Followers(n):
    a=0    
    URL='https://api.github.com/users/'+n
    resp = requests.get(URL)
    data=json.loads(resp.content)
    a=data["followers"]
    
    return a

#Funcion Stars
def Stars(n):
    k=0
    a=0
    cont=0
    URL='https://api.github.com/users/'+n+'/repos'
    resp = requests.get(URL)
    data=json.loads(resp.content)
    for k in range(len(data)):
        a=data[k]["stargazers_count"]
        cont=cont+a
    return cont

#Funcion Puntajetotal
def Puntajet(n):
    a=Tipe(n)
    b=Followers(n)
    c=Stars(n)
    PuntajeTotal=((a*0.4)+(c*0.4)+(b*0.2))
    return PuntajeTotal

#Funcion Battle
def Battle(n,n1):
    print ('Nombre del primer usuario:',n)
    print ('Nombre del segundo usuario',n1)
    p1=Puntajet(n)
    print (me,p1)
    p2=Puntajet(n1)
    print(mo,p2)

    if p1 < p2:
        return n1
    elif p1>p2:
        return n
    else:
        h="Empate"
        return h

#Funcion para Escribir en un archivo de texto 
def Escribir(n):
    a=Puntajet(n)
    URL=':     https://api.github.com/users/n'+n+'     '
    Apuntes=str(a)
    f = open ('datos_puntajes.txt','a')
    juntar=n+URL+Apuntes+'\n'
    f.write(juntar)
    f.close()
    
Escribir(nombre1)
Escribir(nombre)