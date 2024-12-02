import logging
import sys
from concurrent.futures import ThreadPoolExecutor

class AsyncHandler(logging.Handler):
    def __init__(self, handler):
        super().__init__()
        self.handler = handler
        self.executor = ThreadPoolExecutor(max_workers=1)

    def emit(self, record):
        self.executor.submit(self.handler.emit, record)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

async_handler = AsyncHandler(stream_handler)
logger.addHandler(async_handler)
