import hashlib 
import json 
import datetime

def listhash(listofitems):
	"""
	Convert a list of data to jsonified string, and hash it 
	"""
	strdata = json.dumps(listofitems)
	return unicode(hashlib.sha256(strdata).hexdigest(),'utf-8')


def provework(inputhash, mustendwith):
	"""
	A very simple proof of work function. Sequentially augments
	an input hash until the result hash ends with correct string
	Arguments:
	    inputhash:   The starting hash value
	    mustendwith: Value string must be found to end with
	Output: 
		A hash of values including:
		  iterations: iterations required to solve for the answer
		  answer: The string which when hashed with input gets the 
		          correct "mustendwith" string. e.g. the "nonce"
		  resulthash: The resulting hash containing the "mustendwith" 
	"""	
	testvalue = str(datetime.datetime.utcnow())
	niter = 0
	while True:
		niter = niter +1 
		resulthash = listhash([inputhash, testvalue])
		if resulthash.endswith(mustendwith):
			return {'iterations': niter, 'answer': testvalue, 'resulthash': resulthash}
		else:
			testvalue = str(resulthash)



class Transaction:
    """
    A wallet-to-wallet transaction 
    Attributes:
        timestamp: A string of format YYYY-MM-DD HH24:MI:SS
        amount:    The amount (integer)
        sender:    The wallet address sending the transaction
        recipient: Wallet address receiving the transaction
    """	
    def __init__(self, sender, recipient, amount):    
        self.timestamp = str(datetime.datetime.utcnow())
        self.sender    = sender
        self.recipient = recipient
        self.amount    = amount

    def validate(self):
    	if self.timestamp is None: 
    		raise TypeError("Timestamp not defined")
    	if self.sender    is None: 
    		raise TypeError("Sender not defined")
    	if self.recipient is None: 
    		raise TypeError("Recipient not defined")
    	if self.amount    is None: 
    		raise TypeError("Amount not defined")  
    	if self.amount != int(self.amount):
    		raise ValueError("Amount must be an integer")  		
    	return 1

    def signature(self):
    	self.validate()
    	return listhash([self.timestamp, self.sender, self.recipient, self.amount])

    def display(self):
    	print "Timestamp: " + str(self.timestamp)
    	print "Sender:    " + str(self.sender)
    	print "Recipient: " + str(self.recipient)
    	print "Amount:    " + str(self.amount)
    	print "Hash:      " + str(self.signature())


hh = Transaction(sender = 'x', recipient = 'y', amount=10)
hh.display()

print provework(inputhash='asdfkjh', mustendwith = '0000')
