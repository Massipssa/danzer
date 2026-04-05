import logging
from danzer.anonymizer.cli.main import main

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main()
