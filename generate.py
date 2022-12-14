import argparse

from figures.Circle import Circle
from figures.Hexagon import Hexagon
from figures.Pentagon import Pentagon
from figures.Quarter import Quarter
from figures.Semicircle import Semicircle
from figures.Square import Square
from figures.Triangle import Triangle

parser = argparse.ArgumentParser(description='Generate figures + labels for YOLOv5.')
parser.add_argument('destination')
parser.add_argument('count', type=int)

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

    for i in range(args.count):
        for f in figures:
            f.generate()
            f.save(args.destination)
