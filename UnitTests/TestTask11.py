import unittest
import Tasks.task11 as task11


test_data = [
    {
        'V': [1, 2, 3, 4, 5, 6, 7],
        'E': [(1,2), (1,3), (1,5), (1,6), (2,3), (3,4), (3,6), (4,5), (4,7), (5,6), (6,7)],
        'OutLVS': [(1, 7), (2, 5, 7), (2, 4, 6), (1, 4), (3, 5, 7)],
        'OutLVS_L': [(2, 5, 7), (2, 4, 6), (3, 5, 7)]
    }
]


class Testtask11(unittest.TestCase):

    def test(self):
        for data in test_data:
            OutLVS, OutLVS_L = task11.lis(data['V'], data['E'])
            self.assertEqual(OutLVS, data['OutLVS'])
            self.assertEqual(OutLVS_L, data['OutLVS_L'])


if __name__ == '__main__':
    unittest.main()