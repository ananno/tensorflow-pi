import time
import tensorflow as tf
import multiprocessing as mp

st_time = time.time()
total_core = mp.cpu_count()

batch_size = 2000000000
total_itr = batch_size

st1 = 3
st2 = 5
val1 = val2 = val3 = val4 = 0.0

with tf.device('/gpu:0'):
    p1 = tf.placeholder(dtype=tf.float64, shape=None, name='denominator')
    tf_list1 = tf.range(st1, total_itr, 4, dtype=tf.float64)
    tf_var1 = tf.Variable(0.0, dtype=tf.float64)
    cal_op1 = tf.divide(tf.constant(1.0, dtype=tf.float64), tf_list1)
    tf_var1 = tf.add(tf_var1, cal_op1)

# with tf.device('gpu:1'):    # Enable this line if there are two GPUs
    p2 = tf.placeholder(dtype=tf.float64, shape=None, name='multiplier')
    tf_list2 = tf.range(st2, total_itr, 4, dtype=tf.float64)
    tf_var2 = tf.Variable(0.0, dtype=tf.float64)
    cal_op2 = tf.divide(tf.constant(1.0, dtype=tf.float64), tf_list2)
    tf_var2 = tf.add(tf_var2, cal_op2)

init = tf.global_variables_initializer()

gpu_config = tf.ConfigProto(allow_soft_placement=True)
gpu_config.gpu_options.per_process_gpu_memory_fraction = 0
gpu_config.gpu_options.allow_growth = True

sess = tf.Session(config=gpu_config)
sess.run(init)

batch_count = 0
print("Total polynomial size : %s" % total_itr)
print("Batch size : %s" % batch_size)
print("Starting ...")
feed_dict = {}

while True:
    batch_count += 1

    with tf.device('/gpu:0'):
        sess.run([tf_list1, cal_op1, tf_var1], feed_dict=feed_dict)
        final1 = tf.reduce_sum(cal_op1)
        val3 = sess.run(final1, feed_dict=feed_dict)
        st1 += batch_size
        total_itr += batch_size
        tf_list1 = tf.range(st1, total_itr, 4, dtype=tf.float64)

    # with tf.device('/gpu:1'): # Enable this line if there are two GPUs
        sess.run([tf_list2, cal_op2, tf_var2], feed_dict=feed_dict)
        final2 = tf.reduce_sum(cal_op2)
        val4 = sess.run(final2, feed_dict=feed_dict)
        st2 += batch_size
        tf_list2 = tf.range(st2, total_itr, 4, dtype=tf.float64)

    val5 = val4 - val3

    result = 4.0 * (1 + val5)
    print('Batch %s (%s) : %s' % (batch_count, total_itr, result))

    print('Time taken : %f secs' % (time.time() - st_time))
    st_time = time.time()

