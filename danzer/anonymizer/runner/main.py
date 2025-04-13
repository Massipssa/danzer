import logging
from danzer.anonymizer.runner.runner import run

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s'
)

WELCOME_MESSAGE = r"""
 ██████████     █████████   ██████   █████ ███████████ ██████████ ███████████  
░░███░░░░███   ███░░░░░███ ░░██████ ░░███ ░█░░░░░░███ ░░███░░░░░█░░███░░░░░███ 
 ░███   ░░███ ░███    ░███  ░███░███ ░███ ░     ███░   ░███  █ ░  ░███    ░███ 
 ░███    ░███ ░███████████  ░███░░███░███      ███     ░██████    ░██████████  
 ░███    ░███ ░███░░░░░███  ░███ ░░██████     ███      ░███░░█    ░███░░░░░███ 
 ░███    ███  ░███    ░███  ░███  ░░█████   ████     █ ░███ ░   █ ░███    ░███ 
 ██████████   █████   █████ █████  ░░█████ ███████████ ██████████ █████   █████
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ 
"""

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info(WELCOME_MESSAGE)
    run()
    """
    config_path = "../../../examples/config/spark-ano-config.json"
    config_data = load_config_from_json(config_path)
    ano_config = load_config(config_data)
    print(ano_config)
    """
