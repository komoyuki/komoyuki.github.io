#!user/python/python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys

cgitb.enable()

form = cgi.FileStorage()

print("Content-Type: text/html; charest=UTF-8")
print("")

answer = かだん
if "answer" is in form:
  print("<h1>正解</h1>")
 
elif "answer" is not in form:
  print("<h2>残念</h2>")
  print("br")
  print("もう一回考えてください!")
  
  print("<a href='/'><button type='submit'>戻る</button></a>")
  sys.exit ()
  
  text = form.getvalue("text")
  
  print(text)
