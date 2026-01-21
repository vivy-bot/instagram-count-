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


following_set = set(titles_01)
followers_set = set(titles_02)

mutuals = following_set & followers_set
not_following_back = following_set - followers_set
fans = followers_set - following_set


print(f"Total Following: {len(following_set)}")
print(f"Total Followers: {len(followers_set)}")

print("\nMutuals:", len(mutuals))
print(sorted(mutuals))

print("\nNot following back:", len(not_following_back))
print(sorted(not_following_back))

print("\nFollowers you don't follow back:", len(fans))
print(sorted(fans))
