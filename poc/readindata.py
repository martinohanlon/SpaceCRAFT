from collections import OrderedDict
from csv import DictReader
from time import time

#field name constants
TIME = "time"
HUMIDITY = "humidity"
PRESSURE = "pressure"
TEMP_HUMIDITY = "temperature (humidity)"
TEMP_PRESSURE = "temperature (pressure)"
ORIENTATION_RAD_PITCH = "orientation radians pitch"
ORIENTATION_RAD_YAW = "orientation radians yaw"
ORIENTATION_RAD_ROLL = "orientation radians roll"
ORIENTATION_DEG_PITCH = "orientation degrees pitch"
ORIENTATION_DEG_YAW = "orientation degrees yaw"
ORIENTATION_DEG_ROLL = "orientation degrees roll"
COMPASS_RAW_X = "compass raw x"
COMPASS_RAW_Y = "compass raw y"
COMPASS_RAW_Z = "compass raw z"
GYRO_RAW_X = "gyroscope raw x"
GYRO_RAW_Y = "gyroscope raw y"
GYRO_RAW_Z = "gyroscope raw z"
ACCEL_RAW_X = "accelerometer raw x"
ACCEL_RAW_Y = "accelerometer raw y"
ACCEL_RAW_Z = "accelerometer raw z"

"""
print("Reading file into OrderedDict")

starttime = time()

dataDict = OrderedDict()

with open("/home/pi/data/data.2015-05-13-19-33-42.csv", "r") as datafile:
    reader = DictReader(datafile)
    print(reader[0])
    for row in reader:
        dataDict[row[TIME]] = row

#for time, data in dataDict.items():
#    print("{} : {}".format(time, data))


endtime = time()

print("Completed {}".format(endtime - starttime))
"""
print("Reading file into list")

starttime = time()

datalist = []

with open("/home/pi/data/data.2015-05-13-19-33-42.csv", "r") as datafile:
    reader = DictReader(datafile)
    for row in reader:
        datalist.append(row)
print(len(datalist))
#for row in datalist:
#    temp = row[TEMP_HUMIDITY]

endtime = time()

print("Completed {}".format(endtime - starttime))
