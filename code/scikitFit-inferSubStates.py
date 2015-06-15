import numpy as np
import pandas as pd
import pickle
import sys
from sklearn.hmm import GaussianHMM
from sklearn import cluster
from sklearn import mixture
import sklearn
from subprocess import call

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

print "Scikit version:", sklearn.__version__
if not sklearn.__version__.startswith("0.15"):
    print "ERROR: Version 0.15 of scikit is needed to run this script."
    sys.exit()

if len(sys.argv) == 1:
    print("\nUsage: python scripts/scikitFit-inferSubStates.py <state to substate>\n")
    print("Note: this script has been originally run with scikit version 0.13.\nIt may or may not work with a different version of scikit.")
    sys.exit()

stateNum = int(sys.argv[1])
numReps = 10
maxSubstates = 5

print "State to be split:", stateNum
sys.stdout.flush()

basepath = "BG3Kc-11states-state"

# load data
indata = pd.read_csv("data/substates/%s%d.csv" % (basepath,stateNum))
grouped = indata.groupby('regions')

# number of data columns
num_data = indata.shape[1] - 1

data = []
for state, record in grouped:
    r = record.iloc[:,0:num_data]
    data.append(r.as_matrix())

# save the actual object
def saveobject(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


for numState in range(2, maxSubstates+1):
    
    # make the output directory
    call(["mkdir", "-p", "data/substates/%s%d/%d" % (basepath,stateNum,numState)])
    
    # do the replicates
    for repInx in range(0, numReps):
        print "Doing replicate", repInx, "/", numReps, "with", numState, "states"
        sys.stdout.flush()
        
        # cluster all the available data and use that as initial point
        means = cluster.KMeans(n_clusters=numState).fit(indata.iloc[:,0:num_data]).cluster_centers_
        cv = np.cov(indata.iloc[:,0:num_data].T)
        covars = mixture.distribute_covar_matrix_to_match_covariance_type(cv, "tied", num_data)
        covars[covars==0] = 1e-5
        
        model = GaussianHMM(numState, covariance_type="tied", n_iter=1000, init_params='abdefghijklnopqrstuvwxyzABDEFGHIJKLNOPQRSTUVWXYZ')
        model.means_ = means
        model.covars_ = covars
        
        print("Fitting model...")
        sys.stdout.flush()
        model.fit(data)

        print("Decoding states...")
        sys.stdout.flush()
        # do a loop over everything and record in one long array
        states = np.array([])
        score = 0
        for i in range(0, len(data)):
            hidden_states = model.decode(data[i])
            states = np.append(states, hidden_states[1])
            score = score + model.score(data[i])

        print("Saving data...")
        sys.stdout.flush()

        # save the states and LLH
        np.savetxt("data/substates/%s%d/%d/rep_%d_states.txt" % (basepath,stateNum,numState,repInx), states, fmt="%d")
        with open("data/substates/%s%d/%d/rep_%d_LLH.txt" % (basepath,stateNum,numState,repInx), 'w') as f:
        	f.write(str(score))
	
        saveobject(model, "data/substates/%s%d/%d/rep_%d.pk" % (basepath,stateNum,numState,repInx))    
        
