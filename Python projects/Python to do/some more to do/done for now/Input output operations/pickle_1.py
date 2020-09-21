import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1,'Pulling the rug'),
           (2,'Psycho'),
           (3,'Mayhem'),
           (4,'Kentish')))

with open("imelda.pickle","wb")as pickle_file:
    pickle.dump(imelda,pickle_file)

