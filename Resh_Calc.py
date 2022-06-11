import datetime
import ephem
import time

def resh_calc(date, lat, lng):

     # Getting day of the week from input date
     year = int((date.split('-')[0]))
     month = int((date.split('-')[1]))
     day = int((date.split('-')[2]))
     date2 = datetime.date(year, month, day)
     next_day = (date2)+datetime.timedelta(days=1)

     # making calculations
     loc = ephem.Observer()
     loc.pressure = 0
     loc.horizon = '-0:34'
     loc.lat, loc.lon = lat, lng
     loc.date = str(date+' 00:01')
     loc.date = str(date+' 23:59')
     loc.date = next_day
     next_sunrise = loc.previous_rising(ephem.Sun())
     noon = (12)
     noon = "{:02d}".format(noon)
     noon = str(noon+':00')
     loc.date = str(date+ ' '+noon)
     sunrise = loc.previous_rising(ephem.Sun())
     sunset = loc.next_setting(ephem.Sun())
     solar_noon = loc.next_transit(ephem.Sun(), start=sunrise)

    # turning times into strings
     sunrise = str(sunrise)
     sunset = str(sunset)
     solar_noon = str(solar_noon)
     next_sunrise = str(next_sunrise)

     # Formating to datetime objects
     sunrise = sunrise.replace("/", '-')
     sunrise1, sunrise2 = sunrise.split(" ")
     sunrise1 = (sunrise1+'T'+sunrise2)
     sunrise_time = datetime.datetime.strptime(
         sunrise1, '%Y-%m-%dT%H:%M:%S')

     sunset = sunset.replace("/", '-')
     sunset1, sunset2 = sunset.split(" ")
     sunset1 = (sunset1+'T'+sunset2)
     sunset_time = datetime.datetime.strptime(sunset1, '%Y-%m-%dT%H:%M:%S')

     next_sunrise = next_sunrise.replace("/", '-')
     next_sunrise1, next_sunrise2 = next_sunrise.split(" ")
     next_sunrise1 = (next_sunrise1+'T'+next_sunrise2)

     solar_noon = solar_noon.replace("/", '-')
     solar_noon1, solar_noon2 = solar_noon.split(" ")
     solar_noon1 = (solar_noon1+'T'+solar_noon2)
     solar_noon_time = datetime.datetime.strptime(
     solar_noon1, '%Y-%m-%dT%H:%M:%S')


     #Checking to see if sunset was in previous day UTC time, if so, addinging a day
     if sunset_time < sunrise_time:
         sunset_time = (sunset_time)+datetime.timedelta(days=1)

     else:
         pass

     # Calculating day length and solar hour
     day_length = sunset_time-sunrise_time
     # day length is a timedelta, so making it into seconds
     total_sec= day_length.total_seconds()
     day_length = str(day_length)

    # Calculating night length and lunar hour
     night_length = round(86400 - total_sec)
     lunar_half = float(night_length/2/60)
     night_length = time.strftime('%H:%M:%S', time.gmtime(night_length))
     night_length = str(night_length)

     lunar_half_time = datetime.timedelta(minutes=lunar_half)
     lunar_midnight = (sunset_time + lunar_half_time)

     # Adjusting solar times to strings
     sunrise_time = str(sunrise_time)
     sunset_time = str(sunset_time)
     solar_noon_time = str(solar_noon_time)
     lunar_midnight_time = str(lunar_midnight)

     results2 = (sunrise_time[11:19], solar_noon_time[11:19], sunset_time[11:19], lunar_midnight_time[11:19])
     print(results2)

     return results2
