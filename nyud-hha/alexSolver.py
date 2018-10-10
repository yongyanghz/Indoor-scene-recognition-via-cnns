import sys
import caffe
import os
import PIL
import scipy.io as sio

caffe.set_mode_cpu()
solver = None  # ignore this workaround for lmdb data (can't instantiate two solvers on the same data)
solver = caffe.SGDSolver('solver.prototxt')

weights = '/home/yongyang/CVProjects/nyud/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
solver.net.copy_from(weights)
