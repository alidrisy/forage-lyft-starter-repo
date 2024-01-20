from service_able import Serviceable


class WilloughbyEngine(Serviceable):
    """WilloughbyEngine model to create a WilloughbyEngine model and detremain if the Engin need service"""
    def __init__(self, current_mileage, last_service_mileage):
        """Initilaize data and attrbutes"""
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Return True if the engin need service and False other waies"""
        return self.current_mileage - self.last_service_mileage > 60000
