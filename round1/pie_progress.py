import sys
import math

INFINITY = float('inf')


def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        T = int(f.readline().rstrip('\n'))

        cases = list()

        for t in xrange(T):
            N, M = map(int, f.readline().rstrip('\n').split(' '))
            prices = list()
            for n in xrange(N):
                prices.append(map(float, f.readline().rstrip('\n').split(' ')))

            cases.append(prices)

    return cases


def compute_cost(solution, prices):
    cost = 0.0
    for day_pies, day_prices in zip(solution, prices):
        pie_cost = sum([day_prices[p] for p in day_pies])
        extra_tax = math.pow(len(day_pies), 2)

        cost += (pie_cost + extra_tax)

    return cost


def buy_one_more(prev_solution, prices):
    best_cost = INFINITY
    best_buy = None

    solution = [list(day_pies) for day_pies in prev_solution]

    for d in xrange(len(prices)):
        day_pies = solution[d]
        day_prices = prices[d]

        for p in [p for p in xrange(len(day_prices)) if p not in day_pies]:
            day_pies.append(p)
            curr_cost = compute_cost(solution, prices)

            if curr_cost <= best_cost:
                best_cost = curr_cost
                best_buy = (d, p)

            day_pies.pop()

    assert best_buy

    solution[best_buy[0]].append(best_buy[1])

    return solution


def get_solution(prices):
    print 'computing case ' + str(prices)

    solution = [list()] * len(prices)

    for d in xrange(len(prices)):
        solution = buy_one_more(solution, prices)

    return solution


def store_output(output, output_file_name):
    with open(output_file_name, 'w') as f:
        caseno = 1
        for o in output:
            f.write("Case #" + str(caseno) + ": " + str(o) + '\n')
            caseno = caseno + 1


def main():
    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    input_prices = read_input(input_file_name)
    output = map(lambda prices: int(round(compute_cost(get_solution(prices), prices))), input_prices)

    store_output(output, output_file_name)


if __name__ == "__main__":
    main()
