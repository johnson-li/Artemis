import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)
logging.getLogger('paramiko.transport').setLevel(logging.WARNING)

