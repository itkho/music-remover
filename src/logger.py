import logging

def init_logger(log_path: str, log_level: str):
    logging.basicConfig(
        level=log_level,
        filename=log_path,
        filemode="w",
        format="[%(asctime)s] %(name)s - %(levelname)s: %(message)s"
    )
