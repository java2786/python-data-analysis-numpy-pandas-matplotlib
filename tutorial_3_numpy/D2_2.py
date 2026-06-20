import numpy as np

std1_marks = [78,81,92,83] # Ramesh
std2_marks = [78,82,81,63] # Suresh
std3_marks = [78,61,72,81] # Dinesh
np_marks = np.array([std1_marks, std2_marks, std3_marks])

# np_marks = np.array([
#     [78,81,92,83],
#     [87,82,82,63],
#     [68,61,72,81]
# ])


print(np_marks)
print(np_marks.shape)



print(f"3rd marks of Suresh: {np_marks[1,2]}")
print(f"All marks of Suresh: {np_marks[1,:]}")
print(f"All marks of Hindi subject (first column): {np_marks[:,0]}")


print("\n\n+++++++++++++++++++++++\n\n")

print("Studens' Report")
print(f"Subject Average: {np.mean(np_marks, axis=0)}") # column
print(f"Student Average: {np.mean(np_marks, axis=1)}") # row


