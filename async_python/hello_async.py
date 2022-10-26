import asyncio 

#We are defining the function as an async function 
async def main():
    print('Hello...')

    #We are telling the operation to await 
    await asyncio.sleep(1)
    print('...World!')


if __name__=='__main__': 
    asyncio.run(main())

#Resources: 
# - https://docs.python.org/3/library/asyncio-task.html