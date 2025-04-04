import requests

class RequestFetcher:
    BASE_URL = "http://20.244.56.144/evaluation-service"

    @staticmethod
    def get_users():
        url = f"{RequestFetcher.BASE_URL}/users"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {"error": response.text}

    @staticmethod
    def get_posts(user_id):
        url = f"{RequestFetcher.BASE_URL}/users/{user_id}/posts"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {"error": response.text}

    @staticmethod
    def get_comments(post_id):
        url = f"{RequestFetcher.BASE_URL}/posts/{post_id}/comments"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {"error": response.text}
