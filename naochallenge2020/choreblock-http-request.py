import urllib2
import json

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self, p):
        #self.onStopped(p) #activate the output of the box
        resp = urllib2.urlopen(p)
        content = resp.read()
        
        self.info = json.loads(content)


    def onInput_onStop(self):
    
        res = self.info["author"]
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped(res) #activate the output of the box
