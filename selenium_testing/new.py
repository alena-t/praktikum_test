import requests


class TestGithubApi:

    BASE_URL = 'https://api.github.com'
    TOKEN = '<token>'
    TEST_REPO_NAME = 'Hello-World'
    USERNAME = '<username>'

    def setup(self):
        self.headers = {
            'Authorization': f'Bearer {self.TOKEN}',
            'Accept': 'application/vnd.github+json'
        }
        self.run_teardown = True

    def test_get_user(self):
        self.run_teardown = False
        username = 'octocat'
        response = requests.get(f'{self.BASE_URL}/users/{username}')

        assert response.status_code == 200
        assert response.json()['login'] == username

    def test_create_repo(self):
        repo_data = {
            'name': self.TEST_REPO_NAME,
            'description': 'Тестовое описание',
            'private': False,
            'is_template': True
        }
        response = requests.post(f'{self.BASE_URL}/user/repos', headers=self.headers, json=repo_data)

        assert response.status_code == 201
        assert response.json()['name'] == self.TEST_REPO_NAME

    def test_update_repo(self):
        repo_data = {
            'name': self.TEST_REPO_NAME,
            'description': 'Тестовое описание',
            'private': False,
            'is_template': True
        }
        requests.post(f'{self.BASE_URL}/user/repos', headers=self.headers, json=repo_data)

        new_description = 'Новое описание'
        update_data = {'description': new_description}
        response = requests.patch(
            f'{self.BASE_URL}/repos/{self.USERNAME}/{self.TEST_REPO_NAME}', headers=self.headers, json=update_data
        )

        assert response.status_code == 200
        assert response.json()['description'] == new_description

    def teardown(self):
        if self.run_teardown:
            response = requests.delete(
                f'{self.BASE_URL}/repos/{self.USERNAME}/{self.TEST_REPO_NAME}', headers=self.headers
            )

            assert response.status_code == 204
