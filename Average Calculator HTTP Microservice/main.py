from fastapi import FastAPI
from redis_store import get_window, add_number, calculate_average
from number_fetch import fetch_numbers_from_server

app = FastAPI()

@app.get("/numbers/{number_id}")
async def get_numbers(number_id: str):
    prev_window = get_window()

    fetched_numbers = await fetch_numbers_from_server(number_id)

    if fetched_numbers:
        for num in fetched_numbers:
            add_number(num)

    curr_window = get_window()
    avg = calculate_average()

    return {
        "windowPrevState": prev_window,
        "windowCurrState": curr_window,
        "numbers": fetched_numbers,
        "avg": avg
    }
