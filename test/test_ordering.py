from json import JSONDecoder
from os.path import dirname, join
import unittest

from LivelyLetter.model import Letter

THIS_DIR = dirname(__file__)
SAMPLE_NUM = 1000


class TestTwoItemReverse(unittest.TestCase):

    def setUp(self):
        super(TestTwoItemReverse, self).setUp()

    def tearDown(self):
        super(TestTwoItemReverse, self).tearDown()

    def test_start_and_end(self):
        """test for case when re-orderable strings are only at start and end"""
        expected = 2
        with open(join(THIS_DIR, "ordering_letter1.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text)
        uniq_ltrs = set()
        for i in xrange(SAMPLE_NUM):
            uniq_ltrs.add(ltr_obj.apply_ordering())
        actual = len(uniq_ltrs)
        self.assertEqual(expected, actual)

    def test_ordering_and_choice(self):
        """test for having a multiple-choice within an ordering"""
        expected = 2  # either option can go in either place
        with open(join(THIS_DIR, "order_choice_letter.txt"), "r") as f:
            text = f.read().strip()
        with open(join(THIS_DIR, "input_dict.json"), "r") as f:
            subs_dict = JSONDecoder().decode(f.read())
        ltr_obj = Letter(text, subs_dict)
        uniq_ltrs = set()
        for i in xrange(SAMPLE_NUM):
            uniq_ltrs.add(ltr_obj.apply_all())
        actual = len(uniq_ltrs)
        print [x for x in uniq_ltrs]
        self.assertEqual(expected, actual)
