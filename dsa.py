import asyncio
import time

counter = 0
lock = asyncio.Lock()

async def do_some_task(id, delay):
    global counter
    async with lock:
        print(f"Performing task {id} with delay of {delay} after this...")
        await asyncio.sleep(delay)
        print(f"Performed task {id} after delay of {delay}")
        return {"data": id}


async def main():
    start_time = time.time()

    tasks = []
    async with asyncio.TaskGroup() as tg:
        tasks.append(tg.create_task(do_some_task(1, 2)))
        tasks.append(tg.create_task(do_some_task(2, 2)))

    results = [task.result() for task in tasks]
    print(results)

    print(f"Total time taken: {time.time()-start_time}")



asyncio.run(main())
"""
Performing task 1 with delay of 2 after this...
Performed task 1 after delay of 2
Performing task 2 with delay of 2 after this...
Performed task 2 after delay of 2
[{'data': 1}, {'data': 2}]
Total time taken: 4.0154571533203125
"""