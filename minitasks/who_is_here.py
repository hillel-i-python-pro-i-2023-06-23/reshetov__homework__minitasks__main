import aiohttp
import asyncio
import json


async def get_response(url: str) -> dict:
    """
    :param: url: URL of API: "http://api.open-notify.org/astros.json"
    :return: dict: dictionary with info about astronauts
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.text()
            response_dict = json.loads(json_response)
            return response_dict


def number_of_astronauts() -> int:
    """
    :param: None
    :return: astronauts: Number of astronauts
    """

    url = "http://api.open-notify.org/astros.json"
    url_response = asyncio.run(get_response(url))
    astronauts = url_response["number"]
    print(f"{astronauts} astronauts at this moment.")
    return astronauts
