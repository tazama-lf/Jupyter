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
        self.toJSON()

    def getRaw(self):
        return self.raw

    def getJSON(self):
        return self.JSON

    @dispatch()
    def toJSON(self):
        self.JSON = json.loads(self.raw)

    @dispatch(str)
    def toJSON(self, jsonText):
        self.JSON = json.loads(jsonText)

    # Fetch


class ruleConfig(config):
    def __init__(self, id, cfg):
        self.id = id
        self.cfg = cfg

    # CONSTANTS
    KEYBANDED = "bands"
    KEYCASED = "cases"
    KEYCONFIG = "config"
    KEYPARAMETERS = "parameters"
    EXITCONDITIONS = "exitConditions"

    def formatRuleResult(self, ruleResult):
        return {"id": self.id, "cfg": self.cfg, "subRuleRef": ruleResult["subRuleRef"]}

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

    def getExitConditions(self):
        if self.EXITCONDITIONS in self.JSON[self.KEYCONFIG]:
            return (self.JSON[self.KEYCONFIG][self.EXITCONDITIONS])
        else:
            return (print("ERROR: No exit conditions found"))

    def getParameters(self):
        try:
            return (self.JSON[self.KEYCONFIG][self.KEYPARAMETERS].items())
        except:
            return ("null")

    def getResult(self, value):
        resultGroups = self.getResultGroups()

        if self.isBanded() == True:
            if not isinstance(value, int) and not isinstance(value, float):
                return print("value is not a number")
            for result in resultGroups:
                if "upperLimit" in result and "lowerLimit" in result:
                    if value >= result["lowerLimit"] and value < result["upperLimit"]:
                        return self.formatRuleResult(result)
                elif "upperLimit" in result:
                    if value < result["upperLimit"]:
                        return self.formatRuleResult(result)
                elif "lowerLimit" in result:
                    if value >= result["lowerLimit"]:
                        return self.formatRuleResult(result)
            return print("Unable to determine rule result")
        elif self.isCased() == True:
            for result in resultGroups:
                if "value" in result:
                    if value == result["value"]:
                        return self.formatRuleResult(result)
            for result in resultGroups:
                if not "value" in result:
                    return self.formatRuleResult(result)

        return print("Unable to determine rule result")

    def getResultReason(self, subRuleRef):

        # Check exit conditions
        exitConditions = self.getExitConditions()
        for result in exitConditions:
            if subRuleRef == result["subRuleRef"]:
                return result["reason"]

        # Check result bands
        resultGroups = self.getResultGroups()
        for result in resultGroups:
            if subRuleRef == result["subRuleRef"]:
                return result["reason"]

        return print("Unable to determine rule result reason")


class typologyConfig(config):
    def __init__(self, id, cfg):
        self.id = id
        self.cfg = cfg

    # CONSTANTS
    KEYWORKFLOW = "workflow"
    KEYALERTTHRESHOLD = "alertThreshold"
    KEYINTERDICTIONTHRESHOLD = "interdictionThreshold"
    KEYRULES = "rules"
    KEYEXPRESSION = "expression"

    def getDesc(self):
        if ("desc") in self.JSON:
            return (self.JSON["desc"])
        else:
            return print("ERROR: No desc object found")

    def getInterdictionThreshold(self):
        if "workflow" in self.JSON:
            if "interdictionThreshold" in self.JSON["workflow"]:
                return (self.JSON["workflow"]["interdictionThreshold"])
            else:
                return 0
        else:
            return print("ERROR: No workflow object found")

    def getAlertThreshold(self):
        if "workflow" in self.JSON:
            if "alertThreshold" in self.JSON["workflow"]:
                return (self.JSON["workflow"]["alertThreshold"])
            else:
                return print("ERROR: No alertThreshold object found")
        else:
            return print("ERROR: No workflow object found")

    def getWeight(self, ruleResult):
        if "rules" in self.JSON:
            for rule in self.JSON["rules"]:
                if ruleResult["id"]+ruleResult["cfg"]+ruleResult["subRuleRef"] == rule["id"]+rule["cfg"]+rule["ref"]:
                    return rule["wght"]
            return print("ERROR: No ruleResult found")
        else:
            return print("ERROR: No rules object found")
