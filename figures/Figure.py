import cv2
import uuid
from PIL import Image
from os import path
import numpy as np


class Figure:
    def __init__(self):
        self.width = 640

    def init_random(self):
        self.output: str = ""
        self.img = np.zeros((self.width, self.width, 3), np.uint8)

        bg_c = np.random.randint(255, size=3)
        self.bg_c = (int(bg_c[0]), int(bg_c[1]), int(bg_c[2]))
        cv2.rectangle(self.img, (0, 0), (self.width, self.width), self.bg_c, -1)

        self.radius = np.random.randint(self.width / 2, size=1)[0]
        self.xy = np.random.randint(self.radius, self.width - self.radius, size=2)
        c = np.random.randint(255, size=3)
        self.color = (int(c[0]), int(c[1]), int(c[2]))

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
                    self.radius * np.cos(2 * np.pi * vertex / number_of_vertices) + self.xy[0],
                    self.radius * np.sin(2 * np.pi * vertex / number_of_vertices) + self.xy[1]
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

        r_coordinates = [(int(item[0]), int(item[1])) for item in r_coordinates]

        return r_coordinates
