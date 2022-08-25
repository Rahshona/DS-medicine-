import random

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = random.randint(10,100)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is driving'

    def stop(self):
        return f'{self.name} is stopping'

    def turn(self, direction):
        return 'to' + ' ' + direction

    def show_speed(self):
        return f'with speed {self.speed}'


class TownCar(Car):
    def __int__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'with speed {self.speed}')
        self.speed = random.randint(10,100)
        if self.speed > 60:
            return f'Speed of {self.name} is higher. Please, slow down'
        else:
            return f'This speed for {self.name} is normal'

class SportCar(Car):
    def __int__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __int__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'with speed {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher. Please, slow down'
        else:
            return f'This speed for {self.name} is normal'

class PoliceCar(Car):
    def __int__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town = TownCar(random.randint(10,100), 'yellow', 'Range', True)
print(town.name, town.color, town.show_speed, town.is_police)
print(town.go(), town.turn('right'), town.stop())
sport = SportCar(120, 'blue', 'F1', True)
print(sport.name, sport.color, sport.speed, sport.is_police)
print(sport.go(), sport.turn('left'), sport.stop())
work = WorkCar(random.randint(10,100), 'white', 'Damas', False)
print(work.name, work.color, work.show_speed, work.is_police)
print(work.go(), work.turn('straight'), work.stop())
police = PoliceCar(50, 'black', 'Piu', False)
print(police.name, police.color, police.speed, police.is_police)
print(police.go(), police.turn('left'), police.stop())

