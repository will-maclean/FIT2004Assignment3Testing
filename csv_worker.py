import os
import csv
import unittest


def list_to_csv(lst, filename):
    """
    Takes a list of ((str), int/bool) and writes to a csv
    :param lst: given list
    :param filename: filename to write to
    :return: None
    """

    with open(filename, 'w') as csv_file:
        file_writer = csv.writer(csv_file)

        for item in lst:
            row = []
            for i in item[0]:
                row.append(i)

            row.append(item[1])
            file_writer.writerow(row)


def csv_to_lst(filename):
    """
    Converts a csv to a list of ((str), int/bool)
    :param filename: *.csv, containing stored lst
    :return: lst of contents in csv
    """
    lst = []
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            first = tuple(row[:-1])
            if row[-1] == "True":
                second = True
            elif row[-1] == "False":
                second = False
            else:
                second = int(row[-1])
            lst.append((first, second))

    return lst


def add_test_cases(filename, cases):
    """
    Adds a lst of new test cases, of form ((str), bool/int) to an existing csv of test cases
    :param filename: existing csv of test cases
    :param cases: new cases to add
    """
    with open(filename, 'a') as csv_file:
        file_writer = csv.writer(csv_file)

        for item in cases:
            row = []
            for i in item[0]:
                row.append(i)

            row.append(item[1])
            file_writer.writerow(row)


class TestCsvWorker(unittest.TestCase):
    test_lst = [
            (("abbcc", "bccabccad"), False),
            (("abbcc", "d"), False),
            (("abbcc", "a"), 1),
            (("abbcc", "aaaa"), 4),
            (("abbcc", "bbb"), 2),
            (("abbcc", "bb"), 1),
            (("abbcc", "cccc"), 2),
            (("abbcc", "bcbc"), 2),
            (("abbcc", "cdc"), False),
            (("abbcc", "ccdcc"), False),
            (("abbcc", "abbccd"), False),
            (("abbcc", "dbbcca"), False),

        ]

    filename = "test_csv_worker.csv"

    def test_csv_worker(self):
        list_to_csv(self.test_lst, self.filename)
        read = csv_to_lst(self.filename)

        self.assertEqual(self.test_lst, read)

        os.remove(self.filename)

    def test_add_test_cases(self):
        list_to_csv(self.test_lst, "test_append.csv")

        new_cases = [
            (("abbcc", "abbccd"), False),
            (("abbcc", "dbbcca"), 4),
        ]
        add_test_cases("test_append.csv", new_cases)

        self.assertEqual(self.test_lst + new_cases, csv_to_lst("test_append.csv"))

        os.remove("test_append.csv")
