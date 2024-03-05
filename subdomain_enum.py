import requests

def request(url):
	try:
		result = requests.get("https://" + url)
		if(result):
			print("[+] Subdomain Discovered -- " + url)
	except:
		pass

def main():
	# target_url = "google.com"
	target_url = input("Enter the Domain Name : ")
	
	# Open SubDomain wordlist
	with open("subdomainwordlist.txt", "r") as wordlist:
		for line in wordlist:
			word = line.strip()
			test_url = word + "." + target_url
			# print(test_url)
			request(test_url)

main()