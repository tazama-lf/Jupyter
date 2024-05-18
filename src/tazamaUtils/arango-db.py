import requests
import tazamaConfigHandler.config

DATABASE_HOST = "http://192.168.1.222:18529"
DATABASE_CONFIG = "Configuration"
DATABASE_USERNAME = ""
DATABASE_PASSWORD = ""
DATABASE_COLLECTION_RULE_CONFIG = "configuration"
DATABASE_COLLECTION_TYPOLOGY_CONFIG = "typologyExpression"

ruleConfig = tazamaConfigHandler.config.ruleConfig("901@1.0.0", "1.0.0")
ruleConfigDBPath = DATABASE_HOST + "/_db/" + DATABASE_CONFIG + \
    "/_api/document/" + DATABASE_COLLECTION_RULE_CONFIG + "/"

raw = requests.get(ruleConfigDBPath + ruleConfig.getKey()
                   ).content.decode('utf-8')

ruleConfig.setRaw(raw)

print(ruleConfig.getJSON())

print(ruleConfig.getExitConditions())
print(ruleConfig.getResultGroups())

print("")
print("Get rule result:")
print(ruleConfig.getResult(2))

print(ruleConfig.getResultReason(".02"))
print(ruleConfig.getResultReason(".x00"))

typologyConfig = tazamaConfigHandler.config.typologyConfig(
    "typology-processor@1.0.0", "999@1.0.0")
typologyConfigDBPath = DATABASE_HOST + "/_db/" + DATABASE_CONFIG + \
    "/_api/document/" + DATABASE_COLLECTION_TYPOLOGY_CONFIG + "/"

raw = requests.get(typologyConfigDBPath +
                   typologyConfig.getKey()).content.decode('utf-8')

print(raw)

typologyConfig.setRaw(raw)

print(typologyConfig.getJSON())

print(typologyConfig.getKey())
print(typologyConfig.getDesc())

print(typologyConfig.getInterdictionThreshold())
print(typologyConfig.getAlertThreshold())


print("Typology weight outcomes for each rule result")
print(typologyConfig.getWeight(
    ruleConfig.formatRuleResult({"subRuleRef": ".err"})))
print(typologyConfig.getWeight(
    ruleConfig.formatRuleResult(ruleConfig.getExitConditions()[0])))
print(typologyConfig.getWeight(
    ruleConfig.formatRuleResult(ruleConfig.getResultGroups()[0])))
print(typologyConfig.getWeight(
    ruleConfig.formatRuleResult(ruleConfig.getResultGroups()[1])))
print(typologyConfig.getWeight(
    ruleConfig.formatRuleResult(ruleConfig.getResultGroups()[2])))
