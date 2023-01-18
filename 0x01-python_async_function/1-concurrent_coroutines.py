#!/usr/bin/env python3
"""concurrent coroutine"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of all the delays"""
    tasks = []

    for i in range(n):
        task.append(asyncio.create_task(wait_random(max_delay)))

    return [await task for task in asyncio.as_completed(tasks)]
