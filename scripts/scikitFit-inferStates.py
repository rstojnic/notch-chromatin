import numpy as np
import pickle
import sys
from sklearn.hmm import GaussianHMM
import sklearn

print "Scikit version:", sklearn.__version__
sys.stdout.flush()

if len(sys.argv) == 1:
    print("\nUsage: python scripts/scikitFit-inferStates.py <number of states>\n")
    print("Note: this script has been originally run with scikit version 0.13.\nIt may or may not work with a different version of scikit.")
    sys.exit()

print "Number of states:", sys.argv[1]

print("Loading data...")
sys.stdout.flush()
data = np.loadtxt("data/scikit-BG3Kc-K56ac.tsv", skiprows=1)
model = GaussianHMM(int(sys.argv[1]), covariance_type="tied", n_iter=1000)

print("Fitting model...")
sys.stdout.flush()
model.fit([data])

print("Decoding states...")
sys.stdout.flush()

hidden_states = model.decode(data)
llh = model.score(data)

print("Saving data...")
sys.stdout.flush()

# save the states and LLH
np.savetxt("scikit-states-all.txt", hidden_states[1], fmt="%d")
np.savetxt("scikit-states-all-LLH.txt", [llh], fmt="%f")
	
# save the actual object
def saveobject(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

saveobject(model, r'scikit-model.pk')

# to open
# with open('scikit-model.pk', 'rb') as input:
# 	model = pickle.load(input)


