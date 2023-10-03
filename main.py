from summation_curve import SummationCurve

# You can set variables below
# D_UH -> [(time1(hr), discharge1(m^3/s)), (time2(hr),discharge2(m^3/s)), ...]
D_unit_hydrograph = [(0, 0), (1, 5), (2, 18), (3, 35.2), (4, 54), (5, 67.8), (6, 72.9),
                     (7, 72.4), (8, 68.9), (9, 62.9), (10, 56.4), (11, 49.7), (12, 43.2), (13, 37.1),
                     (14, 31.4), (15, 26.3), (16, 22), (17, 18.3), (18, 15.4), (19, 13), (20, 10.7),
                     (21, 8.8), (22, 7.2), (23, 5.9), (24, 4.8), (25, 3.8), (26, 2.9), (27, 2.1),
                     (28, 1.4), (29, 0.8), (30, 0.4), (31, 0.2), (32, 0)]
rainfall_duration_D = 4
rainfall_duration_T = 5

s_obj = SummationCurve(D_unit_hydrograph, rainfall_duration_D, rainfall_duration_T)
print('T-hr unit hydrograph: ' + str(s_obj.get_T_UH()))
s_obj.run()

# More examples:
# You can replace the above data with the data represented in below examples.
# You can also change rainfall_duration_D and rainfall_duration_T for more tests.

# EX)
# D_unit_hydrograph = [(0, 0), (1, 5), (2, 18), (3, 35.2), (4, 54), (5, 67.8), (6, 72.9),
#                      (7, 72.4), (8, 68.9), (9, 62.9), (10, 56.4), (11, 49.7), (12, 43.2), (13, 37.1),
#                      (14, 31.4), (15, 26.3), (16, 22), (17, 18.3), (18, 15.4), (19, 13), (20, 10.7),
#                      (21, 8.8), (22, 7.2), (23, 5.9), (24, 4.8), (25, 3.8), (26, 2.9), (27, 2.1),
#                      (28, 1.4), (29, 0.8), (30, 0.4), (31, 0.2), (32, 0)]
# rainfall_duration_D = 4
# rainfall_duration_T = 3

# EX)
# D_unit_hydrograph = [(0, 0), (3, 200), (6, 500), (9, 1000), (12, 1600), (15, 2400), (18, 3500),
#                      (21, 4200), (24, 5200), (27, 4400), (30, 3100), (33, 2300), (36, 1500),
#                      (39, 1000), (42, 650), (45, 400), (48, 250), (51, 150), (54, 0)]
# rainfall_duration_D = 6
# rainfall_duration_T = 8
