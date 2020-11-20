class MeterDeviceService():

    def add_device(self, meter_id, manufacturer):
        assert meter_id != None, manufacturer != None
        print("add device")

    def assign_device_to_user(self, meter_id, user_id):
        assert meter_id != None, user_id != None

        # TODO
        # check if the user_id exist
        # check if the meter_id exist
        # check if the meter_id has been assigned to someone else
        # do the "thing" if all of the above has passed
        pass

    def activate_device(self, meter_id):
        assert meter_id != None

        # TODO
        pass

    def deactivate_device(self, meter_id):
        assert meter_id != None
        pass

    def remove_device(self, meter_id, reason):
        assert meter_id != None, reason != None
        pass
