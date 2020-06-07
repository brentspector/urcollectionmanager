import sys
import os
from pytest import mark
from urcollectionmanager import api, history, http, missions
from requests import Session
################################
# TO RUN
# Uncomment any function and run
# >>> pytest tests/resources/resource_maker.py
# Comment the function out again when finished
################################

# @mark.create_file("missions.txt")
# def test_create_history_file(create_file):
#     with Session() as s:
#         sys.setrecursionlimit(20000)
#         # Reads "UR_USER" for username and "UR_PASS" for password from host environment variables
#         api.session_connect_to_ur(s, os.environ["UR_USER"], os.environ["UR_PASS"])
#         res = s.get(missions.get_mission_url(0, "flash", "all", None))
#         create_file.append(res)
