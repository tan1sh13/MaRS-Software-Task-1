import math

def transform():
    print("Enter object coordinates (camera frame):")
    x=float(input("x_cam: "))
    y=float(input("y_cam: "))
    z=float(input("z_cam: "))
    print("\nEnter rover position (world frame):")
    rx=float(input("x: "))
    ry=float(input("y: "))
    rz=float(input("z: "))
    print("\nEnter rotation angles (in degrees):")
    ax=float(input("Rotation around X: "))
    ay=float(input("Rotation around Y: "))
    az=float(input("Rotation around Z: "))
    # Convert to radians
    ax=math.radians(ax)
    ay=math.radians(ay)
    az=math.radians(az)
    # rotation around x axis
    y1=y*math.cos(ax)-z*math.sin(ax)
    z1=y*math.sin(ax)+z*math.cos(ax)
    x1=x
    # rotation around y axis
    x2=x1*math.cos(ay)+z1*math.sin(ay)
    z2=-x1*math.sin(ay)+z1*math.cos(ay)
    y2=y1
    # rotation around z axis
    x3=x2*math.cos(az)-y2*math.sin(az)
    y3=x2*math.sin(az)+y2*math.cos(az)
    z3=z2
    #translation
    world_x=x3+rx
    world_y=y3+ry
    world_z=z3+rz
    #output
    print("\nFinal World Coordinates:")
    print("x:",world_x)
    print("y:",world_y)
    print("z:",world_z)

transform()