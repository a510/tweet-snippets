import asyncio

async def get_all(text):
    words = []
    for word in text.split():
        await asyncio.sleep(0.5)
        words.append(word + " ")
    return words

async def main():
    for tok in await get_all("hi from python"):
        print(tok, end="", flush=True)
    print()

asyncio.run(main())
