import pickle

#
# cars=['BMZ','KLJJ','OJKK','TYJUHNJJJ']
# file="mycars.pkl"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "mycars.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
