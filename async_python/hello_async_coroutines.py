import asyncio 
import time 
import aiohttp

#hello_async_time.py has been modifid to run coroutines concurretly as asyncio Tasks
async def say_after(delay, what): 
    await asyncio.sleep(delay)
    print(what)

async def main(): 
    task1 = asyncio.create_task(
        say_after(3, 'hello'))
    
    task2 = asyncio.create_task(
        say_after(1, 'world'))
    
    print(f'Started at {time.strftime("%X")}')

    #Wati until both tasks are completed (should take around 2 seconds))
    await task1
    await task2

    print(f'finished at {time.strftime("%X")}')

if __name__=='__main__': 
    asyncio.run(main())


#Resources: 
# - https://docs.python.org/3/library/asyncio-task.html