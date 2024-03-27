from logging import getLogger
from flask import Flask
import os
from celery import shared_task
from celery.utils.log import get_task_logger
from .models.models import User
from .service.messageService import MessageService

logger = getLogger(__name__)

@shared_task(bind=True)
def heartbeat(self) -> None:
    logger.info("heartbeat!...")

@shared_task(bind=True)
def send_day_before_message(self) -> None:
    logger.info("Sending Day Before Message")
    message_service = MessageService()
    message_service.sendDayBeforeAlert([ user for user in User.query.all() if is_valid_phone_number(user)])

@shared_task(bind=True)
def send_day_of_message(self) -> None:
    logger.info("Sending Day of Message")
    message_service = MessageService()
    message_service.sendGameDayAlert([ user for user in User.query.all() if is_valid_phone_number(user)])

@shared_task(bind=True)
def send_hour_on_hour_message(self) -> None:
    logger.info("Sending Hour on Hour Message")
    userList: list[User] = User.query.all()
    filteredList = [user for user in userList if is_valid_phone_number(user)]
    message_service = MessageService()
    message_service.sendHourOnHourMessage(filteredList)

def is_valid_phone_number(user: User) -> bool:
    return user.phone_number is not None \
          and len(user.phone_number) > 0 \
          and user.phone_number == "5082438026"