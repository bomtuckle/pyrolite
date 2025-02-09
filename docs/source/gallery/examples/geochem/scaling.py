"""
Unit Scaling
=============
"""
import pandas as pd

import pyrolite.geochem

pd.set_option("display.precision", 3)  # smaller outputs
########################################################################################
from pyrolite.util.synthetic import normal_frame

df = normal_frame(
    columns=["CaO", "MgO", "SiO2", "FeO", "Ni", "Ti", "La", "Lu", "Mg/Fe"]
)
########################################################################################
cols = ["Ni", "NiO", "La", "La2O3"]
df.head(2).pyrochem.convert_chemistry(to=cols)[cols]  # these are in ppm!
