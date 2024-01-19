import os
import sys

current = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, current)

import unittest
import datetime

import sampledata.frost_sample_weatherdata
import sampledata.met_sample_weatherdata

from src.frcm.datamodel import model as dm
from src.frcm.fireriskmodel import preprocess as pp
from src.frcm.fireriskmodel.parameters import delta_t

from src.frcm.weatherdata import utils


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.observations_wdps = \
            utils.weatherdata_parse(sampledata.frost_sample_weatherdata.frost_sample_weatherdata['data'])

        self.forecast_wdps = \
            utils.weatherdata_parse(sampledata.met_sample_weatherdata.met_sample_weatherdata['data'])

        self.location = dm.Location(latitude=60.383, longitude=5.3327)

    def test_interpolate_obs(self):

        print("Observations")
        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=self.location,
            data=list())

        wd = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        start_time, time_interpolated_sec, temp_interpolated, humidity_interpolated, wind_interpolated, max_time_delta \
        = pp.preprocess(wd)

        for i in range(0, len(time_interpolated_sec)):
            timestamp = start_time + datetime.timedelta(seconds=time_interpolated_sec[i])
            wd_point = dm.WeatherDataPoint(temperature=temp_interpolated[i],
                                           humidity=humidity_interpolated[i],
                                           wind_speed=wind_interpolated[i],
                                           timestamp=timestamp)

            print(wd_point)

        for i in range(1, len(time_interpolated_sec)):
            timedelta = \
                time_interpolated_sec[i] - time_interpolated_sec[i-1]

            self.assertEqual(timedelta, delta_t)

    def test_interpolate_fct(self):

        print("Forecast")
        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=list())

        forecast = dm.Forecast(
            location=self.location,
            data=self.forecast_wdps)

        wd = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        start_time, time_interpolated_sec, temp_interpolated, humidity_interpolated, wind_interpolated, max_time_delta \
        = pp.preprocess(wd)

        for i in range(0, len(time_interpolated_sec)):
            timestamp = start_time + datetime.timedelta(seconds=time_interpolated_sec[i])
            wd_point = dm.WeatherDataPoint(temperature=temp_interpolated[i],
                                           humidity=humidity_interpolated[i],
                                           wind_speed=wind_interpolated[i],
                                           timestamp=timestamp)
            print(wd_point)

        for i in range(1, len(time_interpolated_sec)):
            timedelta = \
                time_interpolated_sec[i] - time_interpolated_sec[i-1]

            self.assertEqual(timedelta, delta_t)


if __name__ == '__main__':
    unittest.main()
