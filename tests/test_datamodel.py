import unittest
import datetime

import os
import sys

current = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, current)

from src.frcm.datamodel import model as dm
from src.frcm.datamodel import utils

import testdata.test_testdata_datamodel as test_testdata



class TestDataModel(unittest.TestCase):

    def setUp(self):
        self.observations_wdps = utils.list_to_wdps(test_testdata.frost_sample_weatherdatapoints)
        self.forecast_wdps = utils.list_to_wdps(test_testdata.met_sample_weatherdatapoints)

    def test_validate(self):
        timedelta_ok = datetime.timedelta(minutes=70)
        timedelta_nok = datetime.timedelta(minutes=30)

        location = dm.Location(latitude=60.383, longitude=5.3327)

        observations = dm.Observations(
            source="testdata",
            location=location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        self.assertTrue(utils.wd_validate(weatherdata, timedelta_ok))
        self.assertFalse(utils.wd_validate(weatherdata, timedelta_nok))


if __name__ == '__main__':
    unittest.main()
