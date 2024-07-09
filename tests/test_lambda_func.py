import json
import requests
import pytest


LAMBDA_URL = "https://zo6emcw4a6z5mkihjkggrvutqe0gvpbi.lambda-url.eu-west-3.on.aws/"

@pytest.fixture
def lambda_url():
    return LAMBDA_URL

def test_lambda_function(lambda_url):
    event = {"key": "value"}

   
    response = requests.post(lambda_url, data=json.dumps(event))

   
    assert response.status_code == 200

    try:
        result = response.json()
        if isinstance(result, int):
            result = {"views": result}
        assert "views" in result
        assert isinstance(result["views"], int)

    except json.JSONDecodeError:
        
        pytest.fail("Response is not a valid JSON")

if __name__ == "__main__":
    pytest.main()