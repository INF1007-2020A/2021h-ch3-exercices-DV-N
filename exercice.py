#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a**2.0                             #Alternative : pow(a,2) fonctionne aussi, mais a**2.0 est preferable


def average(a: float, b: float, c: float) -> float:
    moyenne = sum ([a, b, c])/len([a, b, c])   #sum(lst) / len(lst, (a + b + c)/3
    return moyenne  


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degs + (angle_mins / 60) + (angle_secs / 3600)  # convertir a,b,c en degres en premier
    radian = math.radians(angle_degs)                          # convertir deg et rad
    return radian

# Alternative qui ne fonctionne pas pcq on veut retourner une seule valeurqui combine les 3 unités input
#    deg_to_rad = (angle_degs * (math.pi/180))
#    mins_to_rad = (angle_mins * (math.pi/(60 * 180))
#    secs_to_rad = (angle_secs * (math.pi/(180 * 3600))
#    return deg_to_rad, mins_to_rad, secs_to_rad


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads) # Ex. 90.705, convertir rad to deg
    min = (degrees - math.floor(degrees)) * 60 # (90.705- 90) * 60 = 42.3, conserver les deg décimaux
    sec = (min - math.floor(min)) * 60 # 0.705*60,  conserver les decimaux de min
    return math.floor(degrees), math.floor(min), sec


def to_celsius(temperature: float) -> float:
    return (temperature - 32) * 5/9


def to_farenheit(temperature: float) -> float:
    return (temperature*1.8) + 32               #(temperature × 9/5) + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
