import json
from multipledispatch import dispatch


class config:
    def __init__(self, id, cfg):
        self.id = id
        self.cfg = cfg

    # CONSTANTS
    KEYBANDED = "bands"
    KEYCASED = "cases"
    KEYCONFIG = "config"
    KEYPARAMETERS = "parameters"

    # Attributes
    raw = ""
    JSON = {}

    # Config dictionary

    # Methods
    def getKey(self):
        return self.id + "@" + self.cfg

    def setRaw(self, value):
        if isinstance(value, bytes):
            self.raw = value.decode('utf-8')
        else:
            self.raw = value

    def getRaw(self):
        return self.raw

    @dispatch()
    def toJSON(self):
        self.JSON = json.loads(self.raw)

    @dispatch(str)
    def toJSON(self, jsonText):
        self.JSON = json.loads(jsonText)

    def getResults(self):
        pass

    # Fetch


class ruleConfig(config):
    def __init__(self, id, cfg):
        self.id = id
        self.cfg = cfg
        

    def isBanded(self):
        try:
          if self.KEYBANDED in self.JSON[self.KEYCONFIG]:
            return True
          else:
            return False
        except:
            return print(f"ERROR: No {self.KEYCONFIG} found in dictionary.")
        

    def isCased(self):
        try:
          if self.KEYCASED in self.JSON[self.KEYCONFIG]:
            return True
          else:
            return False
        except: 
            return print(f"ERROR: No {self.KEYCONFIG} found in dictionary.")


    def getResultGroups(self):
        if self.isBanded() == True:
            return (self.JSON[self.KEYCONFIG][self.KEYBANDED])
        elif self.isCased() == True:
            return (self.JSON[self.KEYCONFIG][self.KEYCASED])
        else:
            return (print("ERROR: No result groups found"))
        

    def getParameters(self):
        try:
            return (self.JSON[self.KEYCONFIG][self.KEYPARAMETERS].items())
        except:
            return ("null")
        

    def getResult(self, value):
        resultGroups = self.getResultGroups()
        for result in resultGroups:
            if "upperLimit" in result and "lowerLimit" in result:
                if value >= result["lowerLimit"] and value < result["upperLimit"]:
                    return result["subRuleRef"]
            elif "upperLimit" in result :
                if value < result["upperLimit"]:
                    return result["subRuleRef"]
            elif "lowerLimit" in result :
                if value >= result["lowerLimit"]:
                    return result["subRuleRef"]
        return print("Unable to determine rule result")
