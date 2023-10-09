from core_logic.vehicle_crash_prevention import VehicleBase

class Drone(VehicleBase):

    def going_to_crash(self):
        # Check Drone's state to see if a crash is immanent
        print("DRONE - I'm gonna crash")
        return True

    def dont_crash(self):
        # take Drone-specific actions to avoid a crash
        print("DRONE - I will not crash anymore")