import json
import requests

print ('Nombre de usuario que desea consultar:')
nombre = input()
print ('Nombre de usuario:',nombre)

#funcion score events
def type(n):
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
a=type(nombre)
print ('GitHub events Score:',a)


#funcion Followers
def Followers(n):
    a=0
    
    URL='https://api.github.com/users/'+n
    resp = requests.get(URL)
    data=json.loads(resp.content)
    a=data["followers"]
    
    return a
b=Followers(nombre)
print('Numero de seguidores:',b)

#funcion Stars
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
c=Stars(nombre)
print('Numero total de estrellas:',c)

PuntajeTotal=((a*0.4)+(c*0.4)+(b*0.2))
print ("Puntaje Total:",PuntajeTotal)

#funcion id
def id(n):
    a=0
    
    URL='https://api.github.com/users/'+n
    resp = requests.get(URL)
    data=json.loads(resp.content)
    a=data["login"]
    
    return a
m=id(nombre)
print('ID:',m)