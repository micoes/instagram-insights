import requests
import json
import datetime
import os.path


def instagram(user_id, user_access_token):
    # timestamps in API responses use UTC with zero offset and are formatted using ISO-8601
    # UTC (Universal Time) is 7 hours ahead of PST (Pacific Standard Time)
    until = datetime.datetime.today()
    until_processed = until.strftime("%d/%m/%Y, 00:00:00")
    until_date = datetime.datetime.strptime(until_processed, "%d/%m/%Y, %H:%M:%S")
    until_timestamp = datetime.datetime.timestamp(until_date)
    since_timestamp = until_timestamp - 2592000

    # current data about your Instagram Business or Creator Account
    # https://developers.facebook.com/docs/instagram-api/reference/ig-user
    r = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"?fields=id,username,biography,followers_count"
        f"&access_token={user_access_token}")

    instagram_user = r.json()

    # social interaction metrics within range (max. 30 days = 2592000s)
    # https://developers.facebook.com/docs/instagram-api/guides/insights
    r = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"/insights?metric=impressions,reach&period=days_28&since={since_timestamp}&until={until_timestamp}"
        f"&access_token={user_access_token}")

    instagram_reach = r.json()

    # total number of new followers each day of the last 30 days, excluding the current day
    # https://developers.facebook.com/docs/instagram-api/guides/insights
    r = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"/insights?metric=follower_count&period=day&since={since_timestamp}&until={until_timestamp}"
        f"&access_token={user_access_token}")

    instagram_follower = r.json()
    instagram_reach["data"].append(instagram_follower["data"][0])

    if os.path.exists("data/archive.json"):
        with open("data/archive.json", "r") as json_file:
            archive = json.load(json_file)

        archive.update(instagram_user)
        archive.update(instagram_reach)

        with open("data/archive.json", "w", encoding="utf-8") as json_file:
            json.dump(archive, json_file, indent=4)

    else:
        with open("data/archive.json", "w", encoding="utf-8") as json_file:
            json.dump(instagram_user, json_file, indent=4)
        with open("data/archive.json", "r", encoding="utf-8") as json_file:
            archive = json.load(json_file)

        archive.update(instagram_reach)

        with open("data/archive.json", "w", encoding="utf-8") as json_file:
            json.dump(archive, json_file, indent=4)


"""
if __name__ == "__main__":
    with open("data/authentication.json", "r") as json_file:
        access = json.load(json_file)

    user_access_token = access["user_access_token"]
    user_id = access["user_id"]

    instagram(user_id, user_access_token)
"""
