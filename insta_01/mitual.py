import json


with open(
    r"D:\insta\instagram-roy.suborno-2026-01-18-b6Rvs3cd\connections\followers_and_following\following.json",
    "r",
    encoding="utf-8",
) as following:
    data_01 = json.load(following)
    titles_01 = [item["title"] for item in data_01["relationships_following"]]


with open(
    r"D:\insta\instagram-roy.suborno-2026-01-18-b6Rvs3cd\connections\followers_and_following\followers_1.json",
    "r",
    encoding="utf-8",
) as followers:
    data_02 = json.load(followers)
    titles_02 = [item["string_list_data"][0]["value"] for item in data_02]


mituals = set(titles_01) & set(titles_02)
print(mituals)
