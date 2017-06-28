# PandasMongoDB


## Installation
```python
pip install git+http://github.com/tschm/PandasMongoDB.git
```

## Run a MongoDB Server
```
docker run -v /my/own/datadir:/data/db -d mongo
```
## Quickstart
```python
import numpy as np
import pandas as pd
from mongoengine import connect

from pyPandasMongo.frame import load, store

if __name__ == '__main__':
    # connect to your fav. Mongo Server
    connect(db="Experiments", host="quantsrv", port=27017, alias="default")

    # write data
    f = store(name="history", object=pd.DataFrame(data=np.random.randn(2000,2000)), metadata={"A": "Thomas"})
    print(f.metadata)
    print(f.frame)

    # read data
    f = load(name="history")
    print(f.frame)
    print(f.metadata)
    
    # works also for a Series and without any meta-data
    g = store(name="random series", object=pd.Series(index=[1,2,3], data=[1,2,3]))
    print(load(name="random series").frame)
```
