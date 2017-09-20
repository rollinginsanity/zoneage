from zoneage import Zoneage
import json
from zoneage.models import Zone


zoneage = Zoneage()

zoneage.config.load_config("./config.json")

print(zoneage.config.db_file)

zoneage.init_db()

with open("zone_model_example/zones.json") as zones_json:
    zones_data = json.load(zones_json)

zones = zones_data["zones"]

for zone_data in zones:
    zone = Zone()
    zone.load_data(zone_data)
    zoneage.db.session.add(zone)
    zoneage.db.session.commit()