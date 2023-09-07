import logging

import gpt_assistant_lib
import telegram as tg
import telegram.ext as tg_ext
import telegram.ext.filters as tg_filters

from ._settings import Settings


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class App:
    def __init__(self, settings: Settings) -> None:
        self.token = settings.telegram_bot_token

        self.assistant = gpt_assistant_lib.build_assistant(
            settings.openai_api_key,
            settings.system_prompt,
            settings.history_size,
            settings.history_ttl,
        )
        self.start_message = settings.start_message
        self.allowed_users = set(settings.allowed_users)

    def run(self) -> None:
        self.application = tg_ext.ApplicationBuilder().token(self.token).build()

        start_handler = tg_ext.CommandHandler("start", self.start)
        regular_message_handler = tg_ext.MessageHandler(
            tg_filters.TEXT & ~tg_filters.COMMAND, self.handle_regular_message
        )

        self.application.add_handler(start_handler)
        self.application.add_handler(regular_message_handler)

        logger.info("Start BOT")

        self.application.run_polling()

    async def start(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        if update.effective_chat is None:
            logger.error("Unexpected update object received in start handlea")
            return
        logger.info(f"Start received from {update.effective_chat.id}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=self.start_message)

    async def handle_regular_message(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        if update.message is None or update.message.text is None or update.effective_user is None:
            logger.error("Unexpected update object received in regular message handle")
            return

        message_text = update.message.text
        user_id = str(update.effective_user.id)

        logger.info(f"{user_id}: {message_text}")

        if user_id not in self.allowed_users:
            logger.info("Not allowed user. skip", extra={"user_id": user_id})
            return
        try:
            response = self.assistant.exchange(user_id, message_text)
        except gpt_assistant_lib.GptAssistantBaseException as e:
            logger.exception(f"GPT assistant exception, {e}")
            return
        logger.info(f"assistant: {response}")
        await update.message.reply_text(response)
