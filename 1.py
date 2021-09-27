import os


def save_ckpt(sess, path, save_prefix, data_loader, network, num_words, num_classes, iter):
    ckpt_path = os.path.join(path, save_prefix)
    if not os.path.exists(ckpt_path):
        os.makedirs(ckpt_path)
    filename = os.path.join(ckpt_path, network.name + '_d{:d}c{:d}(r{:d}c{:d})_iter_{:d}'.
                            format(num_words, num_classes, data_loader.rows_ulimit, data_loader.cols_ulimit,
                                   iter) + '.ckpt')
    ckpt_saver.save(sess, filename)
    print('\nCheckpoint saved to: {:s}\n'.format(filename))