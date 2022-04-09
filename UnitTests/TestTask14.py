import unittest
import Tasks.Task14 as Task14


test_data = [
    {
        'V': [1, 2, 3, 4, 5, 6, 7],
        'E': [(1,2),(1,4),(1,6),(1,7),(2,4),(2,6),(3,4),(3,5),(3,6),(3,7),(4,5),(5,6),(6,7)],
        'Outses': [[5, 6], [2, 5, 7], [4, 5, 7], [4, 6]],
        'Outses_L': [[5, 6], [4, 6]]
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