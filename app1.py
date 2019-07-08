from py2neo import Graph, Node, Relationship
import os
uri = "bolt://localhost:7687"
user = "neo4j"
password = "monalisa7"

g = Graph(uri=uri, user=user, password=password)

# optionally clear the graph
# g.delete_all()
import os
os.system("cls")
import operator
print(len(g.nodes))
print(len(g.relationships))

# begin a transaction
tx = g.begin()

# define some nodes and relationships
a1 = Node("Movie", name="The Incredible Hulk",releaseDate="June 13,2008",Director="Louis Leterrier",BoxOffice="$ 263,427,551")
a2= Node("Movie", name="Ant-Man",releaseDate="July 17,2015",Director="Peyton Reed",BoxOffice="$ 519,311,965")
a3= Node("Movie", name="Thor",releaseDate="May 6,2011",Director="Kenneth Branagh",BoxOffice="$ 449,326,618")
a4 = Node("Movie", name="Captain America:The First Avenger",releaseDate="July 22,2011",Director="Joe Johnston",BoxOffice="$ 370,764,774")
a5= Node("Movie", name="Marvel The Avengers",releaseDate="June 13,2008",Director="Louis Leterrier",BoxOffice="$ 263,427,551")
a6 = Node("Movie", name="Thor 2",releaseDate="Nov 8,2013",Director="Alan Taylor",BoxOffice="$ 644,751,402")
a7 = Node("Movie", name="Captain America:The Winter Soldier",releaseDate="April 4,2014",Director="Russo Brothers",BoxOffice="$714,264,267")
a8 = Node("Movie", name="Guardians of the galaxy",releaseDate="August 1,2014",Director="James Gunn",BoxOffice="$ 773,328,629")
a9 = Node("Movie", name="Avengers Age of Ultron",releaseDate="May 1,2015",Director="Joss Whedon ",BoxOffice="$1,405,403,694")
a10 = Node("Movie", name="Captain America Civil War",releaseDate="May 6,2016",Director="Russo Brothers",BoxOffice="$ 1,153,304,495")
a11 = Node("Movie", name="Doctor Strange",releaseDate="November 4,2016",Director="Scott Derrikson",BoxOffice="$ 1,153,304,495")
a12 = Node("Movie", name="Guardian's of the Galaxy 2",releaseDate="May 5,2017",Director="James Gunn",BoxOffice="$ 863,756,051")
a13 = Node("Movie", name="Spider-Man Homecoming",releaseDate="July 7,2017",Director="Jon Watts",BoxOffice="$ 880,166,924")
a14 = Node("Movie", name="Thor Ragnarok",releaseDate="November 3,2017",Director="Taika Waititi",BoxOffice="$ 853,977,126")
a15 = Node("Movie", name="Black Panther",releaseDate="Feb 16,2018",Director="Ryan Coogler",BoxOffice="$ 1,346,917,161")
a16 = Node("Movie", name="Avenger's Infinity War",releaseDate="April 27,2018",Director="Russo Brothers",BoxOffice="$ 2,048,359,746")
a17 = Node("Movie", name="Captain Marvel",releaseDate="March 8,2019",Director="Kevin Feige",BoxOffice="$ 1,098,094,680")
a18 = Node("Movie", name="Ant Man The Wasp",releaseDate="July 6,2018",Director="Peyton Reed",BoxOffice="$ 622,674,139")
a19 = Node("Movie", name="Avenger's End Game",releaseDate="April 25,2019",Director="Russo Brothers",BoxOffice="$ 2,000,000,000")
a20 = Node("Movie", name="Iron Man 3",releaseDate="May 3,2013",Director="Shane Black",BoxOffice="$ 1,214,811,252")
a21 = Node("Movie", name="Iron Man",releaseDate="May 2,2008",Director="John Favreau",BoxOffice="$ 585,174,222")
a22 = Node("Movie", name="Iron Man 2",releaseDate="May 7,2008",Director="John Favreau",BoxOffice="$ 623,933,331")


b0=Node("Diretor",name="Anna Boden")
b1=Node("Diretor",name="Ryan Fleck")
b2=Node("Diretor",name="Ryan Coogler")
b3=Node("Diretor",name="Peyton Reed")
b4=Node("Diretor",name="Jon Favreau")
b5=Node("Diretor",name="Louis Leterrier")
b6=Node("Diretor",name="Kenneth Branagh")
b7=Node("Diretor",name="Joe Johnston")
b8=Node("Diretor",name="Joss Whedon")
b9=Node("Diretor",name="Shane Black")
b10=Node("Diretor",name="Alan Taylor")
b11=Node("Diretor",name="Russo Brothers")
b12=Node("Diretor",name="James Gunn")
b13=Node("Diretor",name="Scott Derrickso")
b14=Node("Diretor",name="Jon Watts")
b15=Node("Diretor",name="Taika Waititi")




c1=Node("Character",name="Hulk",realName="Bruce Banner")
c2=Node("Character",name="Hawkeye",realName="Clinton Barton")
c3=Node("Character",name="Captain Marvel",realName="Karol Danvers")
c4=Node("Character",name="Nick Fury",realName="Nicholas Joseph Fury")

c5=Node("Character",name="Gamora",realName="Gamora")
c6=Node("Character",name="Groot ",realName="Groot")

c7=Node("Character",name="Ant-Man",realName="Scott Lang")

c8=Node("Character",name="Loki",realName="Loki")

c9=Node("Character",name="Scarlet Witch",realName="Wanda Maximoff")

c10=Node("Character",name="Captain America",realName="Steve Rogers")

c11=Node("Character",name="Black Widow",realName="Natasha Romanoff")
c12=Node("Character",name="Iron Man",realName="Tonny Stark")
c13=Node("Character",name="War Machine",realName="Rhodey Rhodes")

c14=Node("Character",name="Thor",realName="Thor Odison")

c15=Node("Character",name="Dr. Strange",realName="Steve Strange")
c16=Node("Character",name="Black Panther",realName="T Challa")
c17=Node("Character",name="SpiderMan",realName="Peter Benjamin Parker")


d0=Node("Actor",name="Benedict Cumberbatch")
d0=Node("Actor",name="Don Cheadle")
d0=Node("Actor",name="Chris Hemsworth")
d0=Node("Actor",name="Paul Rudd")
d0=Node("Actor",name="Chadwick Boseman")
d0=Node("Actor",name="Tom Hiddleston")
d0=Node("Actor",name="Elizabeth Olsen")
d0=Node("Actor",name="Mark Ruffalo")
d0=Node("Actor",name="Bri Larson")
d0=Node("Actor",name="Chris Evans")
d0=Node("Actor",name="Vin Diesel")
d0=Node("Actor",name="Tom Holland")
d0=Node("Actor",name="Geremy Renner")
d0=Node("Actor",name="Robert Downey Jr.")
d0=Node("Actor",name="Scarlett Johnsson")
d0=Node("Actor",name="Samuel L.Jackson")
d0=Node("Actor",name="Zoe Saldana")










         

ab=Relationship(b0,"DIRECTED_BY",a17)
ab1=Relationship(b1,"DIRECTED_BY",a17)
ab2=Relationship(b2,"DIRECTED_BY",a15)
ab3=Relationship(b3,"DIRECTED_BY",a18)
ab4=Relationship(b3,"DIRECTED_BY",a2)
ab5=Relationship(b4,"DIRECTED_BY",a21)
ab6=Relationship(b4,"DIRECTED_BY",a22)
ab7=Relationship(b5,"DIRECTED_BY",a1)
ab8=Relationship(b6,"DIRECTED_BY",a3)
ab9=Relationship(b7,"DIRECTED_BY",a4)
ab10=Relationship(b8,"DIRECTED_BY",a5)
ab11=Relationship(b9,"DIRECTED_BY",a20)
ab12=Relationship(b10,"DIRECTED_BY",a6)
ab13=Relationship(b11,"DIRECTED_BY",a7)
ab14=Relationship(b11,"DIRECTED_BY",a10)
ab15=Relationship(b11,"DIRECTED_BY",a16)
ab16=Relationship(b11,"DIRECTED_BY",a19)
ab17=Relationship(b12,"DIRECTED_BY",a12)
ab18=Relationship(b12,"DIRECTED_BY",a8)
ab19=Relationship(b13,"DIRECTED_BY",a11)
ab20=Relationship(b14,"DIRECTED_BY",a13)
ab21=Relationship(b15,"DIRECTED_BY",a14)





cb=Relationship(a21,"SEQUEL",a22)
cb1=Relationship(a22,"SEQUEL",a20)
cb2=Relationship(a4,"SEQUEL",a7)
cb3=Relationship(a7,"SEQUEL",a10)
cb4=Relationship(a8,"SEQUEL",a12)
cb5=Relationship(a6,"SEQUEL",a14)
cb6=Relationship(a3,"SEQUEL",a6)
cb7=Relationship(a2,"SEQUEL",a18)



db1= Relationship(c1,"APPEARED_IN",a1)
db2 =Relationship(c1,"APPEARED_IN",a19)
db3=Relationship(c1,"APPEARED_IN",a9)
db4= Relationship(c1,"APPEARED_IN",a14)
db5= Relationship(c1,"APPEARED_IN",a5)
db6= Relationship(c1,"APPEARED_IN",a16)
db7= Relationship(c1,"APPEARED_IN",a3)
db8= Relationship(c1,"APPEARED_IN",a9)
db9= Relationship(c1,"APPEARED_IN",a5)
db10= Relationship(c1,"APPEARED_IN",a10)
db11= Relationship(c1,"APPEARED_IN",a19)
db12= Relationship(c1,"APPEARED_IN",a19)
db13= Relationship(c1,"APPEARED_IN",a17)
db14= Relationship(c1,"APPEARED_IN",a4)
db15= Relationship(c1,"APPEARED_IN",a1)




#ab = Relationship(a, "KNOWS", b)

# create the nodes and relationships


tx.create(a1)
tx.create(a2)
tx.create(a3)
tx.create(a4)
tx.create(a5)
tx.create(a6)
tx.create(a7)
tx.create(a8)
tx.create(a9)
tx.create(a10)
tx.create(a11)
tx.create(a12)
tx.create(a13)
tx.create(a14)
tx.create(a15)
tx.create(a16)
tx.create(a17)
tx.create(a18)
tx.create(a19)
tx.create(a20)
tx.create(a21)
tx.create(a22)


tx.create(b0)
tx.create(b1)
tx.create(b2)
tx.create(b3)
tx.create(b4)
tx.create(b5)
tx.create(b6)
tx.create(b7)
tx.create(b8)
tx.create(b9)

tx.create(ab)
tx.create(ab1)
tx.create(ab2)
tx.create(ab3)
tx.create(ab4)
tx.create(ab5)
tx.create(ab6)
tx.create(ab7)
tx.create(ab8)
tx.create(ab9)
tx.create(ab10)
tx.create(ab11)
tx.create(ab12)
tx.create(ab13)
tx.create(ab14)
tx.create(ab15)
tx.create(ab16)
tx.create(ab17)
tx.create(ab18)
tx.create(ab19)
tx.create(ab20)
tx.create(ab21)



tx.create(cb)
tx.create(cb1)
tx.create(cb2)
tx.create(cb3)
tx.create(cb4)
tx.create(cb5)
tx.create(cb6)
tx.create(cb7)







tx.create(db1)
tx.create(db2)
tx.create(db3)
tx.create(db4)
tx.create(db5)
tx.create(db6)
tx.create(db7)


# commit the transaction
tx.commit()

#print(g.exists(ab))
print(len(g.nodes))
print(len(g.relationships))






























#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "getd":
    
      result = req.get("result")
      parameters = result.get("parameters")
      zone = parameters.get("Movie")

      ans=(g.run("MATCH(a:Movie)-[:DIRECTED_BY]-(b) WHERE a.name= {x} RETURN b.name ",x=zone).data())
   
      print(ans)
      speech = "The Director of " + zone + " is " + str(ans)
      print("Response:")
      #print(speech)
      return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "KG_Marvel"
             }
    elif  req.get("result").get("action") == "getboxoffice":
    

       result = req.get("result")
       parameters = result.get("parameters")
       zone = parameters.get("Movie")

    
  
       ans=(g.run("MATCH(a:Movie) WHERE a.name= {x} RETURN a.BoxOffice as ANSWER ",x=zone).data())
       print(ans)
       speech = "Box Office Collection of " + zone + " is " + str(ans)
       print("Response:")

    elif  req.get("result").get("action") == "getm":
    

       result = req.get("result")
       parameters = result.get("parameters")
       zone = parameters.get("Director")

    
  
       ans=(g.run("MATCH(a:Movie)-[:DIRECTED_BY]-(b) WHERE b.name= {x} RETURN a.name as ANSWER ",x=zone).data())
       print(ans)
       speech = "Movies directed by  " + zone + " are " + str(ans)
       print("Response:")
    #print(speech)
       return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "KG_Marvel"


              }
    
    

if __name__ == '__main__':
    port = int(os.getenv('PORT',80))
    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
