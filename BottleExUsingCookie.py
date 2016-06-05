import bottle

@bottle.route('/')
def homePage():
    Arr=['One','Two','Three']
    return bottle.template('controller.tpl',{'username':"Test",'Arr':Arr})

@bottle.post('/Selection')
def getSelection():    
    thing=bottle.request.forms.get("thing")
    if (thing== None or thing == ""):
        thing="No thing Selected"
    
    bottle.response.set_cookie("thing",thing)
    bottle.redirect('/showThing')
    
@bottle.route('/showThing')
def setShowThing():
    thing=bottle.request.get_cookie("thing")
    
    return bottle.template('thing.tpl',{'thing':thing})
    
bottle.debug(True)
bottle.run(host='localhost',port=8080)
