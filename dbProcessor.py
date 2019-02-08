import pickle
import re
from convertdate import islamic
import datetime



suratKeluar_list = list()
with open('suratKeluar','rb') as f:
	suratKeluar_list = pickle.load(f)



for i in suratKeluar_list:
	noagenda = i["nomor"]
	print noagenda
	a = re.search("\.([0-9]+).*YPM - (\w{4}) /",noagenda)
	code = -1
	g2 = "-"
	if a is not None:
		print a.group(1) +"---" + a.group(2)
		code = int(a.group(1))
		g2 = a.group(2)
	if code == 1:
		i["kategori"] = "Surat Keputusan"
	elif code == 2:
		i["kategori"] ="Surat Pengumuman"
	elif code == 3:
		i["kategori"] = "Surat Edaran"
	elif code == 4:
		i["kategori"] = "Surat Keterangan"
	elif code == 5:
		i["kategori"] = "Surat Rekomendasi"
	elif code == 6:
		i["kategori"] = "Surat Permohonan"
	elif code == 7:
		i["kategori"] = "Surat Undangan"
	elif code == 8:
		i["kategori"] = "Surat Kuasa"
	elif code == 9:
		i["kategori"] = "Surat Perjanjian"
	elif code == 10:
		i["kategori"] = "Surat Pengantar"
	elif code == 11:
		i["kategori"] = "Surat Tugas"
	elif code == 12:
		i["kategori"] = "Surat Ucapan"
	elif code == 13:
		i["kategori"] = "Surat Peringatan"
	elif code == 14:
		i["kategori"] = "Surat Ijin"
	elif code == 15:
		i["kategori"] = "Surat Pengusulan"
	elif code == 16:
		i["kategori"] = "Surat Balasan"
	elif code == 17:
		i["kategori"] = "Surat Pembatalan"
	else:
		i["kategori"] = ""
		



'''	
	code = int(code)
	if code == 1:
		i["kategori"] = "Surat Keputusan"
	elif code == 2:
		i["kategori"] ="Pengumuman"
	elif code == 3:
		i["kategori"] = "Surat Edaran"
	elif code == 4:
		i["kategori"] = "Surat Keterangan"
	elif code == 5:
		i["kategori"] = "Rekomendasi"
	elif code == 6:
		i["kategori"] = "Permohonan"
	elif code == 7:
		i["kategori"] = "Undangan"
	elif code == 8:
		i["kategori"] = "Surat Kuasa"
	elif code == 9:
		i["kategori"] = "Perjanjian"
	elif code == 10:
		i["kategori"] = "Surat Pengantar"
	elif code == 11:
		i["kategori"] = "Surat Tugas"
	elif code == 12:
		i["kategori"] = "Ucapan"
	elif code == 13:
		i["kategori"] = "Surat Peringatan"
	elif code == 14:
		i["kategori"] = "Ijin"
	elif code == 15:
		i["kategori"] = "Pengusulan"
	elif code == 16:
		i["kategori"] = "Balasan"
	elif code == 17:
		i["kategori"] = "Pembatalan"



for i in suratMasuk_list:
	print i["kategori"]
'''