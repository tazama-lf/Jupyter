import json
from multipledispatch import dispatch


class config:
    def __init__(self, id, cfg):
        self.id = id
        self.cfg = cfg

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

    def getResults(self):
        try:
            return (self.JSON["config"]["bands"])
        except:
            return (self.JSON["config"]["cases"])


    def getParameters(self):
        try:
            return (self.JSON["config"]["parameters"].items())
        except:
            return ("null")
