import json
import time;
import asyncio

from tzlocal import get_localzone

def get_time():
    return int(time.time_ns())

def get_timezone():
    return str(get_localzone())

async def gen_event():
    try:
        count = 0
        while True:
            count += 1
            yield {
                "id": str(count),
                "data": json.dumps({
                    "timezone": get_timezone(),
                    "timestamp": get_time()
                })
            }
            await asyncio.sleep(1)
    except Exception as error:
        print(error)
    finally:
        print("Client disconnected")