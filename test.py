import unittest

from frename import *

class TestStringMethods(unittest.TestCase):

    def test_remove_characters(self):
        tests = [
            ("(Foo PHYS111) Syllabus Fall 16.doc", "(foo-phys111)-syllabus-fall-16.doc"),
            ("Rec+20+WS+solutions<<.pdf", "rec-20-ws-solutions.pdf"),
            ("Sweet%20Victory%20-%20Tuba.pdf", "sweet-victory-tuba.pdf"),
            ("Template%20%28Yellow%20Card%29%20%", "template-(yellow-card)"),
            ]

        for input, output in tests:
            result = get_new_filename(input)
            self.assertEqual(result, output,
                    msg=f"with input {input} got {result} instead of {output}")


if __name__ == '__main__':
    unittest.main()


