import unittest

# Testing User database model
#
# TODO tests:
#     - User insertion/deletion/update/read
#     - Check if first user is an admin


class TestUserDao(unittest.TestCase):

    # Setup and teardown of entire test

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    # Setup and teardown for each test case

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Tests

    def test_is_first_user_admin(self):
        self.assertTrue(True)  # just to test that this is working


if __name__ == "__main__":
    unittest.main()