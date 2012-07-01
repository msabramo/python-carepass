import os
import urllib

import requests


class GoodRxAPI(object):

    url_format = '{carepass_api_url}/good-rx-api/drugprices/{method}?apikey={api_key}'

    def __init__(self, carepass_api_url=None, api_key=None):
        if not carepass_api_url:
            carepass_api_url = os.getenv("CAREPASS_API_URL")

        if not api_key:
            api_key = os.getenv("CAREPASS_GOODRX_API_KEY")

        self.carepass_api_url = carepass_api_url
        self.api_key = api_key

    def get_drugprices_low(self, name, form, dosage, quantity, manufacturer, ndc):
        return self._do_get(
            'low',
            name=name,
            form=form,
            dosage=dosage,
            quantity=quantity,
            manufacturer=manufacturer,
            ndc=ndc)

    def get_drugprices_compare(self, name, form, dosage, quantity, manufacturer, ndc):
        return self._do_get(
            'compare',
            name=name,
            form=form,
            dosage=dosage,
            quantity=quantity,
            manufacturer=manufacturer,
            ndc=ndc)

    def _do_get(self, method, **kwargs):
        url = self._get_url('compare') + '&' + urllib.urlencode(kwargs)
        response = requests.get(url)
        return response.json

    def _get_url(self, method, **kwargs):
        vars = self.__dict__
        vars.update(**kwargs)
        vars['method'] = method.format(**vars)
        # print(vars)
        return self.url_format.format(**vars)


class MedCostOfCareAPI(object):

    url_format = '{carepass_api_url}/ecc-directory-api/{method}?apikey={api_key}'

    def __init__(self, carepass_api_url=None, api_key=None):
        if not carepass_api_url:
            carepass_api_url = os.getenv("CAREPASS_API_URL")

        if not api_key:
            api_key = os.getenv("CAREPASS_ECC_API_KEY")

        self.carepass_api_url = carepass_api_url
        self.api_key = api_key

    def get_medical_cpt_zip(self, cpt, zip):
        return self._do_get('med/{cpt}/zip/{zip}', cpt=cpt, zip=zip)

    def get_medical_cpt_lat_long(self, cpt, lat_long):
        return self._do_get('med/{cpt}/{lat_long}', cpt=cpt, lat_long=lat_long)

    def get_medical_cpt(self):
        return self._do_get('med/cpt')

    def get_dental_cpt_zip(self, cpt, zip):
        return self._do_get('med/{cpt}/zip/{zip}', cpt=cpt, zip=zip)

    def get_dental_cpt_lat_long(self, cpt, lat_long):
        return self._do_get('med/{cpt}/{lat_long}', cpt=cpt, lat_long=lat_long)

    def get_dental_cpt(self):
        return self._do_get('med/cpt')

    def get_categories(self):
        return self._do_get('categories')

    def get_category(self, category):
        return self._do_get('categories/{category}', category=category)

    def _do_get(self, method, **kwargs):
        url = self._get_url(method, **kwargs)
        # print(url)
        response = requests.get(url)
        return response.json

    def _get_url(self, method, **kwargs):
        vars = self.__dict__
        vars.update(**kwargs)
        vars['method'] = method.format(**vars)
        # print(vars)
        return self.url_format.format(**vars)
