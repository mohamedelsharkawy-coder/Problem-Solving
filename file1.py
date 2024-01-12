# this is file 1 
print(__name__) # in this file main else will be the same name of it 

if __name__ == '__main__':
    print('File is run direclty')

else:
    print('File is imported From another file')