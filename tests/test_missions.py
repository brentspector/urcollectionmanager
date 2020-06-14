from urcollectionmanager import missions, http


def test_get_mission_url():
    """Happy Path - Get Mission URL"""
    ALT_URL = "http://fakesite.com?"
    url = missions.get_mission_url(2, "montana", "progress", ALT_URL)
    assert ALT_URL in url
    assert "page=2" in url
    assert f"category={missions.MissionCategory.MONTANA.value}" in url
    assert "state=inprogress" in url


def test_minimal_get_mission_url():
    """Alt Happy Path - Only bare minimum request"""
    url = missions.get_mission_url(0, "", "", None)
    assert missions.BASE_MISSION_URL in url
    assert "page=0" in url
    assert "category=0" in url
    assert "state=all" in url


def test_find_missions(mocked_missions):
    """Happy Path - List of Missions"""
    res = missions.find_missions(http.convert_html_to_soup(mocked_missions))
    assert len(res) == 10
    assert res[0].name == "BLACK MARKET - 500 Glorg-> 50 Millions"


def test_create_mission(mocked_missions):
    """Happy Path - Create Mission"""
    soup = http.convert_html_to_soup(mocked_missions)
    res = missions.create_mission(soup.find_all("ul")[2].li)
    assert res.name == "BLACK MARKET - 500 Glorg-> 50 Millions"
    assert res.goal == 500

# BELOW IS COMMENTED UNTIL THERE IS A WAY TO MODIFY WHAT DATA IS
# GIVEN TO TOTAL_PROGRESS IN MISSION.PY
# def test_create_mission_no_progress(mocked_missions):
#     """Alt Path - Create Mission"""
#     soup = http.convert_html_to_soup(mocked_missions)
#     val = soup.find_all("ul")[2].li
#     val.find("div", class_="progress-bar").text = "You have completed this mission"
#     res = missions.create_mission(None)
#     assert res.name == "BLACK MARKET - 500 Glorg-> 50 Millions"
#     assert res.goal == 0
#     assert res.progress == 0
