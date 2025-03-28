import os
import psycopg2
import pathlib
from aiogram.types import FSInputFile
from dotenv import load_dotenv
load_dotenv()


# Connect to your postgres DB
def connect_to_db():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )


async def cmd_start_db(user_id, username):
    db = connect_to_db()
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM users WHERE tg_id=%s", (user_id,))
        user = cur.fetchone()
        if user is None:
            cur.execute("INSERT INTO users (tg_id, tg_name) VALUES (%s, %s)", (user_id, username))
            db.commit()
        else:
            print("User already exists in the database.")
    finally:
        cur.close()
        db.close()


async def get_announcements():
    db = connect_to_db()
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM Announcements")
        announcement = cur.fetchall()
        for i in announcement:
            announcement_photo = FSInputFile(pathlib.Path(__file__).resolve().parent.parent.joinpath('media/' + i[2]))
            caption = f' \n {i[1]}'
            return announcement_photo, caption
    finally:
        cur.close()
        db.close()
