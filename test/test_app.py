import unittest

from src.app import div





class BaseTestRunner(unittest.TestCase):
    def setUp(self) -> None:
        print("\tsetUp BaseTestRunner")
    def tearDown(self) -> None:
         print("\ttearDown BaseTestRunner")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass BaseTestRunner")
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass BaseTestRunner")




class TestApp(BaseTestRunner):
    def setUp(self) -> None:
        print("\tsetUp")
    # def tearDown(self) -> None:
    #      print("\ttearDown")

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("setUpClass")
    @classmethod
    def tearDownClass1(cls) -> None:
        print("tearDownClass")

    def  test_app_1(self):
        self.assertEqual(3, div(9, 3))
    def  test_app_2(self):
        self.assertEqual(4, div(9, 3))


if __name__ == "__main__":
    unittest.main()