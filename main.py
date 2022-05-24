
from app.settings import CAPTCHA_DEMO_URL
from app.solution import Solution


if __name__ == '__main__':
    Solution(CAPTCHA_DEMO_URL).resolve()
