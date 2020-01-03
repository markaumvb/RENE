# -*- coding: cp1252 -*-
import urllib3
import requests
import json
import time
from requests.auth import HTTPBasicAuth
import conecta
import sys


GH_USER = "*********"#your github username
GH_PASSWD = "*******"#your github passwd

def get_json(url):
   resp = requests.get(url, auth=HTTPBasicAuth(GH_USER, GH_PASSWD)) 
   json_objs = resp.json()
   return json_objs

def update_pr():

   conecta.c.execute("select owner, nome_projeto, number_pr, id from pr where (commits is null) order by id")
   x = 0
   #try:  
   for linha in conecta.c.fetchall():
      url = 'https://api.github.com/repos/'+linha[0]+'/'+linha[1]+'/pulls/'+linha[2]
   
      #print(url)

      json_objs = get_json(url)
      try:
         codigo_pr = linha[3]
         qtde_commits = json_objs['commits']
         qtde_additions = json_objs['additions']
         qtde_deletions = json_objs['deletions']
         qtde_changed_files = json_objs['changed_files']
         author_association = json_objs['author_association']
         x=x+1

         conecta.c.execute ("update pr set commits = '%d', additions = '%d', deletions = '%d', changed_files = '%d', author_association = '%s' where id = '%s'" %(qtde_commits, qtde_additions,qtde_deletions, qtde_changed_files, author_association, codigo_pr))
         conecta.cnx.commit()
      except:
         print(url)   
      print("Qty executed: " + str(x))
      print(codigo_pr)
   except Exception as e:
      print('error')
      


