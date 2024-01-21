from service_able import Serviceable


class  CarriganTire(Serviceable):
    """CarriganTire class to create a CarriganTire model and detremain if the tires need service"""
    def __init__(self, tires):
        """Initilaize data and attrbutes"""
        self.tires = tires

    def needs_service(self):
        """Return True if the tires need service and False other waies"""
        if 0.9 in self.tires or 1 in self.tires:
            return True
        return False
