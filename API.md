An API is an Application Programming Interface. It's a set of protocols, tools and definitions that allow different software apps to communicate with each other. 

![[API.png]]

It defines how requests and responses should be made between systems, what data should be expected and how different components should interact.

Some characteristics:

- [[Endpoints]]: an API exposes certain endpoints that represent different functions or services. Typically, each endpoint corresponds to a specific resource like databases or services.

- [[Requests and Responses]]: 
	A requests consists in a program sending a signal to an [[API]], accessing to an endpoint. This request can be retrieve, send or manipulate data.
	A response, is done after processing the request. The [[API]] sends a signal back typically in a standard format (JSON, XML?). It contains the requested data or an acknowledgement of the action taken.

- [[Authentication and Authorization]]:
	Many APIs require a form of identification, such as [[API KEYS]], [[OAuth tokens]], or usernames/passwords. 

- [[Methods]]: APIs often follow standard [[HTTP]] methods:
	GET: Retrieve data from server
	POST: Submit data to server
	PUT: Update existing data on the server
	DELETE: Remove data on from the sv.

A very important protocol is [[TCP]] , Transmission Control Protocol. As it is one of the core protocols in the Internet protocol IP suite. This is why is is called TCP/IP model.
