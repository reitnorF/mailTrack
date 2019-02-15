import pickle
import re
from convertdate import islamic
import datetime
from openpyxl import Workbook






def exportToExcel():
	def adjustColumnWidth():
		for col in sheet.columns:
			max_length=0
			column = col[0].column
			for cell in col:
				try:
					if len(str(cell.value)) > max_length:
						max_length = len(cell.value)
				except:
					pass
			adjusted_width = (max_length + 2) * 1.2
			sheet.column_dimensions[column].width = adjusted_width
	suratMasuk_list = list()
	with open('suratMasuk','rb') as f:
		suratMasuk_list = pickle.load(f)
	book = Workbook()
	sheet = book.active
	sheet.title = "Surat Masuk"
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

	adjustColumnWidth()
	book.create_sheet("Surat Keluar")
	sheet= book.get_sheet_by_name("Surat Keluar")

	suratKeluar_list = list()
	with open('suratKeluar','rb') as f:
		suratKeluar_list = pickle.load(f)
	num = 1 
	sheet['B'+str(num)] = "Nama Pengirim" 
	sheet['C'+str(num)] = "Institusi Pengirim" 
	sheet['D'+str(num)] = "Jabatan Pengirim"
	sheet['E'+str(num)] = "Nama Tujuan"
	sheet['F'+str(num)] = "Institusi Tujuan"
	sheet['G'+str(num)] = "Jabatan Tujuan"  
	sheet['H'+str(num)] = "Alamat Tujuan" 
	sheet['I'+str(num)] = "Judul Surat" 
	sheet['J'+str(num)] = "Nomor"
	sheet['K'+str(num)] = "Tanggal "
	sheet['L'+str(num)] = "Penandatangan"
	sheet['M'+str(num)] = "Diketahui Direktur Eksekutif?"
	sheet['N'+str(num)] = "Tanggal Diserahkan"
	sheet['O'+str(num)] = "Diambil Oleh" 
	sheet['P'+str(num)] = "Keterangan" 
	num = 2
	for surat in suratKeluar_list:
		sheet['B'+str(num)] = surat["dari_orang"] 
		sheet['C'+str(num)] = surat["dari_institusi"] 
		sheet['D'+str(num)] = surat["dari_jabatan"] 
		sheet['E'+str(num)] = surat["ke_nama"]
		sheet['F'+str(num)] = surat["ke_institusi"] 
		sheet['G'+str(num)] = surat["ke_jabatan"] 
		sheet['H'+str(num)] = surat["ke_alamat"] 
		sheet['I'+str(num)] = surat["judul"] 
		sheet['J'+str(num)] = surat["nomor"] 
		sheet['K'+str(num)] = surat["tanggal"] 
		sheet['L'+str(num)] = surat["penandatangan"] 
		sheet['M'+str(num)] = surat["diketahui_direktur_eksekutif"] 
		sheet['N'+str(num)] = surat["tanggal_diserahkan"] 
		sheet['O'+str(num)] = surat["diambil_oleh"] 
		sheet['P'+str(num)] = surat["keterangan"] 
		num += 1

	adjustColumnWidth()
	book.save("static/suratsalman.xlsx")

exportToExcel()