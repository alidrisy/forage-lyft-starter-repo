from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battry = SpindlerBattery(last_service_date, current_date)
        return Car(engin, battry)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battry = SpindlerBattery(last_service_date, current_date)
        return Car(engin, battry)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engin = SternmanEngine(warning_light_on)
        battry = SpindlerBattery(last_service_date, current_date)
        return Car(engin, battry)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battry = NubbinBattery(last_service_date, current_date)
        return Car(engin, battry)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battry = NubbinBattery(last_service_date, current_date)
        return Car(engin, battry)
