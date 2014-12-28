#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

## Erwin Nindl, 2014

import ephem
from datetime import datetime
import sys

# ephem works with UTC
utc_time = datetime.utcnow()
now = ephem.Date( utc_time.strftime("%Y/%m/%d %H:%M:%S") )

#Make an observer
fred      = ephem.Observer()
fred.date = utc_time.strftime("%Y/%m/%d 12:00:00")
fred.lon  = str(12.41335)
fred.lat  = str(47.28991)
fred.elev = 950

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
