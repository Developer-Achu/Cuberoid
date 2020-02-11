import random
import CubeRotations

random.seed(183890)


def get_side_matrix(color, n):
    side = {}
    for i in range(n):
        for j in range(n):
            side.update({str(i) + str(j): color})
    return side


def generate_solved_cube_matrix(n):
    generated_sides = []
    color_list = ['w', 'r', 'g', 'o', 'b', 'y']
    for index, color in enumerate(color_list):
        generated_sides.append(get_side_matrix(color, n))
    return generated_sides


# if len(sys.argv) == 3:
#     n = sys.argv[1]
#     scramble_size = sys.argv[2]
# else:
#     print("Invalid argument count")
#     exit(0)

n = 3
scramble_size = 1

sides = generate_solved_cube_matrix(n)
cube_slices_list = [1, 2, 3]
axes_list = ['x', 'y', 'z']
rotations_list = [90, 180, 270]

for scramble in range(scramble_size):
    cube_slice = random.choice(cube_slices_list)
    axis = random.choice(axes_list)
    rotation = random.choice(rotations_list)
    if n == 3:
        sides = CubeRotations.rotate_cube_3x3(cube_slice, axis, rotation, sides)


