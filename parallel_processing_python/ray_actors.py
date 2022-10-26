import ray
import time 

#We can declare python classes with the ray.remote When the class is initiated, Ray creates a new "actor"
# which is a process that runs somewhere on the cluster and holds a copy of the object

