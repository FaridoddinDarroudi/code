from snyder import Snyder

# If it is needed to take input from the user and
# not setting the values down below, comment lines
# between 9-16 and uncomment line 18.
# The first example is from Ex 9-15 Alizade book.

# You can set variables below
watershed_area = 193    # Mile^2
channel_length = 15.53      # Mile
length_to_centroid_of_basin = 4.35      # Mile
ct = 2      # Constant
cp = 0.6      # Constant

s_obj = Snyder(watershed_area, channel_length, length_to_centroid_of_basin, ct, cp)
s_obj.run()

# Snyder.run()

# There is one more example down below:

# Ex 10-15 Alizade book
# watershed_area = 10.73    # Mile^2
# channel_length = 57.14      # Mile
# length_to_centroid_of_basin = 29.34      # Mile
# ct = 2      # Constant
# cp = 0.6      # Constant
