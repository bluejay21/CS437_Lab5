import matplotlib.pyplot as plt
import numpy as np
    
class Zebra_Data:
    # --------------------------------------------------------------------
    # Functions:

    def addData(self, input_file_string):
        fString = input_file_string
        contents = fString.split()
    
        if len(contents) > 0:
            dataType = contents[0]
            contentData = contents[1]

            if "location" in dataType:
                self.addLocation(contentData)
            elif "oxygen_saturation" in dataType:
                self.addOxygenSaturation(contentData.replace(",", ""))
            elif "temperature" in dataType:
                self.addTempurature(contentData)
            elif "air_quality" in dataType:
                self.addAirQual(contentData)
            elif "humidity" in dataType:
                self.addHumidity(contentData)
        
            if len(contents) >= 4:
                if "heart_rate" in contents[2]:
                    self.addHeartRate(contents[3])
        

    # Append Functions
    
    def addLocation(self, input_location):
        appLocation = input_location
        self.addXLocation(input_location)
        self.addYLocation(input_location)
        self.addSpeed()
        self.m_location.append(appLocation)

    def addXLocation(self, input_X):
        appX = self.get_XCoordinate(input_X)
        self.m_xCoordinates.append(appX)
    
    def addYLocation(self, input_Y):
        appY = self.get_YCoordinate(input_Y)
        self.m_yCoordinates.append(appY)

    def addSpeed(self):
        lastIndex = len(self.m_xCoordinates)-1

        if lastIndex > 0:
            x2 = float(self.m_xCoordinates[lastIndex])
            x1 = float(self.m_xCoordinates[lastIndex-1])
            y2 = float(self.m_yCoordinates[lastIndex])
            y1 = float(self.m_yCoordinates[lastIndex-1])
            time = 1

            vx = ((x2-x1) / time)
            vy = ((y2-y1) / time)
            speed = ((vx**2)+(vy**2))**(1/2)

            self.m_speed.append(speed)
        
    
    def addOxygenSaturation(self, input_saturation):
        appOxSat = input_saturation
        self.m_oxygen_saturation.append(appOxSat)

    def addHeartRate(self, input_hr):
        appHR = input_hr
        self.m_heart_rate.append(appHR)

    def addTempurature(self, input_temp):
        appTemp = input_temp
        self.m_temperature.append(appTemp)

    def addAirQual(self, input_quality):
        appQuality = input_quality
        self.m_air_quality.append(appQuality)
    
    def addHumidity(self, input_humidity):
        appHumidity = input_humidity
        self.m_humidity.append(appHumidity)




    # Getter Functions

    def getLocation(self):
        return self.m_location
    
    def get_xCoordinates(self):
        return self.m_xCoordinates
    
    def get_yCoordinates(self):
        return self.m_yCoordinates

    def get_speed(self):
        return self.m_speed

    def getOxygenSaturation(self):
        return self.m_oxygen_saturation

    def getHeartRate(self):
        return self.m_heart_rate

    def getTemperature(self):
        return self.m_temperature

    def getAirQuality(self):
        return self.m_air_quality
    
    def getHumidity(self):
        return self.m_humidity
    


    # helper functions

    def get_XCoordinate(self, gps_str):
        split_gps = gps_str.split(",")
        split_gps_X = split_gps[0]
    
        xCoordinate = split_gps_X.replace("[", "")
        return xCoordinate
    

    def get_YCoordinate(self, gps_str):
        split_gps = gps_str.split(",")
        split_gps_Y = split_gps[1]
    
        yCoordinate = split_gps_Y.replace("]", "")
        return yCoordinate


    def generate_CDF(self):
        count, bins_count = np.histogram(self.get_speed())
        print(count)
        pdf = count / sum(count)

        cdf = np.cumsum(pdf)
        return cdf

    
    

    



    
    # --------------------------------------------------------------------
    # Member Variables:

    m_location = []
    m_xCoordinates = []
    m_yCoordinates = []
    m_speed = []
    m_oxygen_saturation = []
    m_heart_rate = []
    m_temperature = []
    m_air_quality = []
    m_humidity = []






if __name__ == "__main__":

    zebraFiles = []
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra1.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra2.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra3.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra4.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra5.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra6.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra7.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data/Zebra8.txt")
    zebraFiles.append("/Users/jacobriese/Documents/CS_437/Lab5/Zebra_Data_5_1_23/Lion1.txt")

    zebraDataList = []

    for filename in zebraFiles:

        file_in_use = open(filename, 'r')
        lines = file_in_use.readlines()
        file_in_use.close()
        zebraData = Zebra_Data()

        for line in lines:
            zebraData.addData(line)

        zebraDataList.append(zebraData)
    
    allHeartRates = []
    allOxySat = []
    allAirQual = []
    for zebras in zebraDataList:
        allHeartRates = allHeartRates + zebras.getHeartRate()
        allOxySat = allOxySat + zebras.getOxygenSaturation()
        allAirQual = allAirQual + zebras.getAirQuality()

    

    Temperature_Zebra1 = np.array(zebraDataList[0].getTemperature())
    HeartRate_Zebra1 = np.array(zebraDataList[4].getHeartRate())
    # plt.hist(allAirQual)
    X = zebraDataList[7].get_xCoordinates()
    Y = zebraDataList[7].get_yCoordinates()

    # plt.scatter(np.asarray(X, float), np.asarray(Y, float))
    # plt.show()

    plt.hist(zebraDataList[0].get_speed())
    plt.show()


    zebraDataList[0].get_speed()
    zebraAve = np.average(zebraDataList[0].get_speed())
    lionAve = np.average(zebraDataList[8].get_speed())

    print(zebraAve)
    print(lionAve)


    # zebraDataList[0].generate_CDF()