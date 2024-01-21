from service_able import Serviceable


class Car(Serviceable):
    """Car model to create a Car model and detremain if the car need service"""
    def __init__(self, engine, battery, tires):
        """Initilaize data and attrbutes"""
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        """Return True if the car need service and False other waies"""
        if self.battery.needs_service() or self.engine.needs_service() or self.tires.needs_service():
            return True
        return False
