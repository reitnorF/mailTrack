import json
import openpyxl
import string
import pickle

wb = openpyxl.load_workbook('a.xlsx')
a = wb.active
suratKeluar = list()
idSuratKeluar = 1
for x in range (5,1157):
	surat=dict()
	surat["ID"] = idSuratKeluar
	surat["dari_orang"] = a['B'+str(x)].value
	surat["dari_institusi"] = a['C'+str(x)].value
	surat["dari_jabatan"] = a['D'+str(x)].value
	surat["ke_nama"] = a['E'+str(x)].value
	surat["ke_institusi"] = a['F'+str(x)].value
	surat["ke_jabatan"] = a['G'+str(x)].value
	surat["ke_alamat"] = a['H'+str(x)].value
	surat["judul"] = a['I'+str(x)].value
	surat["nomor"] = a['J'+str(x)].value
	surat["tanggal"] = a['K'+str(x)].value
	surat["penandatangan"] = a['L'+str(x)].value
	surat["diketahui_direktur_eksekutif"] = a['M'+str(x)].value
	surat["tanggal_diserahkan"] = a['N'+str(x)].value
	surat["diambil_oleh"] = a['O'+str(x)].value
	surat["keterangan"] = a['P'+str(x)].value
	idSuratKeluar += 1
	suratKeluar.append(surat)
with open("suratKeluar","wb") as f:
	pickle.dump(suratKeluar,f)


	