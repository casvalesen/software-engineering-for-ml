import ray 
import time 


# Define a remote actor class 
@ray.remote
class MessageActor(object): 
    def __init__(self): 
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_and_clear_messages(self): 
        messages = self.messages
        self.messages = [] 
        return messages 

#Define a rempte function which loops around and pushes messages to the actor 
@ray.remote
def worker(message_actor, j ):
    for i in range(100):
        time.sleep(1)
        message_actor.add_message.remote(f'Message from worker {i} , {j}')

def main(): 
    
    #Create a message actor 
    message_actor = MessageActor.remote()

    #Start 3 tasks that push messages to the actor 
    [worker.remote(message_actor, j) for j in range(3)]


    #Periodically get messages and print 
    for _ in range(100): 
        new_messages = ray.get(message_actor.get_and_clear_messages.remote())
        print(f'New messages {new_messages}')
        time.sleep(1)

if __name__=="__main__":
    main()