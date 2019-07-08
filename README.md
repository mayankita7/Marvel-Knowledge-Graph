# Marvel-Knowledge-Graph
A Knowledge Graph based on the Marvel Universe built using neo4j, Dialogflow and python. 

Contructed a graph consisting of movies, actors, directors and characters as its nodes, having relationships and properties, using 
parsehub for the wikipedia page of Marvel movies. A user can ask the same query in different forms. Therefore, it is important to do Intent
analysis of the queries. This has been done  using dialogflow.  
Using dialogflow, the intent and entity for a given query are captured and sent as parameters through webhook to the server. 
The POST request sent by dialogflow to the local server where neo4 graph is present and python application is running to receive this 
request.
ngrok is a tunneling software used for implementing the webhook. Based on the intent identified, the appropriate cql query to search from 
the knowledge graph. 
 The server will process the request and it will return the value through the port allotted by us. 
The response can be seen in both dialogue flow as well as where the local server(python application) is running.  
