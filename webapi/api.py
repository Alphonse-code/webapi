
import requests
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        Initialise le client API.
        @param {str} base_url - L'URL de base de l'API.
        @param {str} token - Le token d'authentification (facultatif).
        """
        self.base_url = base_url
        self.token = token

    def _get_headers(self) -> Dict[str, str]:
        headers = {}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Effectue une requête GET.
        @param {str} endpoint - L'endpoint de la requête.
        @param {dict} params - Les paramètres de la requête (facultatif).
        @return {requests.Response} - La réponse de la requête.
        """
        url = f'{self.base_url}{endpoint}'
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Effectue une requête POST.
        @param {str} endpoint - L'endpoint de la requête.
        @param {dict} data - Les données du formulaire de la requête (facultatif).
        @param {dict} json - Les données JSON de la requête (facultatif).
        @return {requests.Response} - La réponse de la requête.
        """
        url = f'{self.base_url}{endpoint}'
        headers = self._get_headers()
        response = requests.post(url, headers=headers, data=data, json=json)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Effectue une requête PUT.
        @param {str} endpoint - L'endpoint de la requête.
        @param {dict} data - Les données du formulaire de la requête (facultatif).
        @param {dict} json - Les données JSON de la requête (facultatif).
        @return {requests.Response} - La réponse de la requête.
        """
        url = f'{self.base_url}{endpoint}'
        headers = self._get_headers()
        response = requests.put(url, headers=headers, data=data, json=json)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response

    def delete(self, endpoint: str) -> requests.Response:
        """
        Effectue une requête DELETE.
        @param {str} endpoint - L'endpoint de la requête.
        @return {requests.Response} - La réponse de la requête.
        """
        url = f'{self.base_url}{endpoint}'
        headers = self._get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response

    def patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Effectue une requête PATCH.
        @param {str} endpoint - L'endpoint de la requête.
        @param {dict} data - Les données du formulaire de la requête (facultatif).
        @param {dict} json - Les données JSON de la requête (facultatif).
        @return {requests.Response} - La réponse de la requête.
        """
        url = f'{self.base_url}{endpoint}'
        headers = self._get_headers()
        response = requests.patch(url, headers=headers, data=data, json=json)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return response
