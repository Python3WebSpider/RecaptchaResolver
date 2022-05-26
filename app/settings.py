from environs import Env

env = Env()
env.read_env()

CAPTCHA_RESOLVER_API_URL = 'https://api.yescaptcha.com/createTask'
CAPTCHA_RESOLVER_API_KEY = env.str('CAPTCHA_RESOLVER_API_KEY')

CAPTCHA_DEMO_URL = 'https://www.google.com/recaptcha/api2/demo'

CAPTCHA_ENTIRE_IMAGE_FILE_PATH = 'captcha_entire_image.png'
CAPTCHA_SINGLE_IMAGE_FILE_PATH = 'captcha_single_image.png'
CAPTCHA_RESIZED_IMAGE_FILE_PATH = 'captcha_resized_image.png'

import json
CAPTCHA_TARGET_NAME_QUESTION_ID_MAPPING = {
    "taxis": "/m/0pg52",
    "bus": "/m/01bjv",
    "school bus": "/m/02yvhj",
    "motorcycles": "/m/04_sv",
    "tractors": "/m/013xlm",
    "chimneys": "/m/01jk_4",
    "crosswalks": "/m/014xcs",
    "traffic lights": "/m/015qff",
    "bicycles": "/m/0199g",
    "parking meters": "/m/015qbp",
    "cars": "/m/0k4j",
    "vehicles": "/m/0k4j",
    "bridges": "/m/015kr",
    "boats": "/m/019jd",
    "palm trees": "/m/0cdl1",
    "mountains or hills": "/m/09d_r",
    "fire hydrant": "/m/01pns0",
    "fire hydrants": "/m/01pns0",
    "a fire hydrant": "/m/01pns0",
    "stairs": "/m/01lynh",
    "出租车": "/m/0pg52",
    "巴士": "/m/01bjv",
    "摩托车": "/m/04_sv",
    "机动车": "/m/0k4j",
    "小轿车": "/m/0k4j",
    "拖拉机": "/m/013xlm",
    "烟囱": "/m/01jk_4",
    "人行横道": "/m/014xcs",
    "红绿灯": "/m/015qff",
    "自行车": "/m/0199g",
    "停车计价表": "/m/015qbp",
    "汽车": "/m/0k4j",
    "桥": "/m/015kr",
    "船": "/m/019jd",
    "棕榈树": "/m/0cdl1",
    "山": "/m/09d_r",
    "消防栓": "/m/01pns0",
    "楼梯": "/m/01lynh",
    "交通工具": "/m/0k4j",
    "公交车": "/m/01bjv",
    "彩色玻璃": "/m/011y23",
    "火车站": "/m/0py27",
    "消火栓": "/m/01pns0",
    "过街人行道": "/m/014xcs",
    "车库门": "/m/08l941",
    "公交站": "/m/01jw_1",
    "停车计时器": "/m/015qbp",
    "丘陵": "/m/09d_r",
    "车辆": "/m/0k4j",
    "公共汽车": "/m/01bjv",
    "交通灯": "/m/015qff",
    "停车咪表": "/m/015qbp"
}