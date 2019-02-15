#!/usr/bin/python
import pickle
import web
import re
from convertdate import islamic
import datetime
import json
import base64
from openpyxl import Workbook



#Load database
suratKeluar_list = list()
with open('suratKeluar','rb') as f:
	suratKeluar_list = pickle.load(f)

suratMasuk_list = list()
with open ('suratMasuk','rb') as f:
	suratMasuk_list = pickle.load(f)



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


def calculateCategory():
	for i in suratMasuk_list:
		noagenda = i["nomor_agenda"]
		a = re.search("\.([0-9]+)",noagenda)
		code = a.group(1)
		code = int(code)
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





def getMaxSuratID(listOfSurat):
	max = -1
	for x in listOfSurat:
		nomorSurat = x["nomor"]
		match = re.match("(\A[0-9]+)",nomorSurat)
		suratID = int(match.group(1))
		if suratID > max:
			max = suratID
	return max


def getMaxSuratMasukID(listOfSurat):
	max = -1
	for x in listOfSurat:
		nomorSurat = x["nomor_agenda"]
		match = re.match("(\A[0-9]+)",nomorSurat)
		suratID = int(match.group(1))
		if suratID > max:
			max = suratID
	return max

def int_to_roman(input):
	if not isinstance(input, type(1)):
	    raise TypeError, "expected integer, got %s" % type(input)
	if not 0 < input < 4000:
	    raise ValueError, "Argument must be between 1 and 3999"
	ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
	nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
	result = []
	for i in range(len(ints)):
	    count = int(input / ints[i])
	    result.append(nums[i] * count)
	    input -= ints[i] * count
	return ''.join(result)


def deleteItemByKey(key):
	for x in suratKeluar_list:
		if x["ID"] == key:
			suratKeluar_list.remove(x)
			print x

def deleteItemByKeyMasuk(key):
	for x in suratMasuk_list:
		if x["ID"] == key:
			suratMasuk_list.remove(x)
			print x



def endTransaction():
	with open("suratKeluar","wb") as f:
		pickle.dump(suratKeluar_list,f)

def endTransaction_suratMasuk():
	with open("suratMasuk","wb") as f:
		pickle.dump(suratMasuk_list,f)



def generateNewKodeSurat():
	lastSuratID = getMaxSuratID(suratKeluar_list) + 1
	now = datetime.datetime.now()
	year = now.strftime("%Y")
	month  = now.strftime("%m")
	day = now.strftime("%d")
	islam_year = islamic.from_gregorian(int(year),int(month),int(day))[0]
	islam_month = islamic.from_gregorian(int(year),int(month),int(day))[1]
	kodesurat = dict()
	kodesurat["ID"] = lastSuratID
	kodesurat["year"] = islam_year
	kodesurat["month"] = str(int_to_roman(islam_month))
	return kodesurat


def generateNewKodeSuratMasuk():
	lastSuratID = getMaxSuratMasukID(suratMasuk_list) + 1
	return lastSuratID






#Web Server URL Routing Configuration
urls = (
    '/', 'suratMasuk',
    '/login','login',
    '/suratMasuk', 'suratMasuk',
    '/suratKeluar', 'suratKeluar',
    '/addmail', 'addmail',
    '/addmailin', 'addmailin',
    '/dataGateway', 'dataGateway',
    '/dataGatewayMasuk', 'dataGatewayMasuk',
    '/requestDelete', 'requestDelete',
    '/requestDeleteMasuk', 'requestDeleteMasuk',
    '/download' , 'download',
    '/editSuratKeluar/(.+)', 'editSuratKeluar'
)

allowed = (
		('admin','adminsalman'),
		('x','y')
)


def loginCheck():
	if web.ctx.env.get('HTTP_AUTHORIZATION') is None:
		raise web.seeother('/login')



class login:
	def GET(self):
		auth = web.ctx.env.get('HTTP_AUTHORIZATION')
		authreq = False
		if auth is None:
			authreq = True
		else:
			auth = re.sub('^Basic','',auth)
			username,password = base64.decodestring(auth).split(':')
			if (username,password) in allowed:
				raise web.seeother('/suratMasuk')
			else:
				authreq = True
		if authreq:
			web.header('WWW-Authenticate','Basic realm="Auth example"')
			web.ctx.status = '401 Unauthorized'
			return

class download:
	def GET(self):
		loginCheck()
		exportToExcel()
		raise web.seeother('/static/suratsalman.xlsx')


class addmailin:
	def GET(self):
		loginCheck()
		render = web.template.render('templates')
		kodesurat = generateNewKodeSuratMasuk()
		return render.addin(kodesurat)


class suratMasuk:
	def GET(self):
		loginCheck()
		render = web.template.render('templates')
		calculateCategory()
		return render.suratmasuk(suratMasuk_list)

class suratKeluar:
	def GET(self):
		loginCheck()
		render = web.template.render('templates')
		return render.suratkeluar(suratKeluar_list)


class editSuratKeluar:
	def GET(self,id):
		loginCheck()
		render = web.template.render('templates')
		return render.suratkeluar(suratmasuk)

class index:
	def GET(self):
		loginCheck()
		render = web.template.render('templates')
		return render.suratkeluar(suratKeluar_list)

class addmail:
	def GET(self):
		loginCheck()
		render = web.template.render('templates')
		kodesurat = generateNewKodeSurat()
		return render.add(kodesurat)

class dataGateway:
	def POST(self):
		loginCheck()
		data = web.data()
		packagedData = json.loads(data)
		print packagedData["tanggal"]
		suratKeluar_list.append(packagedData)
		with open("suratKeluar","wb") as f:
			pickle.dump(suratKeluar_list,f)
		return data

class dataGatewayMasuk:
	def POST(self):
		loginCheck()
		data = web.data()
		packagedData = json.loads(data)
		suratMasuk_list.append(packagedData)
		endTransaction_suratMasuk()
		return data

class requestDelete:
	def POST(self):
		loginCheck()
		data = web.data()
		print data
		deleteItemByKey(int(data))
		endTransaction()
		return data

class requestDeleteMasuk:
	def POST(self):
		loginCheck()
		data = web.data()
		print data
		deleteItemByKeyMasuk(int(data))
		endTransaction_suratMasuk()
		return data

#Start Web Server
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
