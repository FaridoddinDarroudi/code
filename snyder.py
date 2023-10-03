import matplotlib.pyplot as plt

# primary note:
# This class has been written in a way that the inputs are given
# when the object is initialized, but if the case is that to take inputs
# from the user, lines between 21-87 should be uncommented and lines
# between 15-19 get commented, and paramters in __init__ should be removed.

class Snyder:
    # The main object of this class is to plot the snyder's graph
    # using the data related to physical specifications of the
    # selected area.

    def __init__(self, area:int, channel_length:int, length_to_centroid:int, ct:float, cp:float):
        self.area = area    # Mile^2
        self.channel_length = channel_length      # Mile
        self.length_to_centroid = length_to_centroid       # Mile
        self.ct = ct     # Constant
        self.cp = cp     # Constant

        # self.area = self.get_area()
        # self.channel_length = self.get_channel_length()
        # self.length_to_centroid = self.get_length_to_centroid()
        # self.ct = self.get_ct()
        # self.cp = self.get_cp()

    # # Gets the watershed area
    # def get_area(self):
    #     while True:
    #         area = input("Watershed Area: ")  # (mile^2)
    #         if area.isdigit():
    #             area = int(area)
    #             if area > 0:
    #                 break
    #             else:
    #                 print('Area must be greater than 0')
    #         else:
    #             print('Please enter a number')
    #     return area
    #
    # # Gets the channel length
    # def get_channel_length(self):
    #     while True:
    #         channel_length = input("Channel Length: ")  # (mile)
    #         if channel_length.isdigit():
    #             channel_length = int(channel_length)
    #             if channel_length > 0:
    #                 break
    #             else:
    #                 print('Channel Length must be greater than 0')
    #         else:
    #             print('Please enter a number')
    #     return channel_length
    #
    # # Gets the length to centroid of basin
    # def get_length_to_centroid(self):
    #     while True:
    #         length_to_centroid = input("Length to centroid of basin: ")  # (mile)
    #         if length_to_centroid.isdigit():
    #             length_to_centroid = int(length_to_centroid)
    #             if length_to_centroid > 0:
    #                 break
    #             else:
    #                 print('Length to centroid must be greater than 0')
    #         else:
    #             print('Please enter a number')
    #     return length_to_centroid
    #
    # # Gets the Ct constant
    # def get_ct(self):
    #     while True:
    #         ct = float(input("Ct: "))
    #         if 1.8 < ct < 2.2:
    #             break
    #         else:
    #             print('ct must be between 1.8 and 2.2')
    #     return ct
    #
    # # Gets the Cp constant
    # def get_cp(self):
    #     while True:
    #         cp = float(input("Cp: "))
    #         if 0.4 < cp < 0.8:
    #             break
    #         else:
    #             print('cp must be between 0.4 and 0.8')
    #     return cp

    # Calculates time to pick
    def calc_time_to_pick(self):
        t_lag = self.ct*pow(self.channel_length*self.length_to_centroid, 0.3)
        return t_lag

    # Calculates the duration of rainfall
    def calc_rainfall_duration(self):
        t_lag = self.calc_time_to_pick()
        d = t_lag/5.5
        return d

    # Calculates the maximum discharge
    def calc_peak_discharge(self):
        qp = 640*self.cp*self.area/self.calc_time_to_pick()
        return qp

    # Calculates the time of rise
    def calc_time_of_rise(self):
        tp = self.calc_rainfall_duration()/2 + self.calc_time_to_pick()
        return tp

    # Calculates the base time
    def calc_base_time(self):
        tb = 3 + self.calc_time_to_pick()/8     # days
        tb *= 24      # hrs
        return tb

    # Calculates the distance between two points which has 50% of peak discharge
    def calc_50th_width(self):
        w50 = 770 * pow(self.calc_peak_discharge()/self.area, -1.08)    # hrs
        return w50

    # Calculates the distance between two points which has 75% of peak discharge
    def calc_75th_width(self):
        w75 = 440 * pow(self.calc_peak_discharge() / self.area, -1.08)    # hrs
        return w75

    # Calculates the coordinates of the 2 points with 50% of peak discharge
    def calc_50ths_coordinates(self):
        x1 = self.calc_time_of_rise() - self.calc_50th_width() / 3
        x2 = self.calc_time_of_rise() + 2 * self.calc_50th_width() / 3
        y = 0.5 * self.calc_peak_discharge()
        return [(x1, y), (x2, y)]

    # Calculates the coordinates of the 2 points with 75% of peak discharge
    def calc_75ths_coordinates(self):
        x1 = self.calc_time_of_rise() - self.calc_75th_width() / 3
        x2 = self.calc_time_of_rise() + 2 * self.calc_75th_width() / 3
        y = 0.75 * self.calc_peak_discharge()
        return [(x1, y), (x2, y)]

    def plot_the_graph(self):
        # Unzipping the w50 coordinates
        x1_w50, y_w50 = self.calc_50ths_coordinates()[0]
        x2_w50 = self.calc_50ths_coordinates()[1][0]

        # Unzipping the w75 coordinates
        x1_w75, y_w75 = self.calc_75ths_coordinates()[0]
        x2_w75 = self.calc_75ths_coordinates()[1][0]

        # plotting the graph using matplotlib.pyplot

        # setting the coordinates
        x = [0, x1_w50, x1_w75, self.calc_time_of_rise(), x2_w75, x2_w50, self.calc_base_time()]
        y = [0, y_w50, y_w75, self.calc_peak_discharge(), y_w75, y_w50, 0]
        # plot the graph
        plt.plot(x, y)
        # setting the labels
        plt.xlabel('Time(hr)')
        plt.ylabel('Discharge(cfs)')
        # setting the title
        plt.title("snyder's method")
        # show the graph
        plt.show()

    def run(self):
        self.plot_the_graph()
