# RecaptchaResolver

Recaptcha Resolver

## Usage

### Clone

Clone this repo:

```
git clone https://github.com/Python3WebSpider/RecaptchaResolver.git
```

### Set Client Key

Go to https://yescaptcha.com/i/CnZPBu and register your account, then get a `clientKey` from portal.

![image](https://user-images.githubusercontent.com/8678661/170099424-bbe53c64-79b5-46fc-a7c9-95fc88877e3d.png)

Then create a `.env` file in root of this repo, and write this content:

```
CAPTCHA_RESOLVER_API_KEY=<Your Client Key>
```

### Install packages

```
pip3 install -r requirements.txt
```

### Run demo

```
python3 main.py
```

