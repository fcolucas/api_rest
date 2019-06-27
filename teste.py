import json
import requests

#GET - requisitando dados
response = requests.get("http://jsonplaceholder.typicode.com/comments")

#print (response.status_code)

comments = json.loads(response.content) #transforma json em objeto 

# print (comments[0]) #mostrando conteudo por indice

#print (comments[0]['body']) #mostrando conteudo por dict key

#requisitando por ID
res = requests.get("http://jsonplaceholder.typicode.com/comments/1")

comment = json.loads(res.content)

#print (comment)

#requisitando post de um ID
post = requests.get("http://jsonplaceholder.typicode.com/posts/%d" % comment['postId'])

post = json.loads(post.content)

#print (post)

#POST - inserindo dados
dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
response = requests.post("http://jsonplaceholder.typicode.com/comments/", data = dados)

#print (response.status_code)

comment = json.loads(response.content)

#print (comment["id"])

#PUT - alterando dados
dados = data={'name': "Lucas"};
response = requests.put("http://jsonplaceholder.typicode.com/comments/%d" % comment['id'], data = dados)

new = requests.get("http://jsonplaceholder.typicode.com/comments/%d" % comment['id'])

comment = json.loads(new.content)
print (response)