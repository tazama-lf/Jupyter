import requests
import tazamaConfigHandler.config
import json


ruleConfig = tazamaConfigHandler.config.ruleConfig("006@1.0.0", "1.0.0")
ruleConfigDBPath = "http://localhost:18529/_db/Configuration/_api/document/configuration/"

# ruleConfig.setRaw(requests.get(ruleConfigDBPath + ruleConfig.getKey()).content)
raw = requests.get(ruleConfigDBPath + ruleConfig.getKey()).content.decode('utf-8')

ruleConfig.setRaw(raw)
ruleConfig.toJSON()

for e1 in ruleConfig.getResults():
    print(f"{e2}:")
    for e2 in ruleConfig.getResults()[e1]:
        print(f"{e2}: {ruleConfig.getResults()[e2]}")

print(ruleConfig.getParameters())

for e in ruleConfig.getParameters():
    print(f"{e}: {ruleConfig.getParameters()[e]}")
