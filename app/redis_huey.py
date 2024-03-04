import os
import redis
from huey import RedisHuey
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

redis_client = redis.StrictRedis(host=HOST, port=PORT, decode_responses=True)

huey = RedisHuey(
    APP_NAME,  # Replace with your app name
    host=HOST,  # Redis server hostname
    port=PORT,  # Redis server port
    # blocking=True,  # Use blocking-pop when reading from the queue
)


@huey.task()
def get_key(key):
    key_str = str(key)
    value = redis_client.get(key_str)
    if value is None:
        raise Exception(
            f"Value with key '{key}' not found.",
        )
    return value


@huey.task()
def add_key(key, value):
    key_str = str(key)
    if redis_client.exists(key_str):
        raise Exception(
            f"Value with Key '{key}' already exists.",
        )
    redis_client.set(key, value)
    return {
        "key": key, "value": value
    }


@huey.task()
def delete_key(key):
    key_str = str(key)
    if not redis_client.exists(key_str):
        raise Exception(
            f"Can't delete, key '{key}' not found.",
        )
    redis_client.delete(key)
    return {
        "key": key
    }
