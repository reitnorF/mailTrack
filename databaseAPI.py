import pickle
import web
import re
from convertdate import islamic
import datetime
import json
import base64

#Load database
suratKeluar = list()
with open('suratKeluar','rb') as f:
	suratKeluar = pickle.load(f)

suratMasuk_list = list()
with open ('suratMasuk','rb') as f:
	suratMasuk_list = pickle.load(f)


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
	for x in suratKeluar:
		if x["ID"] == key:
			suratKeluar.remove(x)
			print x

def deleteItemByKeyMasuk(key):
	for x in suratMasuk_list:
		if x["ID"] == key:
			suratMasuk_list.remove(x)
			print x



def endTransaction():
	with open("suratKeluar","wb") as f:
		pickle.dump(suratKeluar,f)

def endTransaction_suratMasuk():
	with open("suratMasuk","wb") as f:
		pickle.dump(suratMasuk_list,f)



def generateNewKodeSurat():
	lastSuratID = getMaxSuratID(suratKeluar) + 1
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
    '/', 'index',
    '/login','login',
    '/suratMasuk', 'suratMasuk',
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
		render = web.template.render('templates')
		kodesurat = generateNewKodeSuratMasuk()
		return render.addin(kodesurat)


class suratMasuk:
	def GET(self):
		render = web.template.render('templates')
		return render.suratmasuk(suratMasuk_list)


class editSuratKeluar:
	def GET(self,id):
		render = web.template.render('templates')
		return render.suratkeluar(suratmasuk)

class index:
	def GET(self):
		if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
			render = web.template.render('templates')
			return render.suratkeluar(suratKeluar)
		else:
			raise web.seeother('/login')

class addmail:
	def GET(self):
		render = web.template.render('templates')
		kodesurat = generateNewKodeSurat()
		return render.add(kodesurat)

class dataGateway:
	def POST(self):
		data = web.data()
		packagedData = json.loads(data)
		print packagedData["tanggal"]
		suratKeluar.append(packagedData)
		with open("suratKeluar","wb") as f:
			pickle.dump(suratKeluar,f)
		return data

class dataGatewayMasuk:
	def POST(self):
		data = web.data()
		packagedData = json.loads(data)
		suratMasuk_list.append(packagedData)
		endTransaction_suratMasuk()
		return data

class requestDelete:
	def POST(self):
		data = web.data()
		print data
		deleteItemByKey(int(data))
		endTransaction()
		return data

class requestDeleteMasuk:
	def POST(self):
		data = web.data()
		print data
		deleteItemByKeyMasuk(int(data))
		endTransaction_suratMasuk()
		return data

#Start Web Server
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()