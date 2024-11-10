TCP (Transmission Control Protocol) is one of the main protocols of the TCP/IP suite. It lies between the Application and Network Layers which are used in providing reliable delivery services. Transmission Control Protocol (TCP) ensures reliable and efficient data transmission over the internet

![[TCP.png]]

[[TCP]] is known for having reliable communication:

- Before transmitting data, a connection is established between sender and receiver, called the [[handshake]] . Once connection is set up, data is transmitted

- Three-way handshake: [[Requests and Responses]]
	SYN: A client sends a request to start the connection.
	SYN-ACK: The server responds to acknowledge the request.
	ACK: The client confirms the connection is established. 

- Flow Control:
	[[TCP]] controls the rate at which information is transmitted. The receiver can notify the sender to slow down or speed up based on specific characteristics.

- Error Checking:
	[[TCP]] chcks for errors using [[Checksums]] . If an error is found, the affected data packets are retransmitted.

- Segmentation and Reassembly: 
	[[TCP]]breaks large chunks of data into smaller segments for easier transmission over the network.

![[segmentation.png]]

- Duplex communication:
	It allows for data to be sent and received simultaneously between sender and receiver.