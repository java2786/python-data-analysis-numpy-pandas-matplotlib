"""
Ramesh - data analyst

delivery times (hours)
find total items to deliver
find average time
max time
which delivery took more than 5 hours
due to traffic, adjust delivery time - increase by half 
"""

import numpy

delivery_times = [3, 7, 2, 8, 2, 4, 8, 6]
np_array = numpy.array(delivery_times)

print(np_array)
print(type(delivery_times))
print(type(np_array))

print(np_array.dtype)
print(np_array.shape)


total_time = numpy.sum(np_array)
print(f"Total time: {total_time}")

avg_time = numpy.mean(np_array)
print(f"Average time: {avg_time}")

max_time = numpy.max(np_array)
print(f"Max time: {max_time}")

print(np_array>5)
print(np_array[np_array>5])

print(np_array * 1.5)