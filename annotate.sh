cat webcam02_2014-08-29_19-48.jpg | convert - \
  -gravity southeast -pointsize 32 -background '#00000080' -fill white  label:' webcam.hollersbach.eu ' -composite \
  -gravity northwest -pointsize 32 -background '#00000080' -fill white  label:" Landhaus Nindl - Hollersbach " -composite \
  -gravity northwest -pointsize 26 -background '#00000080' -fill white  label: %[EXIF:*GPS*]  -geometry +0+37 -composite \
  - > out2.jpg
