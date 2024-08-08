import os
from config.connect import dbuser, dbpass, dbhost, dbport, dbname

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'mysql+mysqlconnector://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False









"""
from datetime import datetime

salt = '123456'
roles = ['Member','Tutor','Manager']
Manager_role = ('Manager')
Tutor_role = ('Manager','Tutor')
Member_role = ('Member','Tutor','Manager')
status = ['0','1','2']  #0: normal  1:unpaid 2:deleted
current_date = datetime.now().strftime("%Y-%m-%d")

secret_key = '123456'

list_sort = ['asc','asc']

student_discount = 0.7

membershipType = ['monthly membership','annual membership']
booking_status =['0','1','2'] # 0:normal , 1:expired, 2:canceled
booking_payment = ['0','1','2'] # 0:paid , 1:unpaid, 2:returned

lesson_price = 100.00
workshop_price = 80.00

#url = 'http://127.0.0.1:5000'

url = 'https://robin777.pythonanywhere.com'

lesson_default_image = 'livestock.jpg'
member_default_image = 'people1.jpg'
"""
