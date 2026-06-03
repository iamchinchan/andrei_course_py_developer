import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()

# Its not magic

# An object is being created, you just don't have to write the code for it.

# Because test_do_stuff takes self as a parameter, it strictly requires a live instance to run. unittest.main() handles all of this boilerplate behind the scenes.

# Here is the exact step-by-step of what the library does under the hood:

# Introspection (Scanning): When you execute unittest.main(), it scans the current file for any class that inherits from unittest.TestCase.

# Filtering: It looks inside your TestMain class for any method name that starts with the prefix test_.

# Instantiation (The Secret): For every single test method it finds, it creates a brand new, isolated instance of TestMain.

# Execution: It automatically calls the method on that newly created instance (e.g., instance.test_do_stuff()).

# It is not magic bypassing object-oriented rules; it is just a framework doing the heavy lifting so you only have to focus on writing the logic.
