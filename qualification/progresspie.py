import sys
import math

pie_center = (50.0, 50.0)
pie_radius = 50.0
WHITE = 'white'
BLACK = 'black'
tolerance = 1e-6

def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        f.readline()

        cases = list()

        for line in f:
            line = line.rstrip('\n')
            progress, x, y = map(float, line.split(' '))
            cases.append(
                {'progress': progress,
                 'point': (x, y)})

    return cases


def compute_distance(point1, point2):
    return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))


def compute_progress_from_point(point):
    dx = point[0] - pie_center[0]
    dy = point[1] - pie_center[1]

    return 100.0 * (360 - (((math.degrees(math.atan2(dy, dx)) - 90) + 360) % 360)) / 360


def compute_color(input_data):
    point = input_data['point']

    # Out of the circle, white
    distance = compute_distance(point, pie_center)
    if distance >= pie_radius + tolerance:
        return WHITE

    progress = input_data['progress']
    point_progress = compute_progress_from_point(point)

    if point_progress > progress + tolerance:
        return WHITE

    return BLACK


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + o + '\n')
            caseno = caseno + 1


def main():
    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'
    
    input = read_input(input_file_name)
    output = map(compute_color, input)
    
    store_output(output, output_file_name)


if __name__ == "__main__":
    main()
