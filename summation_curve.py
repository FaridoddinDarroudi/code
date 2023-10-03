import matplotlib.pyplot as plt
import math

class SummationCurve:
    # The main point of this class is to calculate T-hr unit hydrograph
    # from D-hr unit hydrograph using Time, Discharges, rainfall_duration_D
    # and rainfall_duration_T. The final result of this class is a T_UH graph
    # and a figure having T_UH, S-Curve and Lagged-S-Curve graphs for better
    # understandig of the hydrograph.

    def __init__(self, D_UH:list, rainfall_duration_D:int, rainfall_duration_T:int):
        # D_UH --> D-hr Unit Hydrograph : list of tuples
        self.D_UH = D_UH     # [(time1(hr), discharge1(m^3/s)), (time2(hr),discharge2(m^3/s)), ...]
        self.rainfall_duration_D = rainfall_duration_D      # hr
        self.rainfall_duration_T = rainfall_duration_T      # hr

    # Seprate the times in a list from D_UH list
    def get_time_list(self):
        time_tuple, discharge_tuple = zip(*self.D_UH)
        time_list = list(time_tuple)
        return time_list

    # Seprate the discharges in a list from D_UH list
    def get_discharge_list(self):
        time_tuple, discharge_tuple = zip(*self.D_UH)
        discharge_list = list(discharge_tuple)
        return discharge_list

    # shift number (which is used in below methods) is the number of rows
    # we should go down when it's needed to calculate lagged discharges.

    # Calculate shift number according to D hr hydrograph
    # (It'll be used to calculate s-hydrograph)
    def get_shift_number_D(self):
        time_list = self.get_time_list()
        d = math.ceil(self.rainfall_duration_D / (time_list[1] - time_list[0]))
        return d

    # Calculate shift number according to T hr rainfall
    # (It'll be used to calculate lagged s-hydrograph)
    def get_shift_number_T(self):
        time_list = self.get_time_list()
        t = math.ceil(self.rainfall_duration_T / (time_list[1] - time_list[0]))
        return t

    # Calculates the S-Hydrograph by summation of shifted D_UHs and D_UH itself.
    def get_s_hydrograph(self):
        D_UH = self.D_UH
        time_list = self.get_time_list()
        discharge_list= self.get_discharge_list()
        shift_number_D = self.get_shift_number_D()
        # Setting the number of times needed to shift D_UH
        n = int(len(D_UH)/shift_number_D - 1)
        # Gather D_UH and lagged D_UHs in one list
        all_discharge_lists = [discharge_list]     # Will be list of lists
        for i in range(1, n + 1):
            lagged_discharge_list = []
            lagged_discharge_list[:i*shift_number_D] = [0 for j in range(i*shift_number_D)]
            lagged_discharge_list[i*shift_number_D:] = discharge_list[:-i*shift_number_D]
            all_discharge_lists.append(lagged_discharge_list)
        # Calculate the summation of all discharge lists which has the same index
        # EX) assume all_discharge_list be like -> [[D11,D12,D13], [D21, D22, D23], ...]
        # Then summation_list be like -> [D11+D21, D12+D22, D13+D23, ...]
        summation_list = list(map(sum,zip(*all_discharge_lists)))
        return summation_list

    # Calculates the lagged_s_hydrograph
    def get_lagged_s_hydrograph(self):
        s_hydrograph = self.get_s_hydrograph()
        shift_number_T = self.get_shift_number_T()
        lagged_s_hydrograph = []
        lagged_s_hydrograph[:shift_number_T] = [0 for j in range(shift_number_T)]
        # It should be noted that the s_hydrograph should be shifted with
        # shift_number_T not shift_number_D to turn into lagged_s_hydrograph.
        lagged_s_hydrograph[shift_number_T:] = self.get_s_hydrograph()[:-shift_number_T]
        return lagged_s_hydrograph

    # Calculates the difference of s_hydrograph and lagged_s_hydrograph
    def get_diff(self):
        diff = [int(self.get_s_hydrograph()[i]) - int(self.get_lagged_s_hydrograph()[i])
                for i in range(len(self.get_s_hydrograph()))]
        return diff

    # Calculates the T hr Unit hydrograph
    def get_T_UH(self):
        T_UH = [float(self.get_diff()[j]*self.rainfall_duration_D/self.rainfall_duration_T)
                for j in range(len(self.D_UH))]
        # Calculations are in a way that the final discharge which is 0
        # is not considered so we add it to the list like below.
        # T_UH.append(0)

        return T_UH

    # plot the T_UH graph
    def plot_the_graph(self):
        time_list = self.get_time_list()
        discharges = self.get_T_UH()
        # Setting the coordinates
        x = time_list
        y = discharges

        # Plot the graph
        plt.plot(x, y)
        # setting the labels
        plt.xlabel('Time(hr)')
        plt.ylabel('Discharge(m^3/s)')
        # setting the title
        plt.title(f'{self.rainfall_duration_T}-hr Unit Hydrograph')
        # show the graph
        plt.show()

        time_list = self.get_time_list()
        x = time_list
        y1 = self.get_T_UH()
        y2 = self.get_s_hydrograph()
        y3 = self.get_lagged_s_hydrograph()

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.plot(x, y1, label=f'{self.rainfall_duration_T}-hr UH')
        ax.plot(x, y2, label='S-Curve')
        ax.plot(x, y3, label='Lagged-S-Curve')
        ax.legend(loc=0)
        plt.show()

    def run(self):
        self.plot_the_graph()
