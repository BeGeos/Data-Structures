import time
import sys
import matplotlib.pyplot as plt
import timeit

""" This is a simple attemp to verify various data structures, namely dictionaries, lists and tuples.
    The functions are in charge of inserting the data. The method timeit is native python that allows to get 
    time in second for a specified action, called statement. In addition, the size of the structures are also 
    taken into consideration. Finally, plots show important stats about the time of creation, insertion and size.
    I find a good visible way to confront the various application of data structures. """

# Populate a dictionary
def create_dictionary(n):
    dictionary = {}
    for i in range(n):
        dictionary[i] = 1
    return dictionary


# Populate a list
def create_list(n):
    generic_list = []
    for i in range(n):
        generic_list.append(i)
    return generic_list


# Populate a tuple
def create_tuple(n):
    generic_tuple = ()
    for i in range(n):
        i = (i,)
        generic_tuple += i
    return generic_tuple


dictionary_for_dict = {}
dictionary_for_list = {}
dictionary_for_tuple = {}

# Insert the data, the timed part is only the execution of the functions. Changing the parameters allows
# more flexibility. In this case the first loop dictates the number of items to create, the parameter
# inside the function the items are populated by 100 elements, namely number from 0 to 100.
# Ex: First iteration in lists creates 10 lists of 100 elements each.

for inst in range(10, 1001, 10):
    start_dict_time = time.time()
    for d in range(inst):
        action = create_dictionary(101)
    end_dict_time = time.time()
    delta_time_dict = end_dict_time - start_dict_time
    dictionary_for_dict[inst] = delta_time_dict
size_dict = sys.getsizeof(action)

for inst in range(10, 1001, 10):
    start_list_time = time.time()
    for d in range(inst):
        action = create_list(101)
    end_list_time = time.time()
    delta_time_dict = end_list_time - start_list_time
    dictionary_for_list[inst] = delta_time_dict
size_list = sys.getsizeof(action)


for inst in range(10, 1001, 10):
    start_tuple_time = time.time()
    for d in range(inst):
        action = create_tuple(101)
    end_tuple_time = time.time()
    delta_time_dict = end_tuple_time - start_tuple_time
    dictionary_for_tuple[inst] = delta_time_dict
size_tuple = sys.getsizeof(action)

# Timeit function to get the runtime of creation
data_dict = sorted(dictionary_for_dict.items())
x, y = zip(*data_dict)

data_list = sorted(dictionary_for_list.items())
w, z = zip(*data_list)

data_tuple = sorted(dictionary_for_tuple.items())
s, t = zip(*data_tuple)


dict_test = timeit.timeit(stmt='{1:1, 2:1, 3:1, 4:1, 5:1}', number=1000)
list_test = timeit.timeit(stmt='[1,2,3,4,5]', number=1000)
tuple_test = timeit.timeit(stmt='(1,2,3,4,5)', number=1000)

# Create 3 plots
figure = plt.figure(figsize=(21, 8))

plt.subplot(131)
plt.plot(x, y, label='Dictionary')
plt.plot(w, z, label='List')
plt.plot(s, t, label='Tuple')
plt.xlabel('Number of items')
plt.ylabel('time in sec')
plt.title('Inserting Data')
plt.legend()
plt.subplot(132)
plt.bar('Dictionary', size_dict, label='Dictionary')
plt.bar('List', size_list, label='List')
plt.bar('Tuple', size_tuple, label='Tuple')
plt.ylabel('bytes')
plt.title('Size')
plt.subplot(133)
plt.bar('Dictionary', dict_test)
plt.bar('List', list_test)
plt.bar('Tuple', tuple_test)
plt.ylabel('time in sec')
plt.suptitle("Data Structures")
plt.title('Creating Structures')
figure.tight_layout(pad=4.0)
plt.show()
