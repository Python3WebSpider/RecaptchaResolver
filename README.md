# RecaptchaResolver

Recaptcha Resolver

## Usage

Clone this repo:

```
git clone https://github.com/Python3WebSpider/RecaptchaResolver.git
```

Then go to https://yescaptcha.com/i/CnZPBu and register your account, then get a `clientKey` from portal.

![image](https://user-images.githubusercontent.com/8678661/170099424-bbe53c64-79b5-46fc-a7c9-95fc88877e3d.png)

Then create a `.env` file in root of this repo, and write this content:

```
CAPTCHA_RESOLVER_API_KEY=<Your Client Key>
```

Next, you need to install packages:

```
pip3 install -r requirements.txt
```

At last, run demo:

```
python3 main.py
```

Result:

![image](https://user-images.githubusercontent.com/8678661/170100015-f08385e6-7990-4300-831d-b429cd7f9329.png)

