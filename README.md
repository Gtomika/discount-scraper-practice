## Discount scraper

Just a practice app that scrapes discounts from Tesco website and sends them as email.

If the Tesco site HTML structure changes, this app will no longer function.

## Install packages

Make sure pip is up to date:

```
python -m pip install --upgrade pip
```

Install required packages:

```
python -m pip install requests
python -m pip install pyyaml
python -m pip install bs4
```

## Setup Gmail to be able to send your mails

Have Google account (gmail). Go to [app passwords](https://myaccount.google.com/u/4/apppasswords), 
and create new app password for this app.

Then set the following values as environmental variables:

 - `SOURCE_EMAIL`: Gmail address that you configured app passoword for.
 - `SOURCE_EMAIL_APP_PASSWORD`: The app password.
 - `TARGET_EMAIL`: Who you want to send to.