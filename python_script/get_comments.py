# -*- coding: cp1252 -*-
import urllib3
import requests
import json
import time
from requests.auth import HTTPBasicAuth
import conecta_remoto
import conecta
import sys
import re #emojis

### dados dos usuários casuais
GH_USER = "******"#your github username
GH_PASSWD = "*********"#your github passwd

def get_json(url):
   #headers = {'Accept': 'application/vnd.github.v3.star+json'}
   resp = requests.get(url, auth=HTTPBasicAuth(GH_USER, GH_PASSWD)) 
   json_objs = resp.json()
   return json_objs

def get_comments():
   conecta_remoto.c.execute("SELECT owner, nome_projeto, number_pr, id from pr where merge = 'unmerged' order by 4 asc")
   
   for linha in conecta_remoto.c.fetchall():
      x = 1
      url = 'https://api.github.com/repos/'+linha[0]+'/'+linha[1]+'/issues/'+linha[2]+'/comments?page='+str(x)+'&per_page=100&order=asc'
      json_objs = get_json(url)
   #try:
      for PR in json_objs:
         usuario = str(PR['user']['login'])
         projeto = linha[1]
         owner = linha[0]
         criado = str(PR['created_at'])
         numero_pr =linha[2]
         author_association = PR['author_association']
         corpo= PR['body']
         corpo=corpo.replace("'", "")
         corpo = corpo.replace("\\","")
         id_pr = int(linha[3])
         
         conecta_remoto.c.execute ("insert into comentarios_pr (usuario, projeto, owner, body, dt_comentario, number_pr, author_association, id_pr) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)"%(usuario, projeto, owner, corpo, criado, numero_pr, author_association, id_pr))
         conecta_remoto.cnx.commit()
      x = x + 1
      url = 'https://api.github.com/repos/'+linha[0]+'/'+linha[1]+'/issues/'+linha[2]+'/comments?page='+str(x)+'&per_page=100&order=asc'
      json_objs = get_json(url)
   #except:
      #print('erro na URL: ' + url)
