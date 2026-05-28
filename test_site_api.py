import requests
import pytest

#base url for the mock internal site data api
base_url = "https://api.langan-mock.com/v1/site_surveys"

#sample valid payload for a new land development site
valid_payload = {
    "project_id": 8492,
    "location": "parsippany nj",
    "soil_ph": 6.5,
    "is_active": True
}

def test_successful_site_creation():
    #sending valid data to see if the internal app processes it correctly
    response = requests.post(base_url, json=valid_payload)
    
    #expecting a 201 created status code
    assert response.status_code == 201
    assert response.json()["status"] == "success"

def test_missing_location_data():
    #testing an edge case where an engineer forgets to input the location
    bad_payload = valid_payload.copy()
    del bad_payload["location"]
    
    response = requests.post(base_url, json=bad_payload)
    
    #app should fail gracefully with a 400 bad request not a server crash
    assert response.status_code == 400
    assert "location required" in response.json()["error"].lower()

def test_invalid_soil_ph_boundary():
    #testing system validation against impossible environmental data
    out_of_bounds_payload = valid_payload.copy()
    out_of_bounds_payload["soil_ph"] = 15.0  #ph scale only goes to 14
    
    response = requests.post(base_url, json=out_of_bounds_payload)
    
    #expecting a 422 unprocessable entity error
    assert response.status_code == 422
