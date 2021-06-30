#UGSI Project
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
#from Phidget22.Devices.Magnetometer import *
from Phidget22.Devices.Spatial import *
import traceback
import time

#Create output file, Global variable and not the best practice but will make it easier
f = open("Phidget_Output.txt","w+")

#Declare any event handlers here. These will be called every time the associated event occurs.

def onAccelerometer0_AccelerationChange(self, acceleration, timestamp):
    #time.sleep(5) #only need acceleration every 60 seconds
    f.write("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]) + "\n")
    f.write("Timestamp: " + str(timestamp) + "\n")
    f.write("----------"+ "\n")

def onAccelerometer0_Attach(self):
    print("Attach!")

def onAccelerometer0_Detach(self):
    print("Detach!")

def onAccelerometer0_Error(self, code, description):
    f.write("Code: " + ErrorEventCode.getName(code)+ "\n")
    f.write("Description: " + str(description)+ "\n")
    f.write("----------"+ "\n")

def onGyroscope0_AngularRateUpdate(self, angularRate, timestamp):
    #time.sleep(5) #only need acceleration every 60 seconds
    f.write("AngularRate: \t"+ str(angularRate[0])+ "  |  "+ str(angularRate[1])+ "  |  "+ str(angularRate[2])+ "\n")
    f.write("Timestamp: " + str(timestamp)+ "\n")
    f.write("----------"+ "\n")

def onGyroscope0_Attach(self):
    print("Attach!")

def onGyroscope0_Detach(self):
    print("Detach!")

def onGyroscope0_Error(self, code, description):
    f.write("Code: " + ErrorEventCode.getName(code)+ "\n")
    f.write("Description: " + str(description)+ "\n")
    f.write("----------"+ "\n")

'''
def onMagnetometer0_MagneticFieldChange(self, magneticField, timestamp):
print("MagneticField: \t"+ str(magneticField[0])+ "  |  "+ str(magneticField[1])+ "  |  "+ str(magneticField[2]))
print("Timestamp: " + str(timestamp))
print("----------")

def onMagnetometer0_Attach(self):
	print("Attach!")

def onMagnetometer0_Detach(self):
	print("Detach!")

def onMagnetometer0_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")


def onSpatial0_SpatialData(self, acceleration, angularRate, timestamp):
    time.sleep(60) #only need acceleration every 60 seconds
    f.write("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]))
    f.write("AngularRate: \t"+ str(angularRate[0])+ "  |  "+ str(angularRate[1])+ "  |  "+ str(angularRate[2]))
    #print("MagneticField: \t"+ str(magneticField[0])+ "  |  "+ str(magneticField[1])+ "  |  "+ str(magneticField[2]))
    f.write("Timestamp: " + str(timestamp))
    f.write("----------")

def onSpatial0_Attach(self):
    print("Attach!")

def onSpatial0_Detach(self):
    print("Detach!")

def onSpatial0_Error(self, code, description):
    f.write("Code: " + ErrorEventCode.getName(code))
    f.write("Description: " + str(description))
    f.write("----------")
'''

def main():
    try:
        #Create your Phidget channels
        accelerometer0 = Accelerometer()
        gyroscope0 = Gyroscope()
        '''
        magnetometer0 = Magnetometer()
        spatial0 = Spatial()
        '''

        #Set addressing parameters to specify which channel to open (if any)

        #Assign any event handlers you need before calling open so that no events are missed.
        accelerometer0.setOnAccelerationChangeHandler(onAccelerometer0_AccelerationChange,)
        accelerometer0.setOnAttachHandler(onAccelerometer0_Attach)
        accelerometer0.setOnDetachHandler(onAccelerometer0_Detach)
        accelerometer0.setOnErrorHandler(onAccelerometer0_Error)
        
        gyroscope0.setOnAngularRateUpdateHandler(onGyroscope0_AngularRateUpdate)
        gyroscope0.setOnAttachHandler(onGyroscope0_Attach)
        gyroscope0.setOnDetachHandler(onGyroscope0_Detach)
        gyroscope0.setOnErrorHandler(onGyroscope0_Error)
        '''
        magnetometer0.setOnMagneticFieldChangeHandler(onMagnetometer0_MagneticFieldChange)
        magnetometer0.setOnAttachHandler(onMagnetometer0_Attach)
        magnetometer0.setOnDetachHandler(onMagnetometer0_Detach)
        magnetometer0.setOnErrorHandler(onMagnetometer0_Error)
        
        spatial0.setOnSpatialDataHandler(onSpatial0_SpatialData)
        spatial0.setOnAttachHandler(onSpatial0_Attach)
        spatial0.setOnDetachHandler(onSpatial0_Detach)
        spatial0.setOnErrorHandler(onSpatial0_Error)
        '''

        #Open your Phidgets and wait for attachment
        accelerometer0.openWaitForAttachment(5000)
        accelerometer0.setDataInterval(60000) #Setting Interval
        gyroscope0.openWaitForAttachment(5000)
        gyroscope0.setDataInterval(60000) #Setting Interval
        
        '''
        magnetometer0.openWaitForAttachment(5000)
        spatial0.openWaitForAttachment(5000)
        '''

        #Do stuff with your Phidgets here or in your event handlers.

        try:
            input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
            pass

        #Close your Phidgets once the program is done.
        f.close() # close file 
        accelerometer0.close()
        gyroscope0.close()
        '''
        magnetometer0.close()
        spatial0.close()
        '''

    except PhidgetException as ex:
        #We will catch Phidget Exceptions here, and print the error informaiton.
        traceback.print_exc()
        print("")
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()
