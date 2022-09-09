import os
import pandas as pd
import unittest
from PostCodeUK.postcode import PostCode


TEST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\" + "tests" + "\\"
test_file_name = 'test_cases.csv'


class PostCodeTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PostCodeTestCase, self).__init__(*args, **kwargs)
        self.pcObj = PostCode()
        self.test_data = pd.read_csv(TEST_DIR + test_file_name)
        self.pcNames = self.test_data['postcodeName']

    def test_postcode_formatting(self):
        test_formatting = []
        for pcName in self.pcNames:
            with self.subTest(pcName=pcName):
                pcName = pcName.upper()
                if ' ' in pcName:
                    pcName = pcName.replace(" ", "")

                val_bool = self.pcObj.validate_postcode_Regex(pcName)
                if val_bool:
                    test_formatting.append("PASS")
                else:
                    test_formatting.append("FAIL")
                self.assertEqual(val_bool, True), "postcode in wrong format"
        self.test_data['test_formatting'] = test_formatting
        self.test_data.to_csv(TEST_DIR + "TestResults" + "\\" + "test_formatting.csv", sep='\t')

    def test_postcode_validating(self):
        test_validation = []
        for pcName in self.pcNames:
            with self.subTest(pcName=pcName):
                pcName = pcName.upper()
                if ' ' in pcName:
                    pcName = pcName.replace(" ", "")
                val_bool = self.pcObj.validate_postcode(pcName)
                if val_bool:
                    test_validation.append("PASS")
                else:
                    test_validation.append("FAIL")
                self.assertEqual(val_bool,
                                 True), "postcode Not in Database"  # add assertion here
        self.test_data['test_validation'] = test_validation
        self.test_data.to_csv(TEST_DIR + "TestResults" + "\\" + "test_validation.csv", sep='\t')


if __name__ == '__main__':
    unittest.main()
