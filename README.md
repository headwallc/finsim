# Toolkit for bootstrapped investment analysis

## Introduction

`finsim` is a financial return simulation package.

Returns after _k_ years are simulated by bootstrapping the distribution from provided historic index records. 
Expected returns of financial products such as IULs with a _floor_, _cap_ and / or _spread_ can be simulated given a specific historic index return.

### Background

- [What Will The S&P 500 Return Over The Next 10 Years?](https://app.finimize.com/content/Q29udGVudFBpZWNlOjUyMzg=/what-will-sp-500-return-over-next-10-years)
- [Average returns of the S&P 500](https://www.investopedia.com/ask/answers/042415/what-average-annual-return-sp-500.asp)
- [Book Review: Mark Spitznagel’s Thoroughly Excellent “Safe Haven”](https://www.forbes.com/sites/johntamny/2021/08/17/book-review-mark-spitznagels-thoroughly-excellent-safe-haven/?sh=4c2d7e1f32d4)
- [Safe Haven: Investing for Financial Storms](https://www.wiley.com/en-us/Safe+Haven:+Investing+for+Financial+Storms-p-9781119401797)

## Setup

Prerequisites:
- python 3.9
- `virtualenv` installed

Create a virtual environment and load requirements:
    
        $ virtualenv -p python3.9 venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt

Run preconfigured simulation:

        $ python run.py

Copyright: Headwall LLC, Ca, USA

Author: Andreas Hoelzl

