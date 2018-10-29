# -*- coding: utf-8 -*-
"""
@author: Lexzander Saplan
@author: David Ibarra

EE 381 : Lab Project 2 - Part 1A
Professor Sam Jalali
"""

import numpy as np

def expection_to_safety(rooms):
    room_chosen = 0
    time = 0
    while room_chosen != 1:
        room_chosen = np.random.choice(rooms, 1, p=[1/3, 1/3, 1/3])
        if room_chosen == rooms[0]:
            print("Chose Room 1 (+2 hours)")
            time += 2
            break
        elif room_chosen == rooms[1]:
            print("Chose Room 2 (+5 hours)")
            time += 5
        elif room_chosen == rooms[2]:
            print("Chose Room 3 (+3 hours)")
            time += 3
    print("Took", time, "hours to get to safety!")


def main():
    rooms = [1, 2, 3]
    expection_to_safety(rooms)
    print("")


main()