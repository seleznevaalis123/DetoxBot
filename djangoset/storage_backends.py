from storages.backends.s3boto3 import S3Boto3Storage
from boto3.s3.transfer import TransferConfig

# Настройка для безопасной загрузки
DEFAULT_TRANSFER_CONFIG = TransferConfig(
    multipart_threshold=10 * 1024 * 1024,  # 10MB — файлы меньше будут загружаться обычным PUT
    max_concurrency=2,  # меньше потоков, меньше вероятность подвисания
    multipart_chunksize=5 * 1024 * 1024,  # размер частей для multipart
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
