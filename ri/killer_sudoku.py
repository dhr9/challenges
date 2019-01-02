import copy
import argparse
from time import time
from math import ceil

class KillerSudokuSolver:
    def __init__(self):
        self._factors_cache = {}

    def __are_no_numbers_available(self, _available_numbers):
        return sum(_available_numbers) == 0

    def get_factors(self, sum_, num):
        assert sum_ > 0 and num > 0

        def recurse(sum_, num,  max_number):
            assert sum_ > 0 and num > 0

            # TODO(riyansh): hashing triples the runtime, figure out why
            # if cached values already available, return cached value
            # hash = str(sum_) + '-' + str(num) + '-' + str(max_number)
            # if hash in self._factors_cache:
            #     return self._factors_cache[hash]

            # only one number to fill the sum
            if num == 1:
                if sum_ <= max_number:
                    # only one solution, with only one element
                    return [[sum_]]
                else:
                    return None

            # --------------------------------------------------
            # this case handled when max_search_number = sum - 1
            # --------------------------------------------------
            # sum is 1, but more than 1 numbers need to add up to 1
            # if _sum == 1:
            #     return None

            # determine the max number to start the search with
            max_search_number = max_number if sum_ > max_number else sum_ - 1

            # determine the min number to stop the search at
            # for example, starting at 9, you should end at 5
            # because when try for 4, the complement search will
            # start at 5 again, which will make for duplicate work
            min_search_number = ceil(max_search_number/2)

            # list of all possible solutions
            possible_solutions = []

            for i in range(max_search_number, min_search_number-1, -1):
                remaining_solutions = recurse(sum_ - i, num - 1, i-1)

                # we have a solution, possibly multiple solutions
                if remaining_solutions:
                    for remaining_solution in remaining_solutions:
                        solution = [i]
                        solution.extend(remaining_solution)
                        possible_solutions.append(solution)

                # exhaust the current number, so as to try only
                # for numbers smaller than the current number.
                # This results in only a single permutation
                # (the one in descending order) to be present in
                # the possible_solutions.
                # For example, [1, 2] will never be a solution to
                # the call recurse(3, 2), only [2, 1]
                # available_numbers[i] = 0
                        
            # empty solutions list means no solutions
            if not possible_solutions:
                possible_solutions = None

            # TODO(riyansh): hashing triples the runtime, figure out why
            # self._factors_cache[hash] = possible_solutions
            return possible_solutions

        return recurse(sum_, num, 9)

def factorize_time(n, num_factors, N):
    ks = KillerSudokuSolver()
    ts = time()
    for i in range(N):
        ks._factors_cache = {}
        ks.get_factors(n, num_factors)
    te = time()
    print((te - ts) * 1000000.0 / N, "us")
    print(ks.get_factors(n, num_factors))

def find_most_difficult_factorization():
    ks = KillerSudokuSolver()
    max_num_factors = 0
    max_sum = 0
    max_box = 0
    max_factors = []
    for sum_ in range(1, (45*9) + 1):
        for box in range(1, 91):
            factors = ks.get_factors(sum_, box)
            if factors is None: continue
            if len(factors) > max_num_factors:
                max_num_factors = len(factors)
                max_sum = sum_
                max_box = box
                max_factors = factors

    print(max_sum)
    print(max_box)
    print(max_num_factors)
    print(max_factors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='factorize a number into `n` unique numbers from 1 to 9')
    parser.add_argument('n', type=int)
    parser.add_argument('num_factors', type=int)
    parser.add_argument('N', type=int)

    args = parser.parse_args()
    ks = KillerSudokuSolver()

    # time the factorize function
    factorize_time(args.n, args.num_factors, args.N)
