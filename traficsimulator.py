#!/usr/bin/env python2
import sys
import pygame
from road import Road
from car import Car
from bus import Bus
from busroad import BusRoad
import busroad

BLACK = (0, 0, 0)


class TraficSimulator():


    def __init__(self, map_file,bus_map_file):
        pygame.init()
        size = 620, 540

        self.screen = pygame.display.set_mode(size)
        self.time_interval = 0.016
        self.road = Road(map_file)
        self.car_list = []
        self.bus_list = []
        self.busroad_list=busroad.LoadNodesFromFile(bus_map_file)
        for x in range(0, len(self.busroad_list)):
            self.bus_list.append(Bus(self.busroad_list[x]))

    def start_simulation(self):
        while 1:
            if Car.car_number < 50:
                self.car_list.append(Car(self.road))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for car in self.car_list:
                car.update(self.car_list, self.time_interval)
            for bus in self.bus_list:
                bus.update(self.bus_list, self.time_interval)
            self.draw()
            pygame.time.wait(int(self.time_interval * 1000))

    def draw(self):
        self.screen.fill(BLACK)
        self.road.Draw(self.screen, pygame)
        for busroad in self.busroad_list:
            busroad.Draw(self.screen,pygame)
        for car in self.car_list:
            car.draw(self.screen, pygame)
        for bus in self.bus_list:
            bus.draw(self.screen,pygame)
        pygame.display.flip()


if __name__ == '__main__':
    ts = TraficSimulator("map.data","busmap.data")
    ts.start_simulation()
