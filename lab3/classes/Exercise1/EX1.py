class strclass:
    def __init__(x, str=""):
        x.str=str
    def getstring(x):
        x.str=input()
    def printstring(x):
        print(x.str.upper())

string = strclass()
string.getstring()
string.printstring()