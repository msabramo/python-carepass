import unittest

from carepass import GoodRxAPI


class GoodRxTests(unittest.TestCase):

    def setUp(self):
        self.api = GoodRxAPI()

    def test_drugprices_low(self):
        ndc = '0071-0156'
        result = self.api.get_drugprices_low(
            name='lipitor',
            form='tablet',
            dosage='10mg',
            quantity=30,
            manufacturer='brand',
            ndc='0071-0155-23')
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['brand'], ['lipitor'])

    def test_drugprices_compare(self):
        ndc = '0071-0156'
        result = self.api.get_drugprices_compare(
            name='lipitor',
            form='tablet',
            dosage='10mg',
            quantity=30,
            manufacturer='brand',
            ndc='0071-0155-23')
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['brand'], ['lipitor'])
