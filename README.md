# WebAPI

WebAPI est une bibliothèque Python pour se connecter aux APIs Web. Elle permet de faire des requêtes GET, POST, PUT, DELETE et PATCH facilement, et de gérer les tokens d'authentification.

## Installation

Vous pouvez installer cette bibliothèque en utilisant `pip`. Assurez-vous d'être dans le répertoire contenant le fichier `setup.py`, puis exécutez :

```bash
pip install .
```

### Utilisation de la bibliothèque dans un projet Python

Une fois que vous avez installé la bibliothèque `webapi`, vous pouvez l'utiliser dans votre projet Python comme illustré ci-dessus. Voici un exemple de script Python complet utilisant `webapi` :

```python
# exemple_d_utilisation.py

# Importation de la classe APIClient depuis la bibliothèque webapi
from webapi.api import APIClient

# Initialisation du client API avec le token d'authentification
client = APIClient(base_url="https://api.example.com", token="votre_token")

# Exemple de requête GET
response = client.get("/data")
print("GET Response:", response.json())

# Exemple de requête POST
data = {"key": "value"}
response = client.post("/data", json=data)
print("POST Response:", response.json())

# Exemple de requête PUT
update_data = {"key": "new_value"}
response = client.put("/data/1", json=update_data)
print("PUT Response:", response.json())

# Exemple de requête DELETE
response = client.delete("/data/1")
print("DELETE Response:", response.status_code)

# Exemple de requête PATCH
patch_data = {"key": "updated_value"}
response = client.patch("/data/1", json=patch_data)
print("PATCH Response:", response.json())
```