from codingbuzz.tireless_runner import TirelessRunner
from random import randint


def solution(input_file_path):
    f = open(input_file_path, 'r')
    (a, b) = map(int, f.readline().split(' '))
    f.close
    x = randint(-100, 100)
    result = a * x**2 + b
    solution = "x = {}".format(x)
    return (result, solution)


TirelessRunner(solution).run()