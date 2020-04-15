import gzip
import pickle

with open('full_dataset_final.pkl', 'rb') as f:
    data = pickle.load(f)