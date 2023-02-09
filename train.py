import numpy as np
from sklearn.decomposition import PCA
import os
import pickle as pk
import  pandas as pd

from data import LoadData


class TD:
  
  def __init__(self):
    """"
    Original Data Set
    224*224 = 50176 values in one image

    [168 150 137 ... 227 243 248]
    """
    self.Data, self.Label = LoadData()
    self.Data = np.asarray(self.Data)
    self.Label = np.asarray(self.Label)


  def train(self):
    print(f"number of images: {len(self.Data)}")
    print("Before PCA Transform")
    print(self.Data)
    print(f"number of values in one image: {len(self.Data[0])}")

    self.pca = PCA(n_components=0.9)
    self.trainDataS = self.pca.fit_transform(self.Data)

    print("After PCA Transform")
    print(self.trainDataS)
    print(f"number of values in one image: {len(self.trainDataS[0])}")
    """
    PCA Transform
    0.9 -> 10 values in one image

    [ 11312.26086973  2283.70464563   788.50317713  -936.93123612
      10767.52238881  -1138.2489218   269.6564662   -690.08832049
      -960.30505439   -524.99817064
    ]
    """
  
  def save_train_data(self):
    pk.dump(self.pca, open(f"pca.pkl","wb"))
    pk.dump(self.trainDataS, open(f"trainDataS.pkl","wb"))
    pd.DataFrame(np.asarray(self.trainDataS)).to_csv(f"trainDataS.csv")


if __name__ == "__main__":
  td = TD()
  td.train()
  td.save_train_data()