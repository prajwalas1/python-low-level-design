# Encapsulation: Car – Engine – Wheel
# ─────────────────────────────────────────────

# === ENTITIES ===
# Suggested: define your core classes
from enum import Enum



class EngineState(Enum):
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    OVERHEATED = "OVERHEATED"


class Car:
    def __init__(self):
        self.__engine = Engine()
        self.__wheels = [
    Wheel(32),
    Wheel(28),
    Wheel(35),
    Wheel(25)
]
        self.__speed = 0

    def start(self):
        return self.__engine.start()

    def stop(self):
        return self.__engine.stop()

    def accelerate(self,speed):
        if self.__engine.get_state() != EngineState.RUNNING:
            return False
        self.__speed = speed  
        return True

    def checkTires(self):
        under_inflated = []
        for wheel in self.__wheels:
            if wheel.is_under_inflated():
                under_inflated.append(wheel)
        return under_inflated        
              




class Engine:
    def __init__(self):
        self.__state = EngineState.IDLE

    def start(self):
        if self.__state == EngineState.RUNNING:
            return False

        if self.__state == EngineState.OVERHEATED:
            return False

        self.__state = EngineState.RUNNING
        return True        

        

    def stop(self):
        if self.__state == EngineState.IDLE:
            return False

        if self.__state == EngineState.OVERHEATED:
            return False    

        self.__state = EngineState.IDLE
        return True    

           

    def get_state(self):
        return self.__state
               

        

class Wheel:
    def __init__(self,pressure):
        self.__pressure = pressure

    def is_under_inflated(self):
        return self.__pressure < 30

    def get_pressure(self) :
        return self.__pressure
    

if __name__ == "__main__":
    car = Car()

    print("Start:", car.start())
    print("Accelerate:", car.accelerate(60))
    print("Stop:", car.stop())

    under_inflated = car.checkTires()

    print("Under-inflated tires:")
    for wheel in under_inflated:
        print(wheel.get_pressure(), "psi")

                    


       


# === RELATIONSHIPS ===
# - A has many B
# - B references C

# === DESIGN PATTERNS ===
# e.g. Strategy, Observer, Factory

# === KEY REQUIREMENTS ===
# 1. Car has a private Engine and private list of Wheels
# 2. Engine has state: IDLE, RUNNING, OVERHEATED
# 3. Car.start() — fails if engine is already running or overheated


