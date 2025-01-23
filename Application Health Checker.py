import requests

def check_application_health(url):
    try:
        # Send a GET request to the application URL
        response = requests.get(url)

        # Check the status code and determine the application status
        if response.status_code == 200:
            print(f"The application at {url} is UP and functioning correctly.")
        else:
            print(f"The application at {url} is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error while checking the application health: {e}")
