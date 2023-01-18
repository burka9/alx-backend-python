#!/usr/bin/env python3
"""async syntax"""
import random
import asyncio


async def wait_random(max_delay: int = 0) -> float:
    """waits for random delay between 0 and max_delay"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return rand
