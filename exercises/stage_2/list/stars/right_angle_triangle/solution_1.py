def right_angle_triangle(level):
  for i in range(0, level, 1):
    stars = '*'
    for j in range(0, i, 1):
      stars += '*'
    print(stars)


right_angle_triangle(5)