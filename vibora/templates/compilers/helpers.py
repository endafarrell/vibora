from inspect import isasyncgen, isasyncgenfunction, iscoroutine


async def smart_iter(element):
    if isasyncgen(element) or isasyncgenfunction(element):
        yield from element
    else:
        yield from element
