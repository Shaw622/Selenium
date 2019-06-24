#! /usr/bin/env python3

from selenium import webdriver

# GoogleChromeを指定して起動
browser = webdriver.Chrome()
browser.get('https://mainichi.jp/')
