import math

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.
        
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT

class Rocket(Body):
    def __init__(self, x, y, mass, dmass):
        """
        Создать ракету.
        
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        mass: float
            масса ракеты и топлива
        dmass: float
            масса выбрасываемого топлива за ед. времени dt
        """
        super().__init__(x, y, 10, 10) # Вызовем конструктор предка — тела, т.к. он для ракеты актуален
        self.mass = mass
        self.dmass = dmass

    def advance(self):
        """
        По закону реактивного движения:
            v(ракеты) = m(топлива)/m(ракеты)*v(топлива) 
        Пусть наши ракеты выпускают топливо с одинаковой скоростью 150
        """
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.
        if self.mass>self.dmass:
            self.mass -= self.dmass
            self.vx+=(self.dmass/self.mass)*150 * MODEL_DT
            self.vy+=(self.dmass/self.mass)*150 * MODEL_DT

import numpy as np

b = Body(0, 0, 10, 10)
r = Rocket(0, 0, 50, 1)
k = Rocket(0, 0, 300, 2)
t = Rocket(0, 0, 2, 1)

bodies = [b, r, k, t]
# Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
# благодаря возможностям ООП будем просто работать со списком тел

for t in np.arange(0, 2, MODEL_DT): # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг
        
#matplotlib inline
from matplotlib import pyplot as pp

i = 0
for b in bodies: # для всех тел
    i+=1
    pp.plot(b.trajectory_x, b.trajectory_y, label=b.__class__.__name__+str(i)) # нарисуем их траектории
pp.legend()
pp.show()
