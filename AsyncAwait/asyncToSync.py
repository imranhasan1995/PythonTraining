import asyncio
from asgiref.sync import sync_to_async, async_to_sync
import time

# Sync function (blocking)
def blocking_db_query(user_id):
    print(f"Querying DB for user {user_id}")
    time.sleep(1)
    return {"user_id": user_id, "name": f"User{user_id}"}

# Async function calling sync DB query
async def fetch_user(user_id):
    user = await sync_to_async(blocking_db_query)(user_id)
    return user

# Sync function calling async fetch_user
def get_user_sync(user_id):
    return async_to_sync(fetch_user)(user_id)

# Example usage
if __name__ == "__main__":
    print(get_user_sync(101))
    print(get_user_sync(102))
