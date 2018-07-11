import maya.cmds as cmds

class sanchez(object):
    def __init__(self, name, morty):
	    self.name = name
	    self.morty = morty 
    def wubalubadubdub(self):
        print("wubalubadubdub")
class rick(sanchez):
    def __init__(self, dimension, name, morty):
        super(rick, self).__init__(name, morty)
        self.dimension = dimension
    
    #def catchphrase(self):
        #super(rick, self).wubalubadubdub()


tinyrick = rick(dimension = "c137", name = "tinyRick", morty = "burlapsackofturds")

print(tinyrick.name)
print(tinyrick.dimension)
print(tinyrick.morty)
tinyrick.wubalubadubdub()
#tinyrick.catchphrase()