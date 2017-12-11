def make_light_prob(distance):
    """
    distance is distance from light, in m
    returns probability that driver can make the light
    assumes driver going 100 km/h (250 / 9 m/s)
    """
    if distance <= 1250 / 9:
        return 1
    return .99 * make_light_prob(distance - 250 / 9)
#


# def make_light_prob(distance, speed):
#     """
#     distance is distance from light, in m
#     speed is initial speed, in m/s
#     returns probability that driver can make the light
#     assumes acceleration at constant 2 m/s/s
#     """
#     time_to_fullspeed = (250 / 9 - speed) / 2
#     if time_to_fullspeed >= 5:
#         if distance <= 5 * speed + 25:
#             return 1
#         return .99 * make_light_prob(distance - (speed + 1), speed + 2)
#     if distance <= (5 - time_to_fullspeed) * 250 / 9 + time_to_fullspeed * speed + .5 * (250 / 9 - speed) * time_to_fullspeed:
#         return 1
#     return .99 * make_light_prob(distance - (speed + 1), min(speed + 2, 100))


def dist_to_stop(speed):
    """
    speed is initial speed of car, in m/s
    returns diff b/w car's initial position and position after stopping, in m
    assumes constant deceleration at 2 m/s/s
    """
    return speed ** 2 / 4


def time_to_point(distance):
    """
    distance is distance b/w car and other point, in m
    returns minimum time to reach light from complete stop, in s
    assumes constant acceleration at 2 m/s/s
    """
    if distance <= (125 / 9) ** 2:
        return distance ** .5
    return distance * 9 / 250 + 125 / 18