import os
import aiohttp
import logging
import asyncio
from aiohttp import web
from flask import Flask
app = Flask(__name__)

# إعدادات السجل
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# تقليل مستوى السجل لـ pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# تعريف الفئة Config
class Config:
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    Max_Tasks = int(os.environ.get("Max_Tasks", 1))
    WhiteList = [int(uid) for uid in os.environ.get("AUTH_USERS", "").split()]
    DB_URI = os.environ.get("MONGODB_URI")
    DB_NAME = "VideoConverter"
    Thumb = "Thumb.jpg"
    InDir = "IN"
    OutDir = "OUT"
    DOWNLOAD_LOCATION = "downloads"  # إضافة موقع التحميل

# معالجة الطلبات الواردة
async def handle_request(request):
    return web.Response(text="𝗛𝗲𝗹𝗹𝗼, 𝗪𝗲𝗯 𝗦𝗲𝗿𝘃𝗲𝗿")

# بدء خادم الويب
async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_request)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 80)
    print("Starting web server on 0.0.0.0:80")
    await site.start()

# نقطة الدخول الرئيسية
if __name__ == "__main__":
    # إنشاء دليل التحميل إذا لم يكن موجودًا
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)



    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_web_server())
    loop.run_until_complete(ntbot.run())
    
