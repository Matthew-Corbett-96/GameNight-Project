from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import os 
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from .models.models import User
from .service.messageService import MessageService

def create_scheduler(app: Flask) -> BackgroundScheduler:
    print("Creating scheduler")
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_jobstore(
        "sqlalchemy", 
        alias='gamenight_scheduler', 
        url=os.environ.get("DATABASE_URL")
    )
    # test job
    # scheduler.add_job(
    #     func=runScheduledTask,
    #     args=(app,),
    #     trigger="interval",
    #     seconds=5,
    #     id="test_id",
    # )
    # Day before alert job 
    scheduler.add_job(
        func=scheduledDayBeforeAlertTask,
        args=(app,),
        trigger="cron",
        day_of_week="wed",
        hour=18,
        minute=0,
        id="day_before_alert"
    )
    # game day alert job
    scheduler.add_job(
        func=scheduledGameDayAlertTask,
        args=(app,),
        trigger="cron",
        day_of_week="wed",
        hour=18,
        minute=1,
        id="game_day_alert"
    )
    return scheduler

def scheduledGameDayAlertTask(app: Flask) -> None:
    print("Running scheduled task")
    with app.app_context():
        messageService = MessageService()
        userList: list[User] = [ User.query.filter_by(username='matthewcorbett').first() ]
        messageService.sendGameDayAlert(userList)
    print("Scheduled task completed")

def scheduledDayBeforeAlertTask(app: Flask) -> None:
    print("Running scheduled task")
    with app.app_context():
        messageService = MessageService()
        userList: list[User] = [ User.query.filter_by(username='matthewcorbett').first() ]
        messageService.sendDayBeforeAlert(userList)
    print("Scheduled task completed")