class VehicleBase:

    def going_to_crash(self):
        raise NotImplementedError

    def dont_crash(self):
        raise NotImplementedError


def prevent_vehicle_from_crashing(vehicle: VehicleBase):
    if vehicle.going_to_crash():
        vehicle.dont_crash()