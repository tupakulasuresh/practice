import unittest


def get_median(l1, l2):
    combined = sorted(l1 + l2)
    size = len(combined)
    med_index = size / 2
    median = float(combined[med_index] if size % 2 != 0
                   else sum(combined[med_index - 1:med_index + 1]) / 2.0)
    return median


class TestMedian(unittest.TestCase):

    def check_solution(self, l1, l2, exp):
        test_name = "Running {}".format(self._testMethodName)
        print("\n %s" % test_name)
        print("-" * (len(test_name) + 2))
        print("Input1  : %s" % l1)
        print("Input2  : %s" % l2)
        print("Expected: %s" % exp)

        got = get_median(l1, l2)
        print("Computed: %s" % got)

        self.assertEqual(got, exp)

    def test_01(self):
        l1 = [1, 3]
        l2 = [2]
        exp = 2.0

        self.check_solution(l1, l2, exp)

    def test_02(self):
        l1 = []
        l2 = [2, 3]
        exp = 2.5

        self.check_solution(l1, l2, exp)


if __name__ == "__main__":
    unittest.main()
