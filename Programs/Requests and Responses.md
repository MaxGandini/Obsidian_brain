### API Request:

It is initiated by the client, often a web browser, mobile app or any service.

- [[HTTP]] Method:
	GET: retrieve data
	POST: send data 
	PUT: Update data
	DELETE: Remove a resource
	PATCH: Update partially

- URL (Uniform Resource Locator):
	The endpoint or location of the server which the request is intraccting with.

- Header: 
	Metadata sent with the request. It can include authentication tokens.

- Body:
	Some requests like POST, PUT and PATCH send data to the server, and this is typically formated in JSON or XML. 

- Query parameters:
	```https://api.example.com/users?age=25&name=john```
	These are often used to filter, sort or paginate results.

```
GET /users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
Content-Type: application/json
```
### API Response:

- 200 OK : Succes
- 201 Created: New resource created
- 400 Bad Request: The server could not process the request due to client error
- 401 Unauthorized.
- 404 Not Found
- 500 Internal server error

The response generally includes headers and body too, and follows similar rules to the requests.

```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "id": 123,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

