import requests
import tazamaConfigHandler.config
import json


ruleConfig = tazamaConfigHandler.config.ruleConfig("006@1.0.0", "1.0.0")
ruleConfigDBPath = "http://192.168.1.222:18529/_db/Configuration/_api/document/configuration/"

# ruleConfig.setRaw(requests.get(ruleConfigDBPath + ruleConfig.getKey()).content)
raw = requests.get(ruleConfigDBPath + ruleConfig.getKey()).content.decode('utf-8')

ruleConfig.setRaw(raw)
ruleConfig.toJSON()

print(ruleConfig.getResultGroups())

print(ruleConfig.getResult(4))