import os
import sys

current = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, current)

import unittest
import datetime


from frcm.fireriskmodel import compute
import testdata.test_testdata_fireriskmodel as test_testdata
from frcm.fireriskmodel import preprocess 


from frcm.datamodel import utils as dmutils
from frcm.datamodel import model as dm
from frcm.weatherdata import utils as wdutils


class TestUtil(unittest.TestCase):

    def setUp(self):

        self.observations_wdps = dmutils.list_to_wdps(test_testdata.frost_sample_weatherdatapoints)

        self.forecast_wdps = dmutils.list_to_wdps(test_testdata.met_sample_weatherdatapoints)

        self.location = dm.Location(latitude=60.383, longitude=5.3327)



    def test_compute_obs(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=self.location,
            data=list())

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)

    def test_compute_fct(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=list())

        forecast = dm.Forecast(
            location=self.location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)

    def test_compute(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=self.location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)


if __name__ == '__main__':
    unittest.main()
