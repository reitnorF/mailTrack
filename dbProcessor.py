import pickle
import re
from convertdate import islamic
import datetime
from openpyxl import Workbook
import roman




suratKeluar_list = list()
with open('suratKeluar','rb') as f:
	suratKeluar_list = pickle.load(f)

def getMaxSuratID(listOfSurat):
	length = len(listOfSurat)
	last = listOfSurat[length-1]
	nomorSurat = last["nomor"]
	match = re.match("(\A[0-9]+)",nomorSurat)
	suratID = int(match.group(1))
	return suratID


print getMaxSuratID(suratKeluar_list)	



