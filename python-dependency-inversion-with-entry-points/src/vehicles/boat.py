from core_logic.vehicle_crash_prevention import VehicleBase

class Boat(VehicleBase):
    def going_to_crash(self):
        # Check Drone's state to see if a crash is immanent
        print("BOAT - I'm gonna crash")
        return True

    def dont_crash(self):
        # take Drone-specific actions to avoid a crash
        self.personal_method_not_included_on_base()
        print("BOAT - I will not crash anymore")
        
    def personal_method_not_included_on_base(self):
        print("BOAT - this is a personal method that my base doesnt have to know about... I'm being called from the dont_crash function")