import json
import openpyxl
import string
import pickle


wb = openpyxl.load_workbook('b.xlsx')
a = wb.active


suratMasuk = list()
idSuratMasuk = 1

for x in range (5,222):
	surat=dict()
	surat["ID"] = idSuratMasuk
	surat["dari_orang"] = a['B'+str(x)].value
	surat["dari_institusi"] = a['C'+str(x)].value
	surat["dari_alamat"] = a['D'+str(x)].value
	surat["dari_kontak"] = a['E'+str(x)].value
	surat["dari_jabatan"] = a['F'+str(x)].value
	surat["ke_orang"] = a['G'+str(x)].value
	surat["ke_bidang"] = a['H'+str(x)].value
	surat["ke_jabatan"] = a['I'+str(x)].value
	surat["judul"] = a['J'+str(x)].value
	surat["ringkasan"] = a['K'+str(x)].value
	surat["nomor_surat"] = a['L'+str(x)].value
	surat["tanggal_surat"] = a['M'+str(x)].value
	surat["nomor_agenda"] = a['N'+str(x)].value
	surat["tanggal_terima"] = a['O'+str(x)].value
	surat["surat_diambil_oleh"] = a['P'+str(x)].value
	surat["keterangan"] = a['Q'+str(x)].value
	idSuratMasuk += 1
	suratMasuk.append(surat)
	print surat


#for x in suratKeluar:
	#print x["judul"]
	

with open("suratMasuk","wb") as f:
	pickle.dump(suratMasuk,f)