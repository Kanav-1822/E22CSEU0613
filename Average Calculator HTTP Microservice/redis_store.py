import redis
from config import REDIS_HOST, REDIS_PORT, WINDOW_KEY, UNIQUE_SET_KEY, WINDOW_SIZE

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_window() -> list[int]:
    data = r.lrange(WINDOW_KEY, 0, -1)
    return [int(x) for x in data]

def add_number(number: int) -> None:
    if r.sismember(UNIQUE_SET_KEY, number):
        return
    
    r.rpush(WINDOW_KEY, number)
    r.sadd(UNIQUE_SET_KEY, number)

    if r.llen(WINDOW_KEY) > WINDOW_SIZE:
        removed = r.lpop(WINDOW_KEY)
        r.srem(UNIQUE_SET_KEY, removed)

def calculate_average() -> float:
    nums = get_window()
    if len(nums) == 0:
        return 0.00

    total = 0
    for n in nums:
        total += n

    avg = total / len(nums)
    return round(avg, 2)
