import torch
import tensorflow.compat.v1 as tf
import numpy as np
import torch.nn as nn


def tensorflow_test_template():
    x = tf.placeholder(tf.float32, shape=[4, 128, 416, 1])
    #y = function_to_be_test(x)

    initialize_op = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(initialize_op)

    x_vars = np.random.rand(4, 128, 416, 1)

    r = sess.run(y, feed_dict={x: x_vars})
    #print(y.shape)
    #print(r)
    pass

def pytorch_test_template():
    image = torch.randn(4, 6, 128, 416)  # 输入尺寸 [N C H W]
    # function to be test
    pass



def demo_logical_and():
    x = torch.Tensor([True, False, True, False])
    y = torch.Tensor([True, True, False, False])
    z = x.mul(y).bool()  # tensor([ True, False, False, False])
    print(z)
    pass

def demo_reduce_all():
    x = torch.Tensor([[True, True, False, False], [False, True, False, True]])

    z = x.prod(dim=0).bool()
    print(z)


    pass

if __name__ == '__main__':
    demo_reduce_all()
    pass
