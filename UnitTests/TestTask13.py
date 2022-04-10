import unittest
import Tasks.task13 as task13


test_data = [
    {
        'V': [1,2,3,4,5,6,7],
        'E': [(1,2), (1,3), (1,5), (1,6), (2,3), (3,4), (3,6), (4,5), (4,7), (5,6), (6,7)],
        'OutDfs': [[2, 5, 6], [2, 5, 7], [3, 4], [3, 6], [3, 5, 7], [2, 6, 7], [1, 4], [1, 7], [2, 4, 5], [2, 4, 6], [2, 4, 7], [1, 5, 6]],
        'OutDfs_L': [[3, 4], [3, 6], [1, 4], [1, 7]]
    }
]


class Testtask11(unittest.TestCase):

    def test(self):
        for data in test_data:
            OutDfs, OutDfs_L = task13.Dfs(data['V'], data['E'])
            self.assertEqual(OutDfs, data['OutDfs'])
            self.assertEqual(OutDfs_L, data['OutDfs_L'])


if __name__ == '__main__':
    unittest.main()