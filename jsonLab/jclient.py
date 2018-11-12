# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import * #import all methods in node
import json #allows objects to be encoded through json
from json import JSONEncoder

# creates socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

#connects to server
rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

#execute in server?
#result = server.swapper('Hello World!')
#test = server.nop('Friend!')
# "!dlroW olleH"
#print(result)
#print(test)

#print(server.nop({1:[2,3]}))

#create a method in server that takes in a tree graph
#send in as server.(encodedInfo)
#on server side, there should be a decoded that's available to take
#change it to a data type there then incremenet
#but then return the same data would have to be encoded and then decoded as well

#TODOLIST FOR NOW
#2.)construct on other side to create tree
#3.)Increment Print
#graph code------------------------------------------------------------------------------
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root  = node("root", [leaf1,leaf2])

#print("tree b4 ++")
root.show();

#supposed increment remotely
server.incrementTree(root.toJson())

#print.("graph after increment")
root.show()

rpc.close() # Closes the socket 's' also
