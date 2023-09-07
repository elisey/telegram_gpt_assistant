import logging

from telegram_gpt_assistant._cli import entrypoint


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


entrypoint()
