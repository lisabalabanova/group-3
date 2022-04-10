import unittest
import Tasks.Task14 as Task14


test_data = [
    {
        'V': [1,2,3,4,5],
        'E': [(1,4), (1,5), (2,1), (2,3), (3,1), (3,4), (4,5), (5,2)],
        'Outses': [[2, 4], [3, 5], [1, 5]],
        'Outses_L': [[2, 4], [3, 5], [1, 5]]
    }
]


class Testtask11(unittest.TestCase):

    def test(self):
        for data in test_data:
            Outses, Outses_L = Task14.ses(data['V'], data['E'])
            self.assertEqual(Outses, data['Outses'])
            self.assertEqual(Outses_L, data['Outses_L'])


if __name__ == '__main__':
    unittest.main()