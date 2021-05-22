import requests
import json
import datetime

with open("data/authentication.json") as open_file:
    access = json.load(open_file)

user_access_token = access["user_access_token"]
user_id = access["user_id"]

# convert datetime to unix timestamp
since, until = "01/01/2021, 00:00:00", "01/10/2021, 23:59:59"
date_since, date_until = datetime.datetime.strptime(since, "%m/%d/%Y, %H:%M:%S"), datetime.datetime.strptime(until, "%m/%d/%Y, %H:%M:%S")
timestamp_since, timestamp_until = datetime.datetime.timestamp(date_since), datetime.datetime.timestamp(date_until)

# get current data about your Instagram Business or Creator Account
# https://developers.facebook.com/docs/instagram-api/reference/ig-user
instagram_user = f"https://graph.facebook.com/v10.0/{user_id}" \
                 "?fields=id,username,biography,followers_count,follows_count" \
                 f"&access_token={user_access_token}"

r = requests.get(instagram_user)
# print(r.text)

# get social interaction metrics about your Instagram Business or Creator Account within the specified range (max. 30 days = 2592000s)
# https://developers.facebook.com/docs/instagram-api/guides/insights
insights = f"https://graph.facebook.com/v10.0/{user_id}" \
           f"/insights?metric=impressions,reach&period=days_28&since={timestamp_since}&until={timestamp_until}" \
           f"&access_token={user_access_token}"

r = requests.get(insights)
# print(r.text)

# get total number of new followers each day for your own Instagram Business or Creator Account within the specified range (max. 1 day = 86400s)
# supports querying data only for the last 30 days excluding the current day
timestamp = 1619215200

insights_follower_count = f"https://graph.facebook.com/v10.0/{user_id}" \
                          f"/insights?metric=follower_count&period=day&since={timestamp}&until={timestamp + 86400}" \
                          f"&access_token={user_access_token}"

r = requests.get(insights_follower_count)
print(r.text)
