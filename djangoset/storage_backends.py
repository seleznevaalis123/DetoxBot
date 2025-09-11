from storages.backends.s3boto3 import S3Boto3Storage
from boto3.s3.transfer import TransferConfig

DEFAULT_TRANSFER_CONFIG = TransferConfig(
    multipart_threshold=15 * 1024 * 1024,  # файлы < 15MB — обычный PUT
    max_concurrency=2,                     # меньше потоков
    multipart_chunksize=5 * 1024 * 1024,   # размер части для больших файлов
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

class PrivateMediaStorage(S3Boto3Storage):
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
    transfer_config = DEFAULT_TRANSFER_CONFIG
