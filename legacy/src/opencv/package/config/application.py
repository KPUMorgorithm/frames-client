##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

# OpenCV configuration

# Haar cascade
HAARCASCADE_FRONTALFACE_DEFAULT_PATH = './src/opencv/cascade' \
                                       '/haarcascade_frontalface_default.xml'

# Caffe deploy Prototxt
PROTOTEXT_PATH = './src/opencv/dnn/prototxt' \
                 '/deploy.prototxt.txt'

# Caffe model
MODEL_PATH = './src/opencv/dnn/model' \
             '/res10_300x300_ssd_iter_140000.caffemodel'

# Default confidence
CONFIDENCE = 0.3
