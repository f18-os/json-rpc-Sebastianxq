# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *
import json

def createGraph(nodeDict):
  #print(nodeDict)
  root = node(nodeDict["name"])
  #root.show()
  buildGraphRecursive(root,nodeDict["children"])
     #return root
def buildGraphRecursive(root,children):
   for child in children:
     #print(child) does indeed print out child
     #if (child["children"] != ""):
        #buildGraphRecursive(child, child["children"])
     tempChild  = node(child["name"]) #valid node is created out of this
     #root.children = node(child["name"]) #returns reference to object addy???
     #print(child) #dictionary type
     #print(root.name) #no error when grabbing fields
     print(tempChild.name)
   #root.show()

   #OPTIONS
   #1.) Recursive call to bottom and then build root from ground up
   #2.) Create 2 seperate objects and then return
   #3.) Append to a list, then output list to children
   
def getChildren(root,children):
  for child in children:
    if (child["children"] == ""):
      return node(root)
    

      
# Class providing functions for the client to use:
@service_class
class ServerServices(object):
      
  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))

  @request
  def nop(self, txt):
    print("taking in %s" (txt))
    return txt

  @request
  def incrementTree(self, o):
    print ("now incrementing tree on server side")
    #nodeData is of type dictionary
    #since dicts are data types, there must be a way to
    #grab the head, head.data, child, child.data easily
    #I would presume it'd be like iterating through a linked list or an associative array

    nodeDict = json.loads(o) #string->dictionary
    createGraph(nodeDict)

        
       
    print("increment complete, now returning serialized tree")
    return ("increment succesffuly")

  #code that I will likely not use
  #subtree method, might not use
  #def getsubtree(d, node) :
    # if nodeDict.has_key(node) :
    #   return([node] + [getsubtree(d,child) for child in d[node]])
    # else :
    #   return([node])
  #def build_tree(nodeDict):
      # create empty tree to fill
      #tree = {}
      # fill in tree starting with roots (those with no parent)
     # build_tree_recursive(tree,None, nodeDict["children"])
     # return tree
    #def build_tree_recursive(tree, parent, nodes):
      # find children
     # children  = [n for n in nodes if n.parent == parent]
      # build a subtree for each child
      #for child in children:
        # start new subtree
      #  tree[child.name] = {}
        # call recursively to build a subtree for current node
        #build_tree_recursive(tree[child.name], child, nodes)
  
  

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
