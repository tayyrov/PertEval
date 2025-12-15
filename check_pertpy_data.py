
import pertpy
from pertpy import data as scpert_data

print("Attributes in pertpy.data:")
for attr in dir(scpert_data):
    if not attr.startswith("_"):
        print(attr)
