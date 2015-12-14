import math
import utils
import random
from vehicle import Vehicle

max_velocity = utils.meterToPixel(5)  # Class variable shared by all instances
min_velocity = utils.meterToPixel(4)
max_acceleration = 200
exit_probability = 0.25  # Set to other then 0 when Active flag is in play
range_of_sight = utils.meterToPixel(10)
vision_angle = math.pi/8
stop_time = 1
radius = utils.meterToPixel(0.5)


class Pedrestian(Vehicle):

    pedrestian_number = 0

    def __init__(self, road):
        super(Pedrestian, self).__init__(road, "Pedrestian")
        Pedrestian.pedrestian_number += 1

    def spawn(self):
        self.startNode=0
        self.nextNode=1
        self.RightOfPassage=1
        self.stopTimer=stop_time
        self.stopped=0
        self.velocity=max_velocity
        self.max_velocity = min_velocity + (max_velocity-min_velocity)*(0.5+0.5*random.random())
        self.vision_angle = vision_angle
        self.range_of_sight = range_of_sight
        self.min_velocity = min_velocity
        self.length = radius*2
        super(Pedrestian, self).spawn()

    def update(self, vehicles, delta_t):
        super(Pedrestian,self).update(vehicles,delta_t)

    def update_next_node(self,delta_t):
        next_pos = self.road.GetNodePosition(self.nextNode)
        if utils.calc_distance(self.position, next_pos) < self.velocity*delta_t: #We arrive at the next node
            self.nextNode=self.road.GetNextNode(self.nextNode)
            if self.nextNode == -1:
                self.active=False

    def draw(self, screen, pygame):
        pos = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(screen, (0, 0, 255), pos, int(radius))
