def solver_loop(X, tsteps=1, dx=0.25, dt=0.001, gamma = 1.):

    for i in range(tsteps):
        X = ch_solver(X, dx=0.25, dt=0.001, gamma = 1.)
    return X
    
def FieldConcentration(X,sample_id=0):
    if X.ndim == 3:
        try:
            return np.sum(X[sample_id])
        except IndexError:
            print("Requested Sample # %d exceeds data size" % (sample_id+1))
    else:
        return np.sum(X)

def FreeEnergy(X, sample_id = 0):
    phi = X[sample_id]
    phi_x, phi_y = np.gradient(phi)
    FE  = phi_x**2+phi_y**2+((phi**2-1)**2)*0.25
    return np.sum(FE)
