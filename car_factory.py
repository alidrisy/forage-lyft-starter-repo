from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battry = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tires_wear)
        return Car(engin, battry, tires)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battry = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tires_wear)
        return Car(engin, battry, tires)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_wear):
        engin = SternmanEngine(warning_light_on)
        battry = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tires_wear)
        return Car(engin, battry, tires)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battry = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tires_wear)
        return Car(engin, battry, tires)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battry = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tires_wear)
        return Car(engin, battry, tires)
