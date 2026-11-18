import asyncio

async def save(item):
    print(f"saving {item}")
    await asyncio.sleep(1)
    print(f"saved {item}")

async def main():
    save("a")                              # never runs: only a RuntimeWarning
    await save("b")                        # runs now
    t = asyncio.create_task(save("c"))     # starts at main's next await
    print("main keeps going")
    await t

asyncio.run(main())
