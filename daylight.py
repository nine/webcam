#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

## Erwin Nindl, 2014

import argparse
import ephem
from datetime import datetime
import sys


# parse arguments
parser = argparse.ArgumentParser(prog="daylight", description='Estimate the presence of daylight')
parser.add_argument('--lon', type=float, dest='lon', required=True, help='position longitude')
parser.add_argument('--lat', type=float, dest='lat', required=True, help='position latitude')
parser.add_argument('--ele', type=int, dest='ele', required=True, help='elevation')
options = parser.parse_args()


# ephem works with UTC
utc_time = datetime.utcnow()
now = ephem.Date( utc_time.strftime("%Y/%m/%d %H:%M:%S") )

#Make an observer
fred      = ephem.Observer()
fred.date = utc_time.strftime("%Y/%m/%d 12:00:00")
fred.lon  = str(options.lon)
fred.lat  = str(options.lat)
fred.elev = options.ele

sunrise = fred.previous_rising( ephem.Sun() ) #Sunrise
noon    = fred.next_transit( ephem.Sun(), start=sunrise ) #Solar noon
sunset  = fred.next_setting( ephem.Sun() ) #Sunset

#We relocate the horizon to get twilight times
fred.horizon = '-12' #-6=civil twilight, -12=nautical, -18=astronomical
beg_twilight = fred.previous_rising( ephem.Sun(), use_center=True ) #Begin twilight
end_twilight = fred.next_setting( ephem.Sun(), use_center=True ) #End twilight

if now>beg_twilight and now<end_twilight:
  sys.exit(0)
else:
  sys.exit(1)

#eof
