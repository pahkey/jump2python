import math

width = 200
height = 80

square_size = math.gcd(200, 80)
print("타일 한 선의 길이:{}".format(square_size))

width_count = width/square_size
height_count = height/square_size

print("필요한 타일의 갯수:{}".format(int(width_count * height_count)))
