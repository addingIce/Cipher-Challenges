# coding=UTF-8

from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

class prpcrypt():
	def __init__(self,key):
		self.key = key
		self.mode = AES.MODE_CBC
	def encrypt(self,text):
		cryptor = AES.new(self.key,self.mode,self.key) #创建cryptor对象
		x = len(text)%16
		if x != 0:
			text = text + '0'*(16-x)   					#补0
		self.ciphertext = cryptor.encrypt(text)			#AES自带加密函数
		return b2a_hex(self.ciphertext)
	def decrypt(self,text):
		cryptor = AES.new(self.key,self.mode,self.key)
		plaintext = cryptor.decrypt(a2b_hex(text))		#AES自带解密函数
		return plaintext.rstrip('0')					#去除补位的0

#key = input('Your key:')
plain_text = input('Your plain text:')					#输入待加密的明文，带引号字符串
pc = prpcrypt('''It is my own key''')					#加密秘钥
e = pc.encrypt(plain_text)								#得到的密文
d = pc.decrypt(e)										#解密后的明文
print 'ciphertext: '+e+'\n'+'plaintext: '+d
