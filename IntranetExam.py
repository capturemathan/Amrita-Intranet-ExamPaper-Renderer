import os
import webbrowser
import time
import random
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from time import sleep

cont = 1

print("Welcome to Qp Bank !")
sleep(1)
print("Crafted with love by Mathan.S")
sleep(1)
print("Ensure your connectivity to Amrita Wifi for smooth experience :)")

# Captcha Disabled
"""a=["M234x","Ad34T","Fr45C","J234r","PKa67"]
z=random.randint(0,4)
print(a[z])
captcha=input("Enter the captcha")
while(captcha!=a[z]):
	print("Enter the correct captcha..")
	a=["M234x","Ad34T","Fr45C","J234r","PKa67"]
	z=random.randint(0,4)
	print(a[z])
	captcha=input("Enter the captcha")"""

while(cont==1):
		
	url="http://dspace.amritanet.edu:8080/xmlui/handle/123456789/150"
	page=requests.get(url)
	soup=BeautifulSoup(page.content,'html.parser')
	div=soup.div
	main_div=soup.find(id="aspect_artifactbrowser_CommunityViewer_div_community-view")
	t=PrettyTable(["S.No","Attribute"])
	main_list_item=main_div.ul
	items=main_list_item.findAll("li")
	for i in range(len(items)):
		t.add_row([i+1,items[i].a.text.strip()])
	print(t)
	ch=int(input("Enter your Semester "))
	while((ch>len(items)) or (ch<0)):
		ch=int(input("Enter your Semester "))
	url="http://dspace.amritanet.edu:8080"
	url+=items[ch-1].a["href"]

	print("Give me just a minute...")

	sec_page=requests.get(url)
	sec_soup=BeautifulSoup(sec_page.content,'html.parser')
	u=sec_soup.findAll("ul")


	if ch<=6:
		sec_li=u[3].findAll("li")
	else:
		sec_li=u[2].findAll("li")


	p=PrettyTable(["S.No","Title"])
	for j in range(len(sec_li)):
		p.add_row([j+1,sec_li[j].a.text.strip()])
	print(p)


	ch3=int(input("Enter your choice "))
	while((ch3>len(sec_li)) or (ch3<0)):
		ch3=int(input("Enter your choice "))
	url="http://dspace.amritanet.edu:8080/"
	url+=sec_li[ch3-1].a["href"]
	third_page=requests.get(url)
	third_soup=BeautifulSoup(third_page.content,'html.parser')
	u3_div=third_soup.findAll("div",class_="ds-static-div secondary recent-submission")
	third_div=u3_div[0].a.text.strip()
	third_li=u3_div[0].findAll("li")

	m=PrettyTable(["S.No","Title"])
	m.add_row([1,third_div])
	print(m)

	ch4=int(input("Enter your choice "))
	while((ch4>len(third_li)) or (ch4<0)):
		ch4=int(input("Enter your choice "))
	url="http://dspace.amritanet.edu:8080/"
	url+=third_li[ch4-1].a["href"]
	fourth_page=requests.get(url)
	fourth_soup=BeautifulSoup(fourth_page.content,'html.parser')
	u4_div=fourth_soup.findAll("div",class_="file-metadata")


	v=PrettyTable(["S.No","Subjects"])
	u4_temp=[]
	mod_u4_temp=[]
	for i in range(len(u4_div)):
		u4_temp.append((u4_div[i].findAll("span")[1].text))
	for j in range(len(u4_temp)):
		mod_u4_temp=u4_temp[j].split(",")
		v.add_row([j+1,mod_u4_temp[0]])

	print(v)

	last_ch=int(input("Enter your choice "))
	last_div=fourth_soup.findAll("div",class_="file-link")
	while((last_ch>len(last_div)) or (last_ch<0)):
		last_ch=int(input("Enter your choice "))
	url_last="http://dspace.amritanet.edu:8080"
	url_last+=last_div[last_ch-1].a["href"]

	print("All the very best for your exams :)")
	sleep(1)
	download=int(input("Enter 1 to download or 0 to open in browser "))
	while(download!=1 and download!=0):
		download=int(input("Enter 1 to download or 0 to open in browser "))
	print("Give me just a minute :)")
	if(download==1):
		response = requests.get(url_last)
		save=url_last[71:79]
		save+=".pdf"
		with open(save,'wb') as f:
			f.write(response.content)
		print("The Qp is waiting for you at "+os.getcwd())
	else:
		print("The Qp is waiting for you :)")
		webbrowser.open_new(url_last)
	cont=int(input("Enter 1 to view another Qp or 0 to exit "))
