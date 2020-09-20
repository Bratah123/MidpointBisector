import math
# @author Brandon Nguyen
SHOW_MIDPOINTS = True
def power_of(x, power):
    result = 1
    for i in range(power):
        result *= x
    # just a simple function that emulates the power of values such as 2^5, probably some other library has a function like this readily avaliable
    return result

def bisect(a , b):
    return (a + b) / 2
    # gets the midpoint of two values

def set_intervals_by_value(intervals, bisected_val, function):
    # if f(x) is negative, then set the a value else set the b value
    if function < 0:
        intervals[0] = bisected_val # a
    elif function > 0:
        intervals[1] = bisected_val # b
    return intervals

def find_root(a, b, iterations):
    # Where the magic happens
    intervals = [a, b]
    print(f"\nStarting Interval Values: {intervals}\n")
    for i in range(iterations): # continue bisecting x amount of times
        a = intervals[0]
        b = intervals[1]
        midpoint = bisect(a, b)
        function = calculate_cos_problem(midpoint)
        intervals = set_intervals_by_value(intervals, midpoint, function)
        if SHOW_MIDPOINTS:
            print(f"Midpoint: {midpoint}")
            print(f"f({midpoint}) = {function}")
            print(f"Intervals: {intervals}\n")
    return intervals

def calculate_cos_problem(midpoint):
    # cos(x) - x
    function = math.cos(midpoint) - midpoint
    return function

def calculate_at_midpoint(midpoint):
    # x^5 + x^4 + x^3 + x^2 + x - 4
    x5 = power_of(midpoint, 5) # x^5
    x4 = power_of(midpoint, 4) # x^4
    x3 = power_of(midpoint, 3) # x^3
    x2 = power_of(midpoint, 2) # x^2
    x = midpoint

    return x5 + x4 + x3 + x2 + x - 4

def main():
    # provide the correct a and b values
    final_interval = find_root(1, 0, 8)
    print("Final intervals a and b", final_interval)
    print("The root of this interval:", bisect(final_interval[0], final_interval[1]))

if __name__ == "__main__":
    main()
