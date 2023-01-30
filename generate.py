import argparse

from figures.Circle import Circle
from figures.Hexagon import Hexagon
from figures.Pentagon import Pentagon
from figures.Quarter import Quarter
from figures.Semicircle import Semicircle
from figures.Square import Square
from figures.Triangle import Triangle
from util import get_fragment, load_map

parser = argparse.ArgumentParser(description='Generate figures + labels for YOLOv5.')
parser.add_argument('destination', nargs='?', default="train")
parser.add_argument('count', nargs='?', type=int, default=1)

'''
    Done:
    - circle
    - triangle
    - square
    - pentagon
    - hexagon
    - semicircle
    - quarter circle

    TODO for generation:
    - rectangle
    - trapezoid
    - heptagon
    - octagon
    - star
    - cross
'''

if __name__ == "__main__":
    args = parser.parse_args()
    print(args.destination)
    print(args.count)

    figures = [
        Circle(),
        Triangle(),
        Square(),
        Pentagon(),
        Hexagon(),
        Semicircle(),
        Quarter(),
    ]

    map_img = load_map("./assets/suasorto.tif")

    for i in range(args.count):
        for f in figures:
            bg = get_fragment(map_img)
            f.generate(bg)
            f.add_reflections()
            f.merge_with_background()
            f.save(args.destination)
