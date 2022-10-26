import ray 
import time 

# Start ray 
ray.init()

#Turn function f into a remote function that can 
# be executed remotely and asynchronously

@ray.remote
def f(x):
    time.sleep(1)
    return x

#Start 4 tasks in parallel 
result_ids = []

for i in range(4): 
    result_ids.append(f.remote(i))

#Wait for the tasks to complete and retrieve the results 
results = ray.get(result_ids) 
print(results)

## Resource: https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8
