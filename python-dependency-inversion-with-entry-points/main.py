from importlib.metadata import entry_points
from src.core_logic.vehicle_crash_prevention import prevent_vehicle_from_crashing


vehicle_entry_points = entry_points(group="vehicles")

vehicle_classes = {
    # name is the one defined on pyproject.toml file
    # load() is the entrypoint function to load the module/plugin
    v.name: v.load() 
    for v in vehicle_entry_points 
    if v.name != "base"  # ignore the VehicleBase class
}

print(vehicle_classes)

for _, vehicle_class in vehicle_classes.items():
    print("vehicle class: ", vehicle_class)
    vehicle = vehicle_class()
    prevent_vehicle_from_crashing(vehicle)