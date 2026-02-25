import math

def angleDifference(angle1, angle2):
    """Calculate the shortest distance between two angles in radians."""
    diff = (angle1 - angle2 + math.pi) % (2 * math.pi) - math.pi
    return diff if diff > -math.pi else diff + 2 * math.pi

def stepTowardsCircular(current, target, stepSize):
    """Step an angle towards a target angle by a specific step size."""
    diff = angleDifference(target, current)
    if abs(diff) < stepSize:
        return target
    else:
        return current + (stepSize if diff > 0 else -stepSize)

def wrapAngle(angle):
    """Wrap an angle to be within -pi and pi."""
    two_pi = 2 * math.pi
    angle %= two_pi
    if angle > math.pi:
        angle -= two_pi
    return angle