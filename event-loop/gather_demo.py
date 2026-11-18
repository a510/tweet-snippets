import asyncio

async def fetch(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} done")
    return name

async def main():
    results = await asyncio.gather(
        fetch("A", 2), fetch("B", 1))
    print(results)

asyncio.run(main())
