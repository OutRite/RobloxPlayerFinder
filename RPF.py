#!/bin/python3

print("Welcome to the ROBLOX player finder.")
print("This only uses official APIs (shouldn't be bannable!)")
print("Made by OutRite (Player: Theuslesseagle_534)")
print("\n")
print("Importing libraries... Please wait.")

import requests # we need this to contact the ROBLOX APIs
import sys
print("\n")

player_name = input("Enter player name: ")

# now for our first API call, to users.roblox.com !

# we need to patch some variables since the json response isn't too python friendly
# thank you roblox very cool

null = 0
true = True
false = False

userid_request_json = {"usernames": [player_name],"excludeBannedUsers": true}

user_api_url = "https://users.roblox.com/v1/usernames/users"

print("Getting user id from username...")

user_api_req = requests.post(user_api_url, data = userid_request_json)

user_api_resp_json = user_api_req.json()

# this is where we extract the user id
try:
	user_id = user_api_resp_json["data"][0]["id"]
except:
	print("Invalid user.")
	sys.exit()

print("User id: {}".format(user_id))
# now to put it into the Badges API

badge_list_url = "https://badges.roblox.com/v1/users/{}/badges?limit=10&sortOrder=Desc".format(user_id)

print("Getting badge list...")

badge_list_req = requests.get(badge_list_url)

badge_list_resp_json = badge_list_req.json()

# extract the latest badge id

try:
	latest_badge_id = badge_list_resp_json["data"][0]["id"]
except:
	print("Failed to get badge. Either something went wrong or \nthe player has not played anything.")
	sys.exit()

print("Latest badge id: {}".format(latest_badge_id))

# Badge API cont. (getting game name from badge ID)

print("Getting game name from latest badge...")

badge_name_url = "https://badges.roblox.com/v1/badges/{}".format(latest_badge_id)

badge_name_req = requests.get(badge_name_url)

badge_name_resp_json = badge_name_req.json()

# print(badge_name_resp_json) # left over from debugging.

try:
	game_name = badge_name_resp_json["awardingUniverse"]["name"]
except:
	print("The most recent badge does not seem to be valid, or something \nwent wrong.")
print("Results:")
print("Player: {}".format(player_name))
print("Likely last played game: {}".format(game_name))
print("Done! Enjoy!")
