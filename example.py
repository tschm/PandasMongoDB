import numpy as np
import pandas as pd
from mongoengine import connect

from pyPandasMongo.frame import frame

if __name__ == '__main__':
    # connect to your fav. Mongo Server
    connect(db="Experiments", host="quantsrv", port=27017, alias="default")

    # write data
    # -----------------------------------------------------------------------------------------------------------------
    # write a Pandas DataFrame to it
    frame(name="history").put(frame=pd.DataFrame(data=np.random.randn(2000,2000)))
    frame(name="random series").put(frame=pd.Series(data=[1,2,3], index=["A","B","C"]))

    # read data
    # -----------------------------------------------------------------------------------------------------------------
    print(frame(name="history").frame)
    print(frame(name="random series").frame)
