import json

with open(
    r"D:\insta\instagram-roy.suborno-2026-01-18-b6Rvs3cd\connections\followers_and_following\following.json",
    "r",
    encoding="utf-8",
) as following:
    data_01 = json.load(following)
    # titles_01 = [item[""] for item in data_01["relationships_following"]]
    # print(data_01)
    # title_01 = [item["href"] for item in data_01["string_list_data"]]
    link = [
        item["string_list_data"][0]["href"]
        for item in data_01["relationships_following"]
    ]
    print(link)
