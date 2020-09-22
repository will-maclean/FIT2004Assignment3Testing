import itertools
import random
import unittest

from assignment3 import *
import csv_worker
from copy import deepcopy


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def random_str(length):
    return "".join(chr(i) for i in random.choices(range(97, 123), k=length))


def format_build_substr(S, T):
    result = build_from_substrings(S, T)
    return (S, T), len(result) if result else result


def gen_build_substr(S):
    return [format_build_substr(S, "".join(T)) for T in itertools.permutations(S)]


def gen_build_substr_random():
    return flatten([gen_build_substr(random_str(l)) for l in range(1, 8)])


def gen_build_substr_random_with_properties():
    cases = set()
    for l in range(1, 3):
        sorted_str = "".join(sorted(random_str(l)))
        reversed_str = sorted_str[::-1]
        sorted_with_repeats = "".join(i * 3 for i in sorted_str)
        reversed_sorted_with_repeats = sorted_with_repeats[::-1]
        strings = [sorted_str, reversed_str, sorted_with_repeats, reversed_sorted_with_repeats]
        cases = cases.union(frozenset(flatten([gen_build_substr(S) for S in strings])))

        # False cases
        # all_same = random_str(1) * l
        # for T in itertools.permutations(random_str(8)):
        #     cases.add(format_build_substr(all_same, "".join(T)))
    return cases


def gen_alpha_pos_random():
    cases = []
    for i in range(1, 30):
        text = [random_str(random.randint(1, 10)) for _ in range(random.randint(1, i))]
        query_list = [random_str(random.randint(1, 20)) for _ in range(random.randint(1, i) * random.randint(1, i))]
        cases.append(((text, query_list), alpha_pos(text, query_list)))
    return cases


def gen_alpha_pos_random_with_properties():
    cases = []
    for i in range(1, 30):
        all_same = [random_str(1) * i] * i
        sorted_strings = sorted([random_str(random.randint(1, 10)) for _ in range(random.randint(1, i))])
        reversed_strings = sorted_strings[::-1]
        query_list = [random_str(random.randint(1, i)) for _ in range(random.randint(1, i) * random.randint(1, i))]
        text_lists = [all_same, sorted_strings, reversed_strings]
        for text in text_lists:
            cases.append(((text, query_list), alpha_pos(text, query_list)))
    return cases


class TestAssignment2(unittest.TestCase):
    def check_input_unmodified(self, func, case):
        original = deepcopy(case)
        solution = func(*case)
        self.assertEqual(original, case, msg="input modified!")
        return solution

    def check_build_substr(self, substr_lst, S, T):
        result = []
        for start, end in substr_lst:
            self.assertGreaterEqual(end, start, msg="end index is greater than start index")
            self.assertGreaterEqual(start, 0, msg="substring index is negative")
            self.assertLess(end, len(S), msg="substring end index is out of bounds")
            result.append(S[start:end+1])
        self.assertEqual(T, "".join(result), msg="formed string is not equal to T")

    def test_build_from_substrings(self):
        # return  # uncomment this if you haven't implemented this function yet

        all_cases = csv_worker.csv_to_lst("build_from_substrings.csv")
        for case, expected in all_cases:
            solution = self.check_input_unmodified(build_from_substrings, case)
            length = len(solution) if isinstance(solution, list) else solution
            self.assertEqual(expected, length, msg="wrong value!")
            if solution:
                self.check_build_substr(solution, *case)

        # print(",\n".join(str(i) for i in gen_build_substr_random_with_properties()))

    def test_alpha_pos(self):
        # return  # uncomment this if you haven't implemented this function yet

        all_cases = csv_worker.csv_to_lst("alpha_pos.csv")
        for case, expected in all_cases:
            solution = self.check_input_unmodified(alpha_pos, case)
            self.assertEqual(expected, solution, msg="wrong value!")

        print(",\n".join(str(i) for i in gen_alpha_pos_random_with_properties()))


if __name__ == '__main__':
    unittest.main()
