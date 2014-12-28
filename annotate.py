#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys
from datetime import datetime
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def readStdinBinary():
  return sys.stdin.buffer.read()

def main():
  img_binary = readStdinBinary()
  with Drawing() as draw:
    with Image(blob=img_binary) as img:
      draw.font_size = 32
      draw.fill_color = Color('#ffffff')
      draw.text_under_color = Color('#00000080')
      draw.gravity = "north_west"
      draw.text(0, 0, u' Landhaus Nindl – Hollersbach im Pinzgau ')

      draw.gravity = "south_east"
      draw.text(0, 0, u' webcam.hollersbach.eu ')

      # exif timestamp example:
      # 2014:08:29 17:49:00
      img_time = datetime.strptime(img.metadata['exif:DateTimeOriginal'], '%Y:%m:%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
      draw.gravity = "north_west"
      draw.font_size = 26
      draw.text(0, 38, ' ' + img_time + ' ')

      draw(img)

      jpeg_bin = img.make_blob('jpeg')
      sys.stdout.buffer.write(jpeg_bin)


if __name__ == '__main__':
  main()


#eof
