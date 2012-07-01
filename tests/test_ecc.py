import unittest

from carepass import MedCostOfCareAPI


class EstimatedCostOfCareTests(unittest.TestCase):

    def setUp(self):
        self.api = MedCostOfCareAPI()

    def test_get_medical_cpt_zip(self):
        cpt = '99201'
        zip = '06111'
        result = self.api.get_medical_cpt_zip(cpt, zip)
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['category'], 'Office Visits')
        self.assertEqual(result[0]['code'], cpt)

    def test_get_medical_cpt_lat_long(self):
        cpt = '99201'
        lat_long = '41.6870,-72.7308'
        result = self.api.get_medical_cpt_lat_long(cpt, lat_long)
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['category'], 'Office Visits')
        self.assertEqual(result[0]['code'], cpt)

    def test_get_medical_cpt(self):
        result = self.api.get_medical_cpt()
        # print(result)
        self.assertGreater(len(result), 300)

    def test_get_dental_cpt_zip(self):
        cpt = '99201'
        zip = '06111'
        result = self.api.get_dental_cpt_zip(cpt, zip)
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['category'], 'Office Visits')
        self.assertEqual(result[0]['code'], cpt)

    def test_get_dental_cpt_lat_long(self):
        cpt = '99201'
        lat_long = '41.6870,-72.7308'
        result = self.api.get_dental_cpt_lat_long(cpt, lat_long)
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['category'], 'Office Visits')
        self.assertEqual(result[0]['code'], cpt)

    def test_get_dental_cpt(self):
        result = self.api.get_dental_cpt()
        # print(result)
        self.assertGreater(len(result), 300)

    def test_get_categories(self):
        result = self.api.get_categories()
        # print(result)
        self.assertGreater(len(result), 1)
        self.assertIn('Dental', result)
        self.assertIn('Medical Tests', result)

    def test_get_category(self):
        result = self.api.get_category('Dental')
        # print(result)
        self.assertGreater(len(result), 1)
        self.assertIn('Dentures', result)
        self.assertIn('Fillings', result)
        result = self.api.get_category('Medical Tests')
        # print(result)
        self.assertGreater(len(result), 1)
