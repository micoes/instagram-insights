import requests
import json
import datetime

with open("authentication.json") as open_file:
    access = json.load(open_file)

user_access_token = access["user_access_token"]
user_id = access["user_id"]

# between since and until cannot be more than 30 days (2592000s)
since, until = "01/01/2021, 00:00:00", "01/10/2021, 23:59:59"
date_since, date_until = datetime.datetime.strptime(since, "%m/%d/%Y, %H:%M:%S"), datetime.datetime.strptime(until, "%m/%d/%Y, %H:%M:%S")
timestamp_since, timestamp_until = datetime.datetime.timestamp(date_since), datetime.datetime.timestamp(date_until)

# get data about your own Instagram Business or Creator Account
# https://developers.facebook.com/docs/instagram-api/reference/ig-user
instagram_user = f"https://graph.facebook.com/v10.0/{user_id}" \
                 "?fields=id,username,biography,followers_count,follows_count" \
                 f"&access_token={user_access_token}"

r = requests.get(instagram_user)
# print(r.text)

# get social interaction metrics about your own Instagram Business or Creator Account and Media objects
# https://developers.facebook.com/docs/instagram-api/guides/insights
insights = f"https://graph.facebook.com/v10.0/{user_id}" \
           f"/insights?metric=impressions,reach&period=days_28&since={timestamp_since}&until={timestamp_until}" \
           f"&access_token={user_access_token}"

r = requests.get(insights)
print(r.text)

# get data about other Instagram Business or Creator Accounts
# https://developers.facebook.com/docs/instagram-api/guides/business-discovery
business_discovery = f"https://graph.facebook.com/v10.0/{user_id}" \
                     "?fields=business_discovery.username(bluebottle){id,username,biography,followers_count,follows_count}" \
                     f"&access_token={user_access_token}"

r = requests.get(business_discovery)
# print(r.text)
