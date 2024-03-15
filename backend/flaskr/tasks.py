from logging import getLogger
from flask import Flask
import os
from celery import shared_task
from celery.utils.log import get_task_logger
from .models.models import User
from .service.messageService import MessageService

logger = getLogger(__name__)

@shared_task(bind=True)
def send_day_before_message(self) -> None:
    logger.info("Sending Day Before Message")
    # message_service = MessageService()
    # message_service.send_day_before_message()
    # users: User = User.query.all()
    # for user in users:
    #     print(user.to_dict())

@shared_task(bind=True)
def send_day_of_message(self) -> None:
    logger.info("Sending Day of Message")
    get_task_logger(__name__).info("Sending Day of Message")
    message_service = MessageService()
    message_service.sendDayBeforeAlert([User.query.filter_by(username="matthewcorbett").first()])
