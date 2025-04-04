import httpx
from config import ACCESS_TOKEN


async def fetch_numbers_from_server(number_id: str):
    urls = {
        "p": "http://20.244.56.144/evaluation-service/primes",
        "f": "http://20.244.56.144/evaluation-service/fibo",
        "e": "http://20.244.56.144/evaluation-service/even",
        "r": "http://20.244.56.144/evaluation-service/rand"
    }

    if number_id not in urls:
        return []

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    try:
        async with httpx.AsyncClient(timeout=0.5) as client:
            response = await client.get(urls[number_id], headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data.get("numbers", [])
            else:
                print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Fetch failed: {e}")

    return []
