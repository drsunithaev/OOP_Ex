import logging
import os

logging.basicConfig(
    filename=os.path.join("log", 'log_info.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )
