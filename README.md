# Password-Strength-Analysis-ML
Password Strength Analysis using Machine Learning technique

### Dataset
The passwords used in our analysis are from [000webhost leak](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/000webhost.txt) that is available online. But the labels of this dataset used for model development has two versions, the difference lies in how it is labelled.
- Origin dataset from Kaggle [here](https://www.kaggle.com/bhavikbb/password-strength-classifier-dataset)
- Using [zxcvbn](https://github.com/XinbeiGong/Password-Strength-Analysis-ML.git) and [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python) to relabel all passwords


### Inference
 ```
 Run infer.py -i <your password>

e.g. python infer.py -i J1982awahAR arrahmane1000assamad hsy000

Output:
strength of the input passwords:
J1982awahAR: fair
arrahmane1000assamad: hard
hsy000: weak
 ```
