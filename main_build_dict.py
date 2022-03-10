import argparse

from data_loader_json import DataLoader

# import tf.io.gfile.GFile

parser = argparse.ArgumentParser(description='CUTIE parameters')
#parser.add_argument('--dict_path', type=str, default='dict/newtest')
parser.add_argument('--dict_path', type=str, default='CutieMLproject/dict/Data_centric_genuine')#40000
#parser.add_argument('--doc_path', type=str, default='data/SROIE')
#parser.add_argument('--dict_path', type=str, default='dict/TEST')
parser.add_argument('--doc_path', type=str, default='CutieMLproject/Data_centric_genuine/train')
parser.add_argument('--test_path', type=str, default='CutieMLproject/Data_centric_genuine/test')
parser.add_argument('--text_case', type=bool, default=True) # case sensitive
parser.add_argument('--tokenize', type=bool, default=True) # tokenize input text
parser.add_argument('--batch_size', type=int, default=4)
parser.add_argument('--use_cutie2', type=bool, default=True)
params = parser.parse_args()

#img_array = np.load('20000T_classes.npy')


if __name__ == '__main__':
    ## run this program before training to create a basic dictionary for training
    data_loader = DataLoader(params, update_dict=True, load_dictionary=False)
