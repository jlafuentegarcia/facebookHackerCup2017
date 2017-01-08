import math
import sys

MIN_WEIGHT = 50.0


def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        nb_days = int(f.readline().rstrip('\n'))

        cases = list()

        for day in xrange(nb_days):
            case = list()

            nb_objects = int(f.readline().rstrip('\n'))

            for obj in xrange(nb_objects):
                weight = int(f.readline().strip('\n'))
                case.append(weight)
            cases.append(case)

    return cases


def is_possible(sorted_objects, nb_trips):
    if len(sorted_objects) < nb_trips:
        return False

    nb_needed_objects = sum(map(lambda x: math.ceil(MIN_WEIGHT / x),  sorted_objects[0:nb_trips]))

    return nb_needed_objects <= len(sorted_objects)


def get_max_nb_trips(objects):
    sorted_objects = sorted(objects, reverse=True)

    for nb_trips in xrange(1, len(objects) + 2):
        if not is_possible(sorted_objects, nb_trips):
            return nb_trips - 1

    return -1


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + str(o) + '\n')
            caseno = caseno + 1


def main():
    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    input = read_input(input_file_name)
    output = map(get_max_nb_trips, input)

    store_output(output, output_file_name)


if __name__ == "__main__":
    main()
