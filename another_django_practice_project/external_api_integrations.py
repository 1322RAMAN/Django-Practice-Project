import requests
from decouple import config


class APIClient:
    """
    A generic client to interact with external APIs.
    """

    def __init__(self, base_url, headers=None, timeout=10):
        """
        Initialize the API client with a base URL and optional headers.

        :param base_url: The base URL of the API.
        :param headers: Optional headers to include in requests.
        :param timeout: Timeout for API requests (default: 10 seconds).
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout

    def get(self, endpoint, params=None):
        """
        Send a GET request.

        :param endpoint: The API endpoint.
        :param params: Query parameters for the GET request.
        :return: Response JSON or None if the request fails.
        """
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None, json=None):
        """
        Send a POST request.

        :param endpoint: The API endpoint.
        :param data: Form data for the POST request.
        :param json: JSON payload for the POST request.
        :return: Response JSON or None if the request fails.
        """
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                data=data,
                json=json,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, endpoint, data=None, json=None):
        """
        Send a PUT request.

        :param endpoint: The API endpoint.
        :param data: Form data for the PUT request.
        :param json: JSON payload for the PUT request.
        :return: Response JSON or None if the request fails.
        """
        try:
            response = requests.put(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                data=data,
                json=json,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint):
        """
        Send a DELETE request.

        :param endpoint: The API endpoint.
        :return: Response JSON or None if the request fails.
        """
        try:
            response = requests.delete(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None


def weather_view():
    # Initialize the API client
    api_client = APIClient(base_url="https://api.openweathermap.org/data/2.5/", headers={"Authorization": f"Bearer {config('SECRET_KEY')}"})

    # Example: Fetch current weather for a city
    response = api_client.get("weather", params={"q": "London", "appid": config("SECRET_KEY")})
    if response:
        print("Weather data:", response)
