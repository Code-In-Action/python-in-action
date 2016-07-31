#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from PIL import Image, ImageDraw, ImageFont
def add_number(num):
    im = Image.open('tx.png')
    txt = Image.new('RGBA', im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('arial.ttf, 40')
    d = ImageDraw.Draw(txt)
    d.text((im.size[0]-50, 5), str(num), font=fnt, fill=(255,0,0,255))
    out = Image.alpha_composite(im, txt)
    out.show()
    out.save("tx_"+str(num)+'.png')

if __name__ == '__main__':
    add_number(42)