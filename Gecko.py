#! /usr/bin/env python3

from selenium import webdriver

# Firefoxを指定して起動
browser = webdriver.Firefox()
browser.get('http://toyokeizai.net/')
