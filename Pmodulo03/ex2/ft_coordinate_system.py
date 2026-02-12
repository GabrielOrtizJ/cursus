#!/usr/bin/env python3

import sys
import math

def calculate_distance(p1: tuple, p2: tuple ) -> float :
    """
    Calculate Euclidean distance between two 3D points.
    Returns:
    Distance between p1 and p2 as float
    """
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2     
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    try:
        start = (0, 0, 0)
        if len(sys.argv) == 1:
            #faltan argumentos 
        elif len(sys.argv) == 2:
            #hacer split
            #haver ecuacion
        elif len(sys.argv) == 3:
            #algo falla
        elif len(sys.argv) == 4:
            #pasar argummentos a una tupla 
            #haver ecuacion
        else:
            #aqui no deberia entrar pero vamos a gestionarlo
    except ValueError as error:
        print(f"Error: {error}")