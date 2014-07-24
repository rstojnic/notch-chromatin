Scripts to derive chromatin states
================

These two Python scripts were used to derive the chromatin states.

* [scikitFit-inferStates.py](https://github.com/rstojnic/notch-chromatin/blob/master/scripts/scikitFit-inferStates.py) - this script is used to infer the chromatin states. Please run as following:

```
$ python scripts/scikitFit-inferStates.py 11
```

after unpacking the .7z files from the data/ directory. Note that this script uses Kmeans initialisation with a random seed, so the result will be different every time the script is run. To obtain the local optimum run multiple times (e.g. 30) and retain the model with the largest log-likelihood (both of which are written as output to the current directory). 

* [scikitFit-inferSubStates.py](https://github.com/rstojnic/notch-chromatin/blob/master/scripts/scikitFit-inferStates.py) - this script is used to infer the chromatin substates. Please run as following:

```
$ python scripts/scikitFit-inferSubStates.py 4
```

to further split State 4. For this to work you will have to unpack the files in data/substates. The script will split the state into 2-5 substates using 10 initial points. 

## Scikit version

The first script requires scikit >= 0.13, while the second requires scikit >= 0.15. Please note that the second script will not work on an earlier version of scikit due to a [bug](https://github.com/scikit-learn/scikit-learn/issues/1817). The HMM submodule of scikit is currently marked for deprecation and is scheduled to be removed from the core scikit library in version 0.17. 
