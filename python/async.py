"""
Most languages have capability for async, at it's most basic level it is just registering with the os to "wake up" your program when your i/o is ready.

The only difference is that python is interpreted which obfuscates a bit how it's implemented, specifically awaitables, iterators, and yields. 

For a given async framework that provides an event-loop implementation, the functions they provide i.e. get() or file reads register thsoe sockets w/ the event loop.
"""

import asyncio
import aiohttp

async def example():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/json') as response:
            data = await response.json()
            print(f"Status: {response.status}")
            print(f"Data: {data}")
            return data
        
asyncio.run(example())