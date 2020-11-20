from google.cloud import storage


def load(bucket: str, project: str, fname: str) -> str:
    """Returns file contents from provided bucket and file names.
    :param bucket: Bucket to fetch file from
    :type bucket: str
    :param project: Project in which bucket lives
    :type project: str
    :param fname: File path in bucket to download
    :type fname: str
    :return: Full file downloaded from GCS
    :rtype: str
    """
    client = storage.Client(project=project)
    bucket = client.bucket(bucket)
    blob = bucket.blob(fname)
    response = blob.download_as_string()

    return response