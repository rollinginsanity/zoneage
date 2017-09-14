from zoneage import Zoneage


zoneage = Zoneage()

zoneage.config.load_config("./config.json")

print(zoneage.config.db_file)