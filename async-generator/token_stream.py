import asyncio

async def token_stream(text):
    for word in text.split():
        await asyncio.sleep(0.5)
        yield word + " "

async def main():
    stream = token_stream("hi from python")
    async for tok in stream:
        print(tok, end="", flush=True)
    print()

asyncio.run(main())
