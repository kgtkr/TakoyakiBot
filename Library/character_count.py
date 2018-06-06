# coding: utf-8

import unicodedata
import os


def count_characters(text):

    count = 0

    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1
    
    count += text.count(os.linesep)

    return count


def check_text_length(text):

    count = count_characters(text)

    if count > 270:
        text = text[:260] + "..文字数((ry"

    return text
