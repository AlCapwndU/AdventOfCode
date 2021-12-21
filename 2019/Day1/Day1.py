# Fuel = floor(Mass/3) - 2

masses = [145963, 119152, 122543, 145710, 133900, 132606, 52408, 53565, 59976, 81701, 121675, 107404, 134873, 141724,
          138465, 96966, 77092, 127607, 142761, 77766, 68747, 126829, 54471, 148637, 69409, 104756, 144862, 81599,
          82815, 123923, 125193, 60380, 84496, 98728, 97193, 111796, 144980, 135001, 136717, 82743, 78261, 143756,
          127891, 111665, 121793, 136152, 144144, 117761, 108060, 94355, 93797, 123979, 122509, 114558, 140655, 94911,
          94615, 54266, 149172, 101186, 132465, 108057, 134115, 74910, 63397, 132916, 56643, 142422, 68900, 146027,
          63015, 71272, 118759, 101247, 114596, 147249, 92866, 93567, 84820, 67882, 87459, 148556, 71855, 53522, 101978,
          82314, 86692, 102372, 92084, 99883, 62642, 57330, 110474, 70679, 101075, 79706, 79487, 139548, 122700, 96657]

total_fuel = 0
fuel = int()

for m in masses:
    fuel = int(m / 3) - 2
    total_fuel += fuel
    while fuel > 0:
        fuel = int(fuel/3) - 2
        if fuel > 0:
            total_fuel += fuel
            print(fuel)
    print(total_fuel)

print(total_fuel)

