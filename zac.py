from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys,time
import webbrowser
webbrowser.open("http://www.explosionsquadcyber.id")
global starttime

g = '\033[0;32m'
gl = '\033[32;1m'
b = '\033[0;36m'
bl = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[1;33m'

class babi():

	def __init__(self):
		self.ngepet()

	def ngepet(self):
		target = input("\033[31;1mT4RG3T \033[37;1m> ")

		site = target
		print("\t\033[32;1mSCANNING ...")
		if not site.startswith("http://"):
			site = "http://"+site
		if not site.endswith("/"):
			site = site+"/"

		try:
			wlist = open("wordlist.txt", "r")
			wordlist = wlist.readlines()
		except fnf as e:
			print("\033[31;1mFILE NOT FOUND LOL!")
			exit()
		finally:
			try:
				wlist.close()
			except:
				print("\033[31;1mWORDLIST CAN'T CLOSE")

		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
		found = []
		resp_codes = {403, 401}
		starttime = time.time()
		for pdl in wordlist:
			try:
				pdl = pdl.replace("\n", "")
				url = site+pdl
				req = Request(url, headers={"User-Agent": user_agent})
				try:
					gotcha = urlopen(req)
					print("\t\033[32;1mDETECTED! \033[31;1m: ","\033[37;1m"+url)
					found.append(url)

				except HTTPError as e:
					if e.code == 404:
						print("\t\033[31;1mNOTFOUND! \033[31;1m: ","\033[37;1m"+url)
					else:
						print("\t\033[37;1mFORBIDDEN!\033[31;1m: ","\033[37;1m"+url)

				except URLError as e:
					sys.exit("\033[31;1mN0 C0NNECTI0N!")
				except Exception as er:
					print("\033[31;1mLAGGING!")
					print("\033[31;1mEXITING!")
					time.sleep(3)
					exit()
			except KeyboardInterrupt as e:
				print("\033[31;1mCTRL+C DETECTED BOS!")
				time.sleep(2)
				exit()

		if found:
			print("\t!DIR FOUND!")
			print("\t \n".join(found))
			print("\t !THANKS!")
		else:
			print("DIR NOT FOUND!")
			print("THANKS")

	def banner():
		yaya = """
\033[32;1m................................................TOOLS... 
\033[32;1m.............................................D1R SCANNER
\033[36;1m.%%%%%%...%%%%....%%%%...........%%%%%....%%%%...%%%%%..
\033[36;1m....%%...%%..%%..%%..%%..........%%..%%..%%..%%..%%..%%.
\033[37;1m...%%....%%%%%%..%%..............%%..%%..%%..%%..%%%%%..
\033[37;1m..%%.....%%..%%..%%..%%..........%%..%%..%%..%%..%%..%%.
\033[36;1m.%%%%%%..%%..%%...%%%%...%%%%%%..%%%%%....%%%%...%%..%%.
\033[36;1m........................................................ 
\t \033[36;1mAuthor  \033[37;1m: Nelo.F4
\t \033[0;36mGithub  \033[37;1m: NeloF4
\t \033[32;1mYoutube \033[37;1m: Nelo.F4
\t \033[0;32mWebsite \033[37;1m: explosionsquadcyber.id
\t \033[1;33mThanks  \033[37;1m: All Member ESC
\t Support : Mynelsss
"""
		return yaya
	print(banner())

if __name__ == '__main__':
	babi()