import matplotlib.pyplot as plt

def displayField(X, sample_id = 0):
    if X.ndim == 3:
        try:
            print("Displaying field #")
            im = plt.imshow(X[sample_id][:][:])
            plt.show(im)
        except IndexError:
            print("Requested Sample # %d exceeds data size" % (sample_id+1))
    else:
        im = plt.imshow(X[:][:])
        plt.show(im)
    return None
