import math

# Original coordinates
x = 1.0
y = 0.0

# Rotation angle in radians
theta = math.pi / 4  # 45 degrees

# Precompute cosine and sine of the angle
ca = math.cos(theta)
sa = math.sin(theta)

# Apply rotation
new_x = x * ca - y * sa
new_y = x * sa + y * ca

print(f"Original coordinates: ({x}, {y})")
print(f"New coordinates after rotation: ({new_x}, {new_y})")
