print()
import math
from tkinter import FLAT

names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303'] 
radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 15.72, 6.83, 7.62, 8.10]
height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]


def main():
    for d in (names):
        name = d
        for i in (radius):
            a = float(i)
            for c in (height):
                b = float(c)
                x = compute_volume(a, b)
                y = compute_surface(a, b)
                efficiency = compute_efficency(x, y)
        print(f'{name}             {efficiency: .2f}')
        





def compute_volume(radius, height):
    volume =float(math.pi * (radius ** 2) * height)
    return volume

def compute_surface(radius, height):
    surface_area = float(2 * math.pi * (radius + height))
    return surface_area

def compute_efficency(volume, surface_area):
    storage_efficiency = float(volume /surface_area)
    return storage_efficiency

main()
