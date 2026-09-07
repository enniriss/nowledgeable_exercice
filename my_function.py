def addition(a, b):
	return a + b


import unittest


class TestAddition(unittest.TestCase):

    def test_deux_positifs(self):
        resultat = addition(2, 3)
        self.assertEqual(resultat, 5)


if __name__ == "__main__":
    unittest.main()

