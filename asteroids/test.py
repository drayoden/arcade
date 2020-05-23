import math

# testing some trig functions...

print(f"testing atan2...")
x = 4
y = 2

print(f"x = {x}, y = {y}")

rads = math.atan2(y,x)

print(f"atan2(y/x): {rads} (rad)")

degs = math.degrees(rads)

print(f"atan2(y/x): {degs} (deg)")
