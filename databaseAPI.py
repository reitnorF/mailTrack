import pickle
import web
import re
from convertdate import islamic
import datetime
import json
import base64

#Load database
suratKeluar_list = list()
with open('suratKeluar','rb') as f:
	suratKeluar_list = pickle.load(f)

suratMasuk_list = list()
with open ('suratMasuk','rb') as f:
	suratMasuk_list = pickle.load(f)

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