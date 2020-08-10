from celery import Celery
from datetime import time
from celery import shared_task
from time import sleep
# app = Celery('hello', broker='amqp://guest@localhost//')
@shared_task
def dump_celery():
   print('ise dusdu')
   sleep(10)
   print('bitdi')
   