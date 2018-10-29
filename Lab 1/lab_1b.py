# -*- coding: utf-8 -*-
"""
@author: Lexzander Saplan
@author: David Ibarra

EE 381 : Project 1 - Lab 1B
"""
import random
import matplotlib.pyplot as plt


# Part 1A
def p_2r_1g(n, boxes):
    total_2r_1g = 0
    for probability_test in range(n):
        # Choose Random Box
        random_box = random.choice(list(boxes))
        # Gets Random Ball List (Based on random box)
        box_list = boxes[random_box]

        # Reset red and green count
        # Set Red Count = 0 , Set Green Count = 0
        red_count = green_count = 0

        # Pick a ball 3 times (3 balls)
        for pick_ball in range(3):
            # Pick a random ball from box set
            random_ball = random.choice(box_list)

            # Check if ball is red
            # If True, increment red_count
            if random_ball == "R":
                red_count += 1

            # Check if ball is green
            # If True, increment green_count
            elif random_ball == "G":
                green_count += 1

        # Check if 2 red balls and 1 green ball was chosen
        # If True, increment count_2red1green
        if red_count == 2 and green_count == 1:
            total_2r_1g += 1

    # Fixes divide by zero error (just in case)
    if n == 0:
            return 0
    # Converts probability into percentage and returns the value
    return total_2r_1g / n * 100

# Part 1B
def p_box1_3g(n, boxes):
    # Keep count of number of time we got box 1 or box 2
    box1_count = box2_count = 0

    for probability_test in range(n):
        # Choose Random Box
        random_box = random.choice(list(boxes))
        # Gets Random Box List (Based on random box)
        box_list = boxes[random_box]

        # Reset red and green count
        # Set Red Count = 0 , Set Green Count = 0
        green_count = 0

        # Pick a ball 3 times (3 balls)
        for pick_ball in range(3):
            # Pick a random ball from box set
            random_ball = random.choice(box_list)

            # Check if ball is green
            # If True, increment green_count
            if random_ball == "G":
                green_count += 1

        # Increment count of specific box when we get 3 green
        if random_box == "Box 1" and green_count == 3:
            box1_count += 1
        elif random_box == "Box 2" and green_count == 3:
            box2_count += 1

    # Fixes divide by zero error (just in case)
    if (box1_count + box2_count == 0):
        return 0

    # Converts probability into percentage and returns the value
    return (box1_count / (box1_count + box2_count)) * 100

# Part 2A
def check_a_error(n, boxes):
    less_error = False
    for x in range(n):
        part_a = p_2r_1g(x, boxes)
        if (20.681 <= part_a <= 20.691):
            print("\tAverage gives an error LESS than 0.005%", "at %.3f" % (part_a), "%\n")
            less_error = True
            break
    if less_error == False:
            print("\tAverage gives MORE than 0.005% error for this instance\n")

# Part 3A
def plot_a(trials, boxes):
    
    for x in trials:
        plot_2r_1g = p_2r_1g(x, boxes)
        plt.scatter(x, plot_2r_1g)
        plt.annotate("%.3f" % plot_2r_1g, xy=(x, plot_2r_1g))        
    plt.show()


# Part 2B  
def check_b_error(n, boxes):
    less_error = False
    for x in range(n):
        part_b = p_box1_3g(x, boxes)
        if (64.411 <= part_b <= 64.421):
            print("\tAverage gives an error LESS than 0.005%", "at %.3f" % (part_b), "%\n")
            less_error = True
            break
    if less_error == False:
            print("\tAverage gives MORE than 0.005% error for this instance\n")

# Part 3B
def plot_b(trials, boxes):
    for x in trials:
        plot_box1_3g = p_box1_3g(x, boxes)
        plt.scatter(x, plot_box1_3g)
        plt.annotate("%.3f" % plot_box1_3g, xy=(x, plot_box1_3g))
    plt.show()


def main():
    # Data Structures holding boxes and balls
    boxes = {"Box 1": ["R", "G", "G", "G"],
             "Box 2": ["R", "R", "R", "R", "R", "G", "G", "G", "G", "G", "G", "G", "G"]}

    # Amount of simulations
    n = 1000

    # Loop 4 times to get 10,000 -> 100,000 -> 1,000,000
    for x in range(4):
        print("Running", n, "Simulations...")
        print("\tAverage of P(2R ^ 1G) was %.3f" % (p_2r_1g(n, boxes)), "%")
        check_a_error(n, boxes)
        print("\tAverage of P(Box 1 | 3G) was %.3f" % (p_box1_3g(n, boxes)), "%")
        check_b_error(n, boxes)

        # Exponentially increases...starts at 1000, then 10,000, then 100,000, finally 1,000,000
        n *= 10
    
    # Trials to be tested
    trials = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    plot_a(trials, boxes)
    plot_b(trials, boxes)
    
    
main()
