import asyncio
import aiohttp
import time
async def main():
  start = time.time()
  async with aiohttp.ClientSession() as session:
    t1 = asyncio.create_task(session.get('https://www.kingname.info/2020/03/23/why-default-aiohttp-slow/'))
    t2 = asyncio.create_task(session.get('https://www.kingname.info/2020/03/23/why-default-aiohttp-slow/'))
    await t1
    await t2
    print(f'task1: {t1}')
    end = time.time()
    print(f'{end - start} seconds')


asyncio.run(main())
