'''
*****************************************************************************************
*
*  ===============================================
*     Niti Vahan (NV) Theme of eYRC 2026-27
*  ===============================================
*
*  This script is intended for implementation of Task 1A of Niti Vahan (NV) Theme.
*
*  Filename:         ackermann_steering.py
*  Created:          2026
*  Last Modified:
*  Author:           e-Yantra Team
*
*  You are ONLY allowed to write your code inside the block marked
*  "ADD YOUR IMPLEMENTATION HERE". Do not change anything outside it - the
*  evaluation script relies on the rest of this file staying as it is.
*
*****************************************************************************************
'''

# Team ID:          < Team-ID >
# Author List:      < Names of the team members who worked on this file, comma separated >
# Filename:         ackermann_steering.py
# Functions:        ackermann_wheel_angles
# Global variables: < List any global variables you add, "None" if you add none >


####################### IMPORT MODULES #######################
import math
import numpy as np
##############################################################


#################### VEHICLE CONSTANTS #######################
WHEELBASE = 0.120           # L: distance between front and rear axle centrelines
TRACK_WIDTH = 0.110         # W: distance between left and right wheel centre
WHEEL_OFFSET = 0.0275       # O: distance between kingpin axis and wheel centre.
##############################################################


##############################################################
############### ADD YOUR IMPLEMENTATION HERE #################
##############################################################


def ackermann_wheel_angles(delta):
    '''
  Purpose:
    ---
    Convert a single virtual steering angle into the two real front-wheel
    angles, per the Ackermann geometry.

    Input Arguments:
    ---
    `delta` : [ float ]
        Steering angle of the virtual centred front wheel, in radians.

    Returns:
    ---
    `left_angle` : [ float ]
        Left front-wheel steering angle in radians.

    `right_angle` : [ float ]
        Right front-wheel steering angle in radians.
    '''

    # Handle the straight-ahead case separately.
    if abs(delta) < 1e-12:
        return 0.0, 0.0

    # Convert wheel track to the effective half kingpin track.
    half_kingpin_track = (TRACK_WIDTH / 2.0) - WHEEL_OFFSET

    # Find the turning radius represented by delta.
    radius = turning_radius(delta)

    # Positive delta means a left turn.
    if delta > 0:
        left_angle = wheel_angle(radius - half_kingpin_track)
        right_angle = wheel_angle(radius + half_kingpin_track)

    # Negative delta means a right turn.
    else:
        left_angle = -wheel_angle(radius + half_kingpin_track)
        right_angle = -wheel_angle(radius - half_kingpin_track)

    return left_angle, right_angle


def turning_radius(delta):
    '''
    Calculate the virtual turning radius from the steering angle.
    '''

    return WHEELBASE / math.tan(abs(delta))


def wheel_angle(radius):
    '''
    Calculate the steering angle corresponding to a wheel's turning radius.
    '''

    return math.atan(WHEELBASE / radius)

##############################################################
################ END OF YOUR IMPLEMENTATION ##################
##############################################################


#################### DO NOT EDIT BELOW THIS LINE ####################

if __name__ == "__main__":

    test_angles = np.arange(-0.35, 0.35, 0.05)

    for d in test_angles:
        left, right = ackermann_wheel_angles(d)
        print(f"delta={d}  ->  left={left}, right={right}")
