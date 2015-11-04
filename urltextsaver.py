#!/usr/bin/env python
import os
import sys
from md5 import md5
from  datetime import datetime

import argparse

import requests
import peewee

import html2text


class BaseModel(peewee.Model):
    class Meta:
        db = peewee.SqliteDatabase("db")

class Link(BaseModel):
    url = peewee.CharField(max_length=255)


class Tag(BaseModel):
    name = peewee.CharField(max_length=20)


class Page(BaseModel):
    body = peewee.TextField()


class Item(BaseModel):
    link = peewee.ForeignKeyField(Link)
    page = peewee.ForeignKeyField(Page)
    created = peewee.DateTimeField(default=datetime.now)


class Manager(object):

    def __init__(self, dbpath=""):

        for model in [Link, Tag, Page, Item]:
            model.create_table(fail_silently=True)

    def put_link(link):
        pass

    def get_page_by_tags(tags):
        pass

def retrive_html(url):
    handle = requests.get(url)
    html = handle.content.decode(handle.encoding)
    return html

def main():
    manager = Manager()
    url = sys.argv[1]
    html = retrive_html(url)
    # import ipdb; ipdb.set_trace()
    text = html2text.html2text(html)
    id_ = md5(text.encode('utf-8')).hexdigest()
    with open(os.path.join("pages",id_), "wt") as f:
        f.write(text.encode('utf-8'))

if __name__ == "__main__":
    main()
