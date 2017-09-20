from zoneage import Zoneage
import json
from zoneage.models import Zone, Node


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


with open("zone_model_example/nodes.json") as nodes_json:
    nodes_data = json.load(nodes_json)

nodes = nodes_data["nodes"]

for node_data in nodes:
    assoc_zone = zoneage.db.session.query(Zone).filter(Zone.zone_name == node_data["node_zone"]).first()
    node_data["zone_id"] = assoc_zone.id
    node = Node()
    node.load_data(node_data)
    zoneage.db.session.add(node)
    zoneage.db.session.commit()

