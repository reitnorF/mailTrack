import pickle
import re
from convertdate import islamic
import datetime



suratKeluar = list()
with open('suratKeluar','rb') as f:
	suratKeluar = pickle.load(f)



for x in suratKeluar:
	print x