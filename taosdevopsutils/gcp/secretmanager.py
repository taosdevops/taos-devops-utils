from google.cloud import secretmanager


def get_from_secret_manager(project_id:str, secret_name:str):
    """Gets the latest version of a secret from GCP Secret Manager.
    :param project_id: Name of GCP project where the secret lives.
    :type project_id: str
    :param secret_name: Name of the secret to access.
    :type secret_name: str
    :return: Value of the latest version of the GCP secret
    :rtype: str
    """
    client = secretmanager.SecretManagerServiceClient()
    request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
    response = client.access_secret_version(request)
    secret_string = response.payload.data.decode("UTF-8")
    return secret_string