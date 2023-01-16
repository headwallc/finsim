import unittest

from finsim.product import FinancialProduct, uncapped_floor_0_spread_8, value_floor_0_cap_10


class ProductTest(unittest.TestCase):
    def test_product_f_id(self):
        product = FinancialProduct("idem", lambda x: x)
        expected = [
            (0.1, 0.1),
            (0.5, 0.5),
            (-0.3, -0.3),
        ]
        for (input, output) in expected:
            self.assertEqual(product.adjusted_gain(input), output)

    def test_product_f_value_cap_10(self):
        prod = value_floor_0_cap_10
        expected = [
            (0.1, 0.1),
            (0.5, 0.1),
            (-0.3, 0.0),
        ]
        for (input, output) in expected:
            self.assertEqual(prod.adjusted_gain(input), output)

    def test_product_param_value_cap_10(self):
        prod = FinancialProduct("value_cap_10_param", floor=0, cap=0.1)
        expected = [
            (0.1, 0.1),
            (0.5, 0.1),
            (-0.3, 0.0),
        ]
        for (input, output) in expected:
            self.assertEqual(prod.adjusted_gain(input), output)

    def test_product_f_uncapped_spread_8(self):
        product = uncapped_floor_0_spread_8
        expected = [
            (0.1, 0.02),  # 10% -> 2%
            (0.12, 0.04),  # 12% -> 4%
            (0.05, 0.0),  # 5% -> 0%
            (-0.3, 0.0),  # -30% -> 0%
        ]
        for (input, output) in expected:
            self.assertAlmostEqual(product.adjusted_gain(input), output, places=4)

    def test_product_param_uncapped_spread_8(self):
        product = FinancialProduct("uncapped_spread_8_param", floor=0, spread=0.08)
        expected = [
            (0.1, 0.02),  # 10% -> 2%
            (0.12, 0.04),  # 12% -> 4%
            (0.05, 0.0),  # 5% -> 0%
            (-0.3, 0.0),  # -30% -> 0%
        ]
        for (input, output) in expected:
            self.assertAlmostEqual(product.adjusted_gain(input), output, places=4)


if __name__ == '__main__':
    unittest.main()
