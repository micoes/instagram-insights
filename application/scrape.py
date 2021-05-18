import requests
import json

with open("authentication.json") as open_file:
    access = json.load(open_file)

user_access_token = access["user_access_token"]
user_id = access["user_id"]

# get data about your own Instagram Business or Creator Account
# https://developers.facebook.com/docs/instagram-api/reference/ig-user
instagram_user = f"https://graph.facebook.com/v10.0/{user_id}" \
                 "?fields=id,username,followers_count,follows_count" \
                 f"&access_token={user_access_token}"

r = requests.get(instagram_user)
print(r.text)

# get data about other Instagram Business or Creator Accounts
# https://developers.facebook.com/docs/instagram-api/guides/business-discovery
business_discovery = f"https://graph.facebook.com/v10.0/{user_id}" \
                     "?fields=business_discovery.username(bluebottle){id,username,followers_count,follows_count}" \
                     f"&access_token={user_access_token}"

r = requests.get(business_discovery)
# print(r.text)

# get social interaction metrics for Instagram Users and their Media objects
# https://developers.facebook.com/docs/instagram-api/guides/insights
insights = f"https://graph.facebook.com/v10.0/{user_id}" \
           "/insights?metric=impressions,reach,profile_views&period=day" \
           f"&access_token={user_access_token}"

r = requests.get(insights)
# print(r.text)
