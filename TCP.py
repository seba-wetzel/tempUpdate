import socket
import sys
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >>sys.stdout, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
           print >>sys.stdout, 'waiting for a connection'
           connection, client_address = sock.accept()
           
           try:
                   print >>sys.stdout, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
                   while True:
                               data = connection.recv(16)
                               print >>sys.stdout, 'received "%s" ' % data.rstrip('\n')
                               if data :
                                   print >>sys.stdout, 'sending data back to the client'
                                   connection.sendall("ok\n")
                                   if data == "CAGAMOS\n":
                                                                           print "llego lo que esperaba"
                               else:
                                          print >>sys.stdout, 'no more data from', client_address
                                          break

           except KeyboardInterrupt:
                                                                print >>sys.stdout, '   user close the script, closing the port '       
                                                                
                                                                break
            
           finally:
        # Clean up the connection
                          connection.close()
           
