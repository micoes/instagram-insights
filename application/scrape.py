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
    instagram_user = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"?fields=username,biography,followers_count"
        f"&access_token={user_access_token}")

    # social interaction metrics within range (max. 30 days = 2592000s)
    # https://developers.facebook.com/docs/instagram-api/guides/insights
    instagram_reach = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"/insights?metric=impressions,reach&period=days_28&since={since_timestamp}&until={until_timestamp}"
        f"&access_token={user_access_token}")

    # total number of new followers each day of the last 30 days, excluding the current day
    # https://developers.facebook.com/docs/instagram-api/guides/insights
    instagram_follower = requests.get(
        f"https://graph.facebook.com/v10.0/{user_id}"
        f"/insights?metric=follower_count&period=day&since={since_timestamp}&until={until_timestamp}"
        f"&access_token={user_access_token}")

    if os.path.exists("data/archive.json"):
        with open("data/archive.json", "a") as json_file:
            archive = json.dumps(instagram_follower.text, indent=4)
            json_file.write(archive)
    else:
        with open("data/archive.json", "w", encoding="utf-8") as json_file:
            archive = json.dumps(instagram_follower.text, indent=4)
            json_file.write(archive)
