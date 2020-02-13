#https://api.github.com/users/taylorotwell/events
import json
import requests
#archivo
with open('documento.json', 'r') as buffer:
    data = json.load(buffer)

#url
print ('Nombre de usuario que desea consultar:')
nombre = input()
URL='https://api.github.com/users/'+nombre+'/events'

resp = requests.get(URL)
data2=json.loads(resp.content)
def type(data):
    P="PushEvent"
    Cr="CreateEvent"
    I="IssuesEvent"
    Co="CommitCommentEvent"
    score=0
    i=0

    for i in range(len(data)):
        a=data [i]["type"]
     
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

a=type(data)
b=type(data2)
print ("GitHub Score:",a)
print ("GitHub Score:",b)
