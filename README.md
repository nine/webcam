# Webcam helper scripts

## daylight.py

Dependency installation instructions:
```
aptitude install python3 python3-pip
pip3 install ephem
```

Usage:
```
#!/bin/bash

if ./daylight --lon 12.00000 --lat 47.00000 --ele 400; then
  # capture image here
fi

#eof

```
