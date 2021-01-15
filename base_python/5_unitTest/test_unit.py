import unittest
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(2, 2, "Is Eaual!")
        self.assertIn('t', 'this')

    @unittest.skipIf(1+1 == 2, "Skip test2")
    def test_case02(self):
        print("test_case02")
        self.assertEqual(2, 2, "Is Eaual!")

    def test_case03(self):
        print("test_case03")
        self.assertEqual(2, 2, "Is Eaual!")


class demo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_demo1_case01(self):
        print("test_case01")
        self.assertEqual(2, 2, "Is Eaual!")
        self.assertIn('t', 'this')

    @unittest.skipIf(1 + 1 == 2, "Skip test2")
    def test_demo1_case002(self):
        print("test_case02")
        self.assertEqual(2, 2, "Is Eaual!")

    def test_demo1_case003(self):
        print("test_case03")
        self.assertEqual(2, 2, "Is Eaual!")


if __name__ == '__main__':
    # 1 ------nly all-----
    # unittest.main()

    # 2 ______multi class_____
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case01"))
    suite.addTest(demo1("test_demo1_case002"))
    unittest.TextTestRunner().run(suite)
