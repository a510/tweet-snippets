import asyncio

async def call_tool():
    for step in range(3):
        try:
            await asyncio.sleep(1)
        except Exception:          # change to BaseException to swallow the cancel
            print("caught")
        print(f"step {step} done")

async def main():
    try:
        async with asyncio.timeout(1.5):
            await call_tool()
        print("finished")
    except TimeoutError:
        print("timed out")

asyncio.run(main())
