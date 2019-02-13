import pickle
import re
from convertdate import islamic
import datetime
from openpyxl import Workbook




suratMasuk_list = list()
with open('suratMasuk','rb') as f:
	suratMasuk_list = pickle.load(f)



book = Workbook()
sheet = book.active

num = 1 
sheet['B'+str(num)] = "Nama Pengirim" 
sheet['C'+str(num)] = "Institusi Pengirim" 
sheet['D'+str(num)] = "Alamat Pengirim"
sheet['E'+str(num)] = "Kontak Pengirim"
sheet['F'+str(num)] = "Jabatan Pengirim"
sheet['G'+str(num)] = "Nama Tujuan Surat"  
sheet['H'+str(num)] = "Bidang Tujuan Surat" 
sheet['I'+str(num)] = "Jabatan Tujuan Surat" 
sheet['J'+str(num)] = "Judul Surat"
sheet['K'+str(num)] = "Ringkasan "
sheet['L'+str(num)] = "Nomor Surat"
sheet['M'+str(num)] = "Tanggal Surat"
sheet['N'+str(num)] = "Nomor Agenda"
sheet['O'+str(num)] = "Tanggal Diterima" 
sheet['P'+str(num)] = "Surat Diambil Oleh" 
sheet['Q'+str(num)] = "Keterangan"

num = 2
for surat in suratMasuk_list:
	sheet['B'+str(num)] = surat["dari_orang"] 
	sheet['C'+str(num)] = surat["dari_institusi"] 
	sheet['D'+str(num)] = surat["dari_alamat"] 
	sheet['E'+str(num)] = surat["dari_kontak"]
	sheet['F'+str(num)] = surat["dari_jabatan"] 
	sheet['G'+str(num)] = surat["ke_orang"] 
	sheet['H'+str(num)] = surat["ke_bidang"] 
	sheet['I'+str(num)] = surat["ke_jabatan"] 
	sheet['J'+str(num)] = surat["judul"] 
	sheet['K'+str(num)] = surat["ringkasan"] 
	sheet['L'+str(num)] = surat["nomor_surat"] 
	sheet['M'+str(num)] = surat["tanggal_surat"] 
	sheet['N'+str(num)] = surat["nomor_agenda"] 
	sheet['O'+str(num)] = surat["tanggal_terima"] 
	sheet['P'+str(num)] = surat["surat_diambil_oleh"] 
	sheet['Q'+str(num)] = surat["keterangan"] 
	num += 1

book.save("test.xlsx")


'''
book = Workbook()
sheet = book.active

sheet['A1'] = "Yo!"
book.save("test.xlsx")
'''