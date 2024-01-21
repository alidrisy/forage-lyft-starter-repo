from service_able import Serviceable


class  OctoprimeTire(Serviceable):
    """OctoprimeTire class to create a OctoprimeTire model and detremain if the tires need service"""
    def __init__(self, tires):
        """Initilaize data and attrbutes"""
        self.tires = tires

    def needs_service(self):
        """Return True if the tires need service and False other waies"""
        sum = 0
        for i in self.tires:
            sum += i

        if sum >= 3:
            return True
        return False
