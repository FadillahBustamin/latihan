class kelilingLingkaran(object):
	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungKeliling(self):
		return  2 * self.phi * self.jarijari
	def cetakData(self):
		print("keliling")
		print("phi\t: ", self.phi)
		print("jarijari\t: ", self.jarijari)
	def cetakKeliling(self):
		print("Keliling\t= ", self.hitungKeliling())

def main ():

	kelilingLingkaran1 = kelilingLingkaran(3.14, 7)

	print("Objek kelilingLingkaran")
	kelilingLingkaran1.cetakData()
	kelilingLingkaran1.cetakKeliling()

if __name__=="__main__":
	main()

class luasLingkaran(object):
	def __init__(self, phi, r):
		self.phi = phi
		self.jarijari = r
	def hitungLuas(self):
		return self.phi * (self.jarijari * self.jarijari)
	def cetakData(self):
		print("luas")
		print("phi\t: ", self.phi)
		print("jarijari\t: ", self.jarijari)
	def cetakLuas(self):
		print("Luas\t= ", self.hitungLuas())


def main ():

	luasLingkaran1 = luasLingkaran(3.14, 14)

	print("Objek luasLingkaran")
	luasLingkaran1.cetakData()
	luasLingkaran1.cetakLuas()

if __name__ == "__main__":
	main()
