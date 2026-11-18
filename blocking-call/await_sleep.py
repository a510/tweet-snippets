import asyncio, time

async def heartbeat():
    for i in range(4):
        print(f"beat {i}")
        await asyncio.sleep(0.5)

async def handler():
    await asyncio.sleep(1.5)  # gives the loop back: beats keep going
    print("handler done")

async def main():
    start = time.perf_counter()
    await asyncio.gather(
        heartbeat(), handler())
    print(f"total {time.perf_counter() - start:.1f} s")

asyncio.run(main())
