import asyncio, time

async def heartbeat():
    for i in range(4):
        print(f"beat {i}")
        await asyncio.sleep(0.5)

async def handler():
    time.sleep(1.5)  # blocks the loop: beats stop
    print("handler done")

async def main():
    start = time.perf_counter()
    await asyncio.gather(
        heartbeat(), handler())
    print(f"total {time.perf_counter() - start:.1f} s")

asyncio.run(main())
