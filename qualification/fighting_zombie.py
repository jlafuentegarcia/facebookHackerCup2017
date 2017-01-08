import sys
import re


def read_input(file_name):
    with open(file_name, 'r') as f:
        # Remove first line
        nb_zombies = int(f.readline().rstrip('\n'))

        cases = list()

        for day in xrange(nb_zombies):
            damage, nb_spells = map(int, f.readline().rstrip('\n').split(' '))
            spells = f.readline().rstrip('\n').split(' ')

            case = {'damage': damage,
                    'spells': spells}

            cases.append(case)

    return cases


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


@memorize
def compute_prob(damage, rolls, sides):
    sum_probs = 0.0

    if damage > rolls * sides:
        return 0.0

    if damage < rolls:
        return 1.0

    if rolls == 1:
        return float(sides - max(0, damage - 1)) / sides

    for o in xrange(1, sides+1):
        sum_probs += compute_prob(damage - o, rolls - 1, sides)

    return sum_probs / sides


def parse_spell(spell):
    spell_list = map(int, re.findall('[+-]*[0-9]+', spell))

    rolls = spell_list[0]
    sides = spell_list[1]
    offset = spell_list[2] if len(spell_list) == 3 else 0

    return rolls, sides, offset


def get_max_prob(damage, spells):
    max_prob = 0
    for spell in spells:
        rolls, sides, offset = parse_spell(spell)

        max_prob = max(max_prob, compute_prob(damage - offset, rolls, sides))

    return max_prob


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
    output = map(lambda x: get_max_prob(x['damage'], x['spells']), input)

    store_output(output, output_file_name)


if __name__ == "__main__":
    main()
