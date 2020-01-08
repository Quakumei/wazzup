#!/usr/bin/env python3

"""
Core of wazzup
"""

import json
import requests
import argparse
import getpass #getpass.getuser() returns username

USERNAME = getpass.getuser()

argparser = argparse.ArgumentParser(
    description="tool to display status of literally anything. v.Kostil'")

argparser.add_argument(
    '-w',
    '--what',
    help="W-What information do you want to actually see, "+ USERNAME +"-sama?",
    required=True)

args = argparser.parse_args()

def greeting_header():
    print("Welcome back, " + USERNAME + "-sama.")
    print("Here goes your order...")


def time():
    """
        Request and print time data.
    """
# Current time display (using API of https://worldtimeapi.org)
# TODO: config file
# TODO: time zones
# TODO: sunset / sunrise time
# TODO: time service choice

    time_get_url = "https://worldtimeapi.org/api/timezone/Etc/GMT-3"
    time_request = requests.get(time_get_url)
    time_response = json.loads(time_request.content)
    print("UTC: " + time_response["utc_datetime"])
    print("RAW:" + time_response.str())


greeting_header()

if args.what == "time":
    time()

