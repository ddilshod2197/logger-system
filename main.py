import logging

# Logger yaratish
logger = logging.getLogger(__name__)

# Logger uchun konfiguratsiya
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Info log qilish
logger.info('Logger yaratildi')

# Warning log qilish
logger.warning('Warning: Logger yaratildi')

# Error log qilish
logger.error('Error: Logger yaratildi')

# Critical log qilish
logger.critical('Critical: Logger yaratildi')
