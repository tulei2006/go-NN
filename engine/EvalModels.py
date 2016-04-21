import tensorflow as tf
from Layers import *

class Conv11PosDepFC1ELU: 
    def __init__(self, N, Nfeat):
        self.train_dir = "/home/greg/coding/ML/go/NN/work/train_dirs/conv12posdepELU_N%d_fe%d" % (N, Nfeat)
        self.N = N
        self.Nfeat = Nfeat
    def inference(self, feature_planes, N, Nfeat):
        NK = 256
        NKfirst = 256
        Nfc = 256
        conv1 = ELU_conv_pos_dep_bias(feature_planes, 5, Nfeat, NKfirst, N, 'conv1')
        conv2 = ELU_conv_pos_dep_bias(conv1, 3, NKfirst, NK, N, 'conv2')
        conv3 = ELU_conv_pos_dep_bias(conv2, 3, NK, NK, N, 'conv3')
        conv4 = ELU_conv_pos_dep_bias(conv3, 3, NK, NK, N, 'conv4')
        conv5 = ELU_conv_pos_dep_bias(conv4, 3, NK, NK, N, 'conv5')
        conv6 = ELU_conv_pos_dep_bias(conv5, 3, NK, NK, N, 'conv6')
        conv7 = ELU_conv_pos_dep_bias(conv6, 3, NK, NK, N, 'conv7')
        conv8 = ELU_conv_pos_dep_bias(conv7, 3, NK, NK, N, 'conv8')
        conv9 = ELU_conv_pos_dep_bias(conv8, 3, NK, NK, N, 'conv9')
        conv10 = ELU_conv_pos_dep_bias(conv9, 3, NK, NK, N, 'conv10')
        conv11 = ELU_conv_pos_dep_bias(conv10, 3, NK, NK, N, 'conv11')
        conv11_flat = tf.reshape(conv11, [-1, NK*N*N])
        fc = ELU_fully_connected_layer(conv11_float, NK*N*N, Nfc)
        score = tf.tanh(linear_layer(fc, Nfc, 1))
        return score