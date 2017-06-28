# PandasMongoDB

Store your Pandas objects in a database.

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
## Concept
It is possible to convert Pandas DataFrames into dictionaries (e.g. Mongo Documents).
However, the sad truth is that MongoDB is rather slow when performing queries over thousands of documents.
There is also an upper limit on the size of a document. It's currently 16MB. This makes
MongoDB often a poor choice for timeseries data. 

Here we go a different approach following the [arctic project](https://github.com/manahl/arctic) released by Man AHL.
Rather than converting a Frame into a dictionary we concert the frame into a massive ByteStream.
We store essentially only links to files in the database. We rely here on a technology called GridFS.
All of this happens in the background and is abstracted away using the FileField of MongoEngine.

We offer only a tiny subset of the arctic project in this lightweight solution.
