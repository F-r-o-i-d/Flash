class parser:
    def __init__(self, arg):
        self.arg = arg
    def GetValueOf(self, filter):
        result = None
        for x in range(len(self.arg)):
            if str(self.arg[x]).lower() == str(filter).lower():
                result = str(self.arg[x+1])
                break
        return result
    def IfExist(self, filter):
        result = False
        for x in range(len(self.arg)):
            if str(self.arg[x]).lower() == str(filter).lower():
                return True
        return False

