import random

import cv2
import numpy as np

from figures.Figure import Figure


class Semicircle(Figure):
    label = 5

    def generate(self):
        self.init_random()

        random_angle = random.choice([0, 90, 180, 270])

        cv2.ellipse(self.img, self.xy, (self.radius, self.radius), random_angle, 180, 360, self.color, -1)

        new_x = int(self.xy[0] + (0.5 * self.radius * np.sin(np.radians(random_angle))))
        new_y = int(self.xy[1] - (0.5 * self.radius * np.cos(np.radians(random_angle))))

        new_w = int(self.radius * np.cos(np.radians(random_angle)) + self.radius / 2 * np.sin(np.radians(random_angle)))
        new_h = int(self.radius * np.sin(np.radians(random_angle)) + self.radius / 2 * np.cos(np.radians(random_angle)))

        self.output = f"{self.label} {new_x / self.width} {new_y / self.width} {new_w / self.width} {new_h / self.width}"


if __name__ == "__main__":
    f = Semicircle()
    f.generate()
    cv2.imshow("test", f.img)
    cv2.waitKey(10000)
