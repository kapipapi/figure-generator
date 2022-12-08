import sys
import cv2
import uuid
import argparse
import numpy as np
from os import path
from PIL import Image


parser = argparse.ArgumentParser(description='Generate figures + labels for YOLOv5.')
parser.add_argument('destination')
parser.add_argument('count', type=int)


class Figure:
    def __init__(self):
        self.img = np.zeros((640, 640, 3), np.uint8)

        bg_c = np.random.randint(255, size=3)
        self.bg_c = (int(bg_c[0]), int(bg_c[1]), int(bg_c[2])) 
        cv2.rectangle(self.img, (0,0), (640, 640), self.bg_c, -1)

        self.r = np.random.randint(640/2, size=1)[0]
        self.xy = np.random.randint(self.r, 640-self.r, size=2)
        c = np.random.randint(255, size=3)
        self.c = (int(c[0]), int(c[1]), int(c[2]))

    def save(self, destination):
        id = str(uuid.uuid1())

        im = Image.fromarray(self.img)

        im.save(path.join(destination, id + '.png'), quality=100, format='png')

        with open(path.join(destination, id + '.txt'), 'w') as f:
            f.write(self.output)
            f.close()

    def get_shape_coordinates(self, number_of_vertices, angle_rotation=0):
        coordinates = []
        for vertex in range(number_of_vertices):
            coordinates.append(
                (
                    self.r * np.cos(2 * np.pi * vertex / number_of_vertices) + self.xy[0],
                    self.r * np.sin(2 * np.pi * vertex / number_of_vertices) + self.xy[1]
                )
            )

        r_coordinates = []
        for item in coordinates:
            r_coordinates.append(
                (
                    (item[0] - self.xy[0]) * np.cos(angle_rotation) -
                    (item[1] - self.xy[1]) * np.sin(angle_rotation) + self.xy[0],

                    (item[0] - self.xy[0]) * np.sin(angle_rotation) +
                    (item[1] - self.xy[1]) * np.cos(angle_rotation) + self.xy[1]
                )
            )

        r_coordinates = [ (int(item[0]), int(item[1])) for item in r_coordinates ]

        return r_coordinates


class Circle(Figure):
    label = 0

    def __init__(self):
        super().__init__()

        cv2.circle(self.img, self.xy, self.r, self.c, -1)
        
        self.output = f"{self.label} {self.xy[0]/640} {self.xy[1]/640} {2*self.r/640} {2*self.r/640}"


class Triangle(Figure):
    label = 1

    def __init__(self):
        super().__init__()

        coords = np.array(self.get_shape_coordinates(3, np.random.randint(360, size=1)[0]))

        cv2.drawContours(self.img, [coords], 0, self.c, -1)

        x,y,w,h = cv2.boundingRect(coords)

        self.output = f"{self.label} {(x + w/2)/640} {(y + h/2)/640} {(w)/640} {(h)/640}"


class Square(Figure):
    label = 2

    def __init__(self):
        super().__init__()

        coords = np.array(self.get_shape_coordinates(4, np.random.randint(360, size=1)[0]))

        cv2.drawContours(self.img, [coords], 0, self.c, -1)

        x,y,w,h = cv2.boundingRect(coords)

        self.output = f"{self.label} {(x + w/2)/640} {(y + h/2)/640} {(w)/640} {(h)/640}"


class Pentagon(Figure):
    label = 3

    def __init__(self):
        super().__init__()

        coords = np.array(self.get_shape_coordinates(5, np.random.randint(360, size=1)[0]))

        cv2.drawContours(self.img, [coords], 0, self.c, -1)

        x,y,w,h = cv2.boundingRect(coords)

        self.output = f"{self.label} {(x + w/2)/640} {(y + h/2)/640} {(w)/640} {(h)/640}"


class Hexagon(Figure):
    label = 4

    def __init__(self):
        super().__init__()

        coords = np.array(self.get_shape_coordinates(6, np.random.randint(360, size=1)[0]))

        cv2.drawContours(self.img, [coords], 0, self.c, -1)

        x,y,w,h = cv2.boundingRect(coords)

        self.output = f"{self.label} {(x + w/2)/640} {(y + h/2)/640} {(w)/640} {(h)/640}"



if __name__ == "__main__":
    args = parser.parse_args()
    print(args.destination)
    print(args.count)

    for i in range(args.count):
        c= Circle()
        c.save(args.destination)
        
        t= Triangle()
        t.save(args.destination)
        
        s= Square()
        s.save(args.destination)

        p= Pentagon()
        p.save(args.destination)

        h= Hexagon()
        h.save(args.destination)