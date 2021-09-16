import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {"Processtemperature[K]": 500, 
    "Rotationalspeed[rpm]": 3000, 
    "Torque[Nm]": 100, 
    "Toolwear[min]": 500, 
    "TWF": 12, 
    "HDF": 9, 
    "PWF": 7, 
    "OSF": 2, 
    "RNF": 3, 
    },

    "correct_range":
    {"Processtemperature[K]": 310, 
    "Rotationalspeed[rpm]": 1200, 
    "Torque[Nm]": 50, 
    "Toolwear[min]": 100, 
    "TWF": 1, 
    "HDF": 0, 
    "PWF": 1, 
    "OSF": 0, 
    "RNF": 0, 
    },

    "incorrect_col":
    {"Process temperature[K]": 500, 
    "Rotational speed[rpm]": 3000, 
    "Torque [Nm]": 100, 
    "Tool wear[min]": 500, 
    "TWF": 12, 
    "HDF": 9, 
    "PWF": 7, 
    "OSF": 2, 
    "RNF": 3, 
    }
}

TARGET_range = {
    "min": 295.3,
    "max": 304.5
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message