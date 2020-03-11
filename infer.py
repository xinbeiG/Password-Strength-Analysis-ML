import pickle
import pandas as pd
import string
import argparse

# usage: python infer.py -i J1982awahAR arrahmane1000assamad hsy000
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i','--input', dest='password', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()
password = args.password


def preprocess(lst):
    df1 = pd.DataFrame(lst,columns=['password'])
    df1['length'] = df1['password'].str.len()
    df1['numerics'] = df1['password'].apply(lambda x: len([str(x) for x in list(x) if str(x).isdigit()]))
    df1['alpha'] = df1['password'].apply(lambda x: len([x for x in list(x) if x.isalpha()]))
    df1['lowercase'] = df1['password'].apply(lambda x: len([x for x in list(x) if x.islower()]))
    df1['uppercase'] = df1['password'].apply(lambda x: len([x for x in list(x) if x.isupper()]))
    df1['punctuation'] = df1['password'].apply(lambda x: len([x for x in list(x) if x in string.punctuation]))
    
    X = df1.drop('password', axis = 1)
    X_tr = loaded_scaler.transform(X)
    return X_tr

def displayResult(lst, res):
    print("strength of the input passwords:")
    for i in range(len(lst)):
        if res[i] == 0:
            label = "weak"
        elif res[i] == 1:
            label = "fair"
        elif res[i] == 2:
            label = "hard"
        print(f"{lst[i]}: {label}")


# load the model and scaler variable from disk
loaded_model = pickle.load(open('./clf_svm_v1.model', 'rb'))
loaded_scaler = pickle.load(open('./my_scaler.pkl', 'rb'))

X = preprocess(args.password)
y_pred = loaded_model.predict(X)
displayResult(password, y_pred)