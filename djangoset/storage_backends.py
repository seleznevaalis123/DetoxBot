from storages.backends.s3boto3 import S3Boto3Storage
from boto3.s3.transfer import TransferConfig

DEFAULT_TRANSFER_CONFIG = TransferConfig(
    multipart_threshold=15 * 1024 * 1024,
    max_concurrency=2,
    multipart_chunksize=5 * 1024 * 1024,
    use_threads=True
)

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    transfer_config = DEFAULT_TRANSFER_CONFIG

class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    transfer_config = DEFAULT_TRANSFER_CONFIG
