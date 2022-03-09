import asyncio
import random


async def func(_1, _2):
    print("开始", "形参", _1)
    await asyncio.sleep(random.randint(0, 3))
    print("结束", "形参", _1)
    return f"返回：形参 {_1} 定参 {_2}"


async def main(event, context):
    ok = ""
    n = "9"
    tasks = [
        func(m, n) for m in range(3)
    ]
    success = await asyncio.wait(tasks)
    for res in success[0]:
        ok += res.result() + "\n"
    print(ok)
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("", ""))
    