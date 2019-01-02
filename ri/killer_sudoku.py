import copy
import argparse
from time import time

class KillerSudokuSolver:
    def __init__(self):
        self._factors_cache = {}

    def __are_no_numbers_available(self, _available_numbers):
        return sum(_available_numbers) == 0

    def get_factors(self, _sum, _num, _available_numbers=None):
        assert _sum > 0 and _num > 0

        # TODO(riyansh): Maybe use sorted hash table
        if _available_numbers is None:
            _available_numbers = [1 for _ in range(10)]
            _available_numbers[0] = 0

        def recurse(_sum, _num, _available_numbers):
            assert _sum > 0 and _num > 0

            # cached values already available
            # TODO(riyansh)

            # only one number to fill the sum
            if _num == 1:
                if _sum < 10 and _available_numbers[_sum] == 1:
                    # only one solution, with only one element
                    return [[_sum]]
                else:
                    return None

            # --------------------------------------------------
            # this case handled when max_search_number = sum - 1
            # --------------------------------------------------
            # sum is 1, but more than 1 numbers need to add up to 1
            # if _sum == 1:
            #     return None

            # -----------------------------------------------------
            # this case handled when if _available_numbers[i] == 1:
            # -----------------------------------------------------
            # no numbers available
            # if self.__are_no_numbers_available(_available_numbers):
            #     return None

            # determine the max number to start the search with
            # if _sum < 9, then _sum - 1
            # (_sum - 1 because there are atleast 2 numbers that need to 
            # add up to sum (_num > 1))
            # if not, then 9
            max_search_number = _sum - 1 if _sum < 9 else 9

            # list of all possible solutions
            possible_solutions = []

            # TODO(riyansh): optimize, maybe use sorted hash table as above
            for i in range(max_search_number, 0, -1):
                if _available_numbers[i] == 1:
                    # i is available, try to find solutions
                    new_available_numbers = copy.copy(_available_numbers)
                    new_available_numbers[i] = 0
                    remaining_solutions = recurse(_sum - i, _num - 1, new_available_numbers)

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
                    _available_numbers[i] = 0
                        
            # empty solutions list means no solutions
            if not possible_solutions:
                return None

            return possible_solutions

        return recurse(_sum, _num, _available_numbers)

def factorize_time(n, num_factors, N):
    ks = KillerSudokuSolver()
    ts = time()
    for i in range(N):
        ks.get_factors(n, num_factors)
    te = time()
    print((te - ts) * 1000.0 / N, "ms")
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
