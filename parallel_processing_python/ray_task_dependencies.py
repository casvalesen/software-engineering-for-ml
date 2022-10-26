import ray 
import numpy as np
import time  

# Ray tasks can depend on other tasks.
# since Multiply matricies depends on two instances of create_matrix, it will not
#Start to execute until these are finished

#Start ray
ray.init()

@ray.remote
def create_matrix(size):
    print(f'Executing matrix creation at time {time.strftime("%X")}')
    return np.random.normal(size=size)

@ray.remote
def multiply_matricies(x,y):
    print(f'Executing multiply at time {time.strftime("%X")}')
    return np.dot(x,y)

x_id = create_matrix.remote([1000,1000])
y_id = create_matrix.remote([1000, 1000])

z_id = multiply_matricies.remote(x_id, y_id)

z = ray.get(z_id)