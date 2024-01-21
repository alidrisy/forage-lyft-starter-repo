from service_able import Serviceable
import datetime


class SpindlerBattery(Serviceable):
    """SpindlerBattery model to create a SpindlerBattery model and detremain if the Battery need service"""
    def __init__(self, last_service_date, current_date):
        """Initilaize data and attrbutes"""
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """Return True if the battery need service and False other waies"""
        diff = self.current_date - self.last_service_date
        if diff > datetime.timedelta(days=365 * 3):
            return True
        return False
