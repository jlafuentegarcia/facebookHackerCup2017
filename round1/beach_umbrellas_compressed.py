import sys
import time

BIG_PRIME = 1000000007

pascal_triangle = [[1], [1]]

def extend_pascal_triangle(n):
    for i in xrange(len(pascal_triangle), n+1):
        row = [1]
        for j in xrange(1, (i+2) / 2):
            row.append(mod_sum(get_pascal_triangle(i-1, j-1), get_pascal_triangle(i-1, j)))

        pascal_triangle.append(row)


def get_pascal_triangle(n, k, log=False):
    row = pascal_triangle[n]

    offset = 1 + ((n + 1) % 2)

    res = row[k] if k < len(row) else row[2 * len(row) - k - offset]

    if log:
        print '[' + str(n) + ', ' + str(k) + ']' + str(res)

    return res

permutations = [1, 1]


def extend_permutations(n):
    for i in xrange(len(permutations), n+1):
        permutations.append(mod_mult(permutations[i-1], i))


def memorize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            res = function(*args)
            memo[args] = res

            return res
    return wrapper


def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        T = int(f.readline().rstrip('\n'))

        cases = list()

        for t in xrange(T):
            N, M = map(int, f.readline().rstrip('\n').split(' '))
            sizes = list()
            for n in xrange(N):
                sizes.append(long(f.readline().rstrip('\n')))

            cases.append({'M': M, 'sizes': sizes})

    return cases


def mod_mult(a, b):
    return ((a % BIG_PRIME) * (b % BIG_PRIME)) % BIG_PRIME


def mod_sum(a, b):
    return ((a % BIG_PRIME) + (b % BIG_PRIME)) % BIG_PRIME


def compute_space(size):
    """
    Computes the space that is occupied by un umbrella of size 'size'
    :param size: The size of the umbrella
    :return: The occupied space
    """

    if (size % 2) == 0:
        size += 1
    return size


def compute_outer_space_in_border(size):
    """
    Computes the space of the umbrella that gets out of the border if it is put in one of the borders of the line.
    It is computed dividing by two the extra space that it occupies (apart of the stick)

    :param size: The size of the umbrella
    :return: the space of the umbrella that gets out of the border if it is put in one of the borders of the line.
    """
    return (compute_space(size) - 1) / 2


def compute_min_total_space(sizes, left_border_radius, right_border_radius):
    """
    Computes the minimum space occupied by all the umbrellas, given that umbrellas of index 'left_border_size'
    and 'right_border_size' are in the borders

    :param sizes:
    :param left_border_radius:
    :param right_border_radius:
    :return:
    """
    return sum(map(lambda x: x * 2, sizes)) + 1 - left_border_radius - right_border_radius


def compute_permutations(n):
    extend_permutations(n)
    return permutations[n]


def compute_combinations(n, k):
    if k == 0 or k == n:
        return 1

    extend_pascal_triangle(n)

    return get_pascal_triangle(n, k)


def compute_possibilities(sizes, M, left_border_id, right_border_id):
    nb_dark_holes = compute_min_total_space(sizes, sizes[left_border_id], sizes[right_border_id])

    nb_occupied_holes = len(sizes)
    nb_free_holes = M - nb_dark_holes

    if nb_free_holes < 0:
        return 0

    # Compute the different configurations in which the light holes can be
    free_configurations = compute_combinations(nb_occupied_holes + nb_free_holes, nb_free_holes)


    #compute the different possibilities to sort the rest
    rest_permutations = compute_permutations(len(sizes) - 2)

    return mod_mult(free_configurations, rest_permutations)


def compute_result(case):
    M = case['M']
    sizes = case['sizes']

    # Base cases
    if len(sizes) > M:
        return 0

    if len(sizes) == 0:
        return 0

    if len(sizes) == 1:
        return M

    combinations = 0

    for i in xrange(len(sizes)):
        for j in xrange(len(sizes)):
            if i != j:
                combinations = mod_sum(combinations, compute_possibilities(sizes, M, i, j))

    return combinations


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + str(o) + '\n')
            caseno += 1


def main():
    start = time.time()
    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    input_cases = read_input(input_file_name)

    print "Solving " + str(len(input_cases)) + " cases"

    output = list()
    for i, case in enumerate(input_cases):
        print "Solving case " + str(i)
        output.append(compute_result(case))
        print "    ...solved "

    store_output(output, output_file_name)
    end = time.time()

    print "Elapsed Time = " + str(end-start)


if __name__ == "__main__":
    main()
