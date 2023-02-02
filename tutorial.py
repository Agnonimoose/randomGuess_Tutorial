
#######
## 1 ##
#######
"""
Start the EC2 incidence called flaskAPI, and copy the ip or DNS. You
will use this ip or DNS for both connections from your python script
and also to use to connect on your ssh client.

Go to the security groups of the EC2 and make sure that you are able
to connect to the EC2 with both your python script and the SSH client.
You will need to allow your IP range in the inbound rules here.

Connect to the EC2 once it is booted up, and open the .py script. Study
the code, and find the 2 enpoints for guessing the numbers. There should 
be a random guess and a logical guess endpoint. Not down these endpoints.

"""



#######
## 2 ##
#######
"""
Do imports to are capable of connecting to the EC2, and doing multitasking
"""


#######
## 3 ##
#######
"""Create a base class that can call an endpoint on the EC2 -> we will use this
later on to call the enpoints, so make it univeral
"""
class bassCaller:
    def __init__(self):
        """initiate some stuff here"""
        pass
    
    def callEndPoint(self):
        """call the endpoint here"""
        pass
    
    def decodeReturnResult(self):
        """decode the return"""
        pass


#######
## 4 ##
#######
"""
Create 2 objecta to call the two endpoints
"""

class callEndpointClass1(INHERIT HERE):
       def __init__(self):
            """Inherit and init the class here"""
            pass
        
        def callSpecificEndpoint(self):
            """call an enpoint"""
            pass
        
        def checkResult(self):
            """check the result from the endpoint"""
            pass


class callEndpointClass2(INHERIT HERE):
       def __init__(self):
            """Inherit and init the class here"""
            pass
        
        def callSpecificEndpoint(self):
            """call an enpoint"""
            pass
        
        def checkResult(self):
            """check the result from the endpoint"""
            pass

#######
## 5 ##
#######
"""
create multitasking funcs that can create 8 objects of each at once, and
call them untill you get the correct result. Time each object to see how
long each one takes and record the time taken.
"""

