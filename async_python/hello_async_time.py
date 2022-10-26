import asyncio 
import time 

async def say_after(delay, what): 
    await asyncio.sleep(delay)
    print(what)

async def main():

    print(f'started at {time.strftime("%X")}')

    await say_after(1, 'hello')
    await say_after(2,'World')

    #We can see that the task finishes after delay + delay seconds
    print(f'Finished at {time.strftime("%X")}')

if __name__=='__main__':
    asyncio.run(main())



#Resources:
# - https://docs.python.org/3/library/asyncio-task.html
# - https://www.geeksforgeeks.org/time-strftime-function-in-python/

