import os
import csv
import unittest


def list_to_csv_build_sub(lst, filename):
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


def csv_to_lst_build_sub(filename):
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


def add_test_cases_build_sub(filename, cases):
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


def list_to_csv_alpha_pos(lst, filename):
    """
    Takes a list of (([str], [str]), [int]) and writes to a csv
    :param lst: given list
    :param filename: filename to write to
    :return: None
    """

    with open(filename, 'w') as csv_file:
        file_writer = csv.writer(csv_file)

        for item in lst:
            row = []
            for i in item[0][0]:
                row.append(i)

            row.append(-1)

            for i in item[0][1]:
                row.append(i)

            row.append(-1)

            for i in item[1]:
                row.append(i)

            file_writer.writerow(row)


def csv_to_lst_alpha_pos(filename):
    """
    Converts a csv to a list of (([str], [str]), [int])
    :param filename: *.csv, containing stored lst
    :return: lst of contents in csv
    """
    lst = []
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            lst1 = []
            index = 0
            while row[index] != "-1":
                lst1.append(row[index])
                index += 1
            index += 1

            lst2 = []
            while row[index] != "-1":
                lst2.append(row[index])
                index += 1
            index += 1

            lst3 = []
            for i in range(index, len(row)):
                lst3.append(int(row[i]))

            lst.append(((lst1, lst2), lst3))

    return lst


def add_test_cases_alpha_pos(lst, filename):
    """
    Takes a list of (([str], [str]), [int]) and writes to a csv
    :param lst: given list
    :param filename: filename to write to
    :return: None
    """

    with open(filename, 'a') as csv_file:
        file_writer = csv.writer(csv_file)

        for item in lst:
            row = []
            for i in item[0][0]:
                row.append(i)

            row.append(-1)

            for i in item[0][1]:
                row.append(i)

            row.append(-1)

            for i in item[1]:
                row.append(i)

            file_writer.writerow(row)


class TestCsvWorker(unittest.TestCase):
    test_lst_build_sub = [
            # Write other cases here with only the size of substrings (or False)
            # But it would be nice to include your solution as a comment :)
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

    def test_csv_worker_build_sub(self):
        list_to_csv_build_sub(self.test_lst, self.filename)
        read = csv_to_lst_build_sub(self.filename)

        self.assertEqual(self.test_lst_build_sub, read)

        os.remove(self.filename)

    def test_add_test_cases(self):
        list_to_csv_build_sub(self.test_lst_build_sub, "test_append.csv")

        new_cases = [
            (("abbcc", "abbccd"), False),
            (("abbcc", "dbbcca"), 4),
        ]
        add_test_cases_build_sub("test_append.csv", new_cases)

        self.assertEqual(self.test_lst + new_cases, csv_to_lst_build_sub("test_append.csv"))

        os.remove("test_append.csv")
