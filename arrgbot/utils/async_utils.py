# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
import asyncio
import functools


def run_in_executor(_func):

    @functools.wraps(_func)
    def wrapped(*args, **kwargs):
        loop = asyncio.get_event_loop()
        func = functools.partial(_func, *args, **kwargs)
        return loop.run_in_executor(executor=None, func=func)

    return wrapped
