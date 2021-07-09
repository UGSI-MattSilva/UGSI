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

count = 2

#Declare any event handlers here. These will be called every time the associated event occurs.
def onSpatial0_SpatialData(self, acceleration, angularRate, magneticField, timestamp):
    global count
    global f
    if count < 3:

        time.sleep(10)
        count += 1
    else:
        count -= 1
        f.write("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2])+"\n")
        f.write("AngularRate: \t"+ str(angularRate[0])+ "  |  "+ str(angularRate[1])+ "  |  "+ str(angularRate[2])+"\n")
        f.write("Timestamp: " + str(timestamp)+"\n")
        f.write("----------\n")
        print(acceleration[0])
    
def onAlgo(self, quaternion, timestamp):
    test = 0

def onSpatial0_Attach(self):
    print("Attach!")

def onSpatial0_Detach(self):
    print("Detach!")

def onSpatial0_Error(self, code, description):
    global f
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
