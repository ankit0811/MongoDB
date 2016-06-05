import bottle

@bottle.route('/')
def home_page():
    tempArr=['One','Two','Three']
#    return bottle.template('hello_world',username="Test",arr=tempArr) #Python always sends data as a dictionary and hence this staement is equivalent to the below format
    return bottle.template('hello_world',{'username':"Test",'arr':tempArr})
    
bottle.debug(True)
bottle.run(host='localhost', port=8080)
