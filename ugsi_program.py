#UGSI Project
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
from Phidget22.Devices.Magnetometer import *
from Phidget22.Devices.Spatial import *
import traceback
import math
import time

#Create output file, Global variable and not the best practice but will make it easier
f = open("Phidget_Output.txt","w+")

count = 0
count1 = 0

#Declare any event handlers here. These will be called every time the associated event occurs.
def onSpatial0_SpatialData(self, acceleration, angularRate, magneticField, timestamp):
    global count1
    if (timestamp - count1) < 10000:
        return 0
    else:
        count1 = timestamp;
        f.write("Acceleration (m/s²): \tX: "+ str(round((acceleration[0] * 9.81), 2)) + "  |  Y: " + str(round((acceleration[1] * 9.81), 2)) +
                "  |  Z: "+ str(round((acceleration[2] * 9.81), 2)) +"\n")
        f.write("AngularRate (°/s): \tX: "+ str(round(angularRate[0],2))+ "  |  Y: "+ str(round(angularRate[1], 2)) + "  |  Z: " +
                str(round(angularRate[2], 2)) +"\n")
        return 0

    
def onAlgo(self, quaternion, timestamp):
    global count
    if (timestamp - count) < 10000:
        return 0
    else:
        count = timestamp
        roll = math.atan2(2.0 * (quaternion[1] * quaternion[0] + quaternion[2] * quaternion[3]), 1 - 2.0 * (quaternion[1] * quaternion[1] + quaternion[2] * quaternion[2]));
        #Convert radians to degrees
        roll = roll * 180 / math.pi
        f.write("Roll (°): \t"+ str(round(roll,2)) + "\n")
        f.write("Timestamp (s): " + str(timestamp/1000)+"\n")
        f.write("----------\n")
        return 0

def onSpatial0_Attach(self):
    print("Attach!")

def onSpatial0_Detach(self):
    print("Detach!")

def onSpatial0_Error(self, code, description):
    f.write("\nCode: " + ErrorEventCode.getName(code))
    f.write("Description: " + str(description))
    f.write("----------")

def main():
    try:
        #Create your Phidget channels

        spatial0 = Spatial()

        #Assign any event handlers you need before calling open so that no events are missed.
        
        spatial0.setOnSpatialDataHandler(onSpatial0_SpatialData)
        spatial0.setOnAlgorithmDataHandler(onAlgo)
        spatial0.setOnAttachHandler(onSpatial0_Attach)
        spatial0.setOnDetachHandler(onSpatial0_Detach)
        spatial0.setOnErrorHandler(onSpatial0_Error)

        #Open your Phidgets and wait for attachment
        spatial0.openWaitForAttachment(5000)
        spatial0.setDataInterval(1000)
        spatial0.zeroAlgorithm()
        spatial0.zeroGyro()
        
        #Do stuff with your Phidgets here or in your event handlers.
        try:
            input("Press Enter to Stop\n")           
        except (Exception, KeyboardInterrupt):
            pass

        #Close your Phidgets once the program is done.
        f.close() # close file 
        spatial0.close()

    except PhidgetException as ex:
        #We will catch Phidget Exceptions here, and print the error informaiton.
        traceback.print_exc()
        print("")
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()
