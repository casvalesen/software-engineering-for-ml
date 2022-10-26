import ray
import time 

#We can declare python classes with the ray.remote When the class is initiated, Ray creates a new "actor"
# which is a process that runs somewhere on the cluster and holds a copy of the object

@ray.remote 
class Counter(object):
    def __init__(self):
        self.x = 0 

    def inc(self): 
        self.x +=1 

    def get_value(self):
        return self.x

def main(): 
    # Create an actor process
    c = Counter.remote()

    #Check the actors counter valute 
    print(ray.get(c.get_value.remote()))

    #Increment the counter twice
    c.inc.remote()
    c.inc.remote()
    print(ray.get(c.get_value.remote()))

if __name__=='__main__': 
    main()