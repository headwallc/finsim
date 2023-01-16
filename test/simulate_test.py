import unittest
from finsim.simulation import *


class SimulateTest(unittest.TestCase):
    def test_simulate_gains(self):
        pool = [1, 2, 3]
        k = 5
        res = simulate_gains(pool, k)
        self.assertEqual(k, len(res))
        for r in res:
            self.assertTrue(r in pool)

    def test_simulate_gain_matrix(self):
        pool = [1, 2, 3]
        k = 5
        N = 10
        res = simulate_gain_matrix(pool, k, N)
        self.assertEqual(N, len(res))
        for r in res:
            self.assertEqual(k, len(r))
            for v in r:
                self.assertTrue(v in pool)

    def test_simulate_terminal_gains(self):
        gains = [0.3, -0.2, 0.1]  # 1.3 * 0.8 * 1.1 = 1.144
        res = calculate_returns(gains)
        self.assertAlmostEqual(1.144, res, places=4)

    def test_simulate_terminal_gains_cap(self):
        gains = [0.3, -0.2, 0.1]  # 1.3 * 0.8 * 1.1 = 1.144
        capf = lambda x: 0 if x < 0 else x if x < 0.1 else 0.1  # cap at 10%, but not negative
        res = calculate_returns(gains, capf)  # 1.1 * 1 * 1.1 = 1.21
        self.assertAlmostEqual(1.21, res, places=4)


if __name__ == '__main__':
    unittest.main()
