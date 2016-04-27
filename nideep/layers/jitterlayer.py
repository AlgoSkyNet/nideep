import caffe
import numpy as np
from scipy.ndimage.interpolation import shift

class JitterLayer(caffe.Layer):

    def setup(self, bottom, top):
        # check input
        if len(bottom) != 1:
            raise Exception("Need one input to apply jitter.")
        self.shift_h = 1

    def reshape(self, bottom, top):
        top[0].reshape(1, *bottom[0].data.shape)

    def forward(self, bottom, top):
        
        #shift_h = np.random.
        top[0].data[...] = shift(bottom[0].data, [0, 0, self.shift_h, 0])
        #mu = np.mean(top[0].data[:,:,0:self.shift_h, :]
        #top[0].data[:,:,0:self.shift_h, :] = np.random.randn()
        print "b", bottom[0].data
        print "t", top[0].data

    def backward(self, top, propagate_down, bottom):
        pass # no backward pass
