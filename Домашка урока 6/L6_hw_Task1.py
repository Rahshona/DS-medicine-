from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self.__color.items():
            sleep(value)
            print(key)



my_traffic = TrafficLight(color={'\033[31mRed': 7, '\033[33mYellow': 2, '\033[32mGreen': 10})
my_traffic.running()






