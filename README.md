# Password-Strength-Analysis-ML
Password Strength Analysis using Machine Learning technique

### Dataset
The passwords used in our analysis are from [000webhost leak](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/000webhost.txt) that is available online. But the labels of this dataset used for model development has two versions, the difference lies in how it is labelled.
- V1: Original dataset from Kaggle [here](https://www.kaggle.com/bhavikbb/password-strength-classifier-dataset)
- V2: Using [zxcvbn](https://github.com/XinbeiGong/Password-Strength-Analysis-ML.git) and [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python) to relabel all passwords (this tool based on how many times it need to crack a given password)

### Model
Saved model for dataset V1: `clf_svm_v1.model`  
Saved model for dataset V2: `clf_svm_v2.model`

### Conclusion
Using dataset v1 to train the model can get very high accuracy

### Inference
You can use the following command to do inference for your passwords, and this based on dataset v1
 ```
 Run infer.py -i <your password>

e.g. python infer.py -i J1982awahAR arrahmane1000assamad hsy000

Output:
strength of the input passwords:
J1982awahAR: fair
arrahmane1000assamad: hard
hsy000: weak
 ```
### Reference
1. https://www.kaggle.com/senthamizhan/starter-password-strength-classifier-d9455d57-b
