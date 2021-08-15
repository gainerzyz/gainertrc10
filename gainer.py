from flask import Flask,request 
import tronapi 
from tronapi import Tron 
 
 
full_node = 'https://api.trongrid.io' 
solidity_node = 'https://api.trongrid.io' 
event_server = 'https://api.trongrid.io' 
 
PK = "0x6e44f5dd097fe7ef25c6c54e4a1013fd36b62791428c3652aec213ac1e17c945" 
 
tron = Tron(full_node=full_node, 
    solidity_node=solidity_node, 
    event_server=event_server) 
 
def setTronPK(pk): 
    tron.private_key = pk 
    tron.default_address = tron.address.from_private_key(pk).base58 
 
setTronPK(PK) 
 
app = Flask(name) 
 
def myfunc(add): 
  txn = tron.trx.send_token(PA, 10*100000*6, "1004018"); 
  return "ok" 
  
app.route('/') 
def getHandler(): 
    return "ok" 
 
@app.route('/post', methods = ['POST']) 
def getHandler(): 
     r = request.json 
     PA = r["address"] 
     PS = r["amount"] 
     PR = r["tokenid"] 
     txn = tron.trx.send_token(PA, 1*PS, PR); 
     return txn["transaction"]["txID"] 
     
     
    
if name == 'main': 
 app.run()
