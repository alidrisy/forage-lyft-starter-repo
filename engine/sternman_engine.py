from service_able import Serviceable


class SternmanEngine(Serviceable):
    """SternmanEngine model to create a SternmanEngine model and detremain if the Engin need service"""
    def __init__(self, warning_light_is_on):
        """Initilaize data and attrbutes"""
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        """Return True if the engin need service and False other waies"""
        if self.warning_light_is_on:
            return True
        else:
            return False
