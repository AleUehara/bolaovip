#!/usr/bin/python
# -*- encoding: utf-8 -*-
import mechanize
import cookielib

br        = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


br.open("http://www.bolaovip.com.br")
#mech.open("http://google.com")

br.select_form(nr=0)
br["ctl00$ctl00$TopoBolao$txtLogin"] = ""
br["ctl00$ctl00$TopoBolao$txtSenha"] = ""
br.submit()
print "Login efetuado com sucesso"

download_url = "http://www.bolaovip.com.br/BolaoMeuPalpite.aspx?bid=61830&uid=321290"

#print br.open("http://www.bolaovip.com.br/BolaoMeuPalpite.aspx?bid=61830")
#br.retrieve(download_url,"teste.html")[0]

br.open(download_url)

#form = ''
#for f in br.forms():
#    #print f
##    print "-----"
#    print f
#    form = f

br.select_form(nr=0)

br['ctl00$cphCentro$txbJogo154960'] = "1"
br['ctl00$cphCentro$txbJogo254960'] = "3"
#br['__EVENTTARGET'] = 'ctl00$cphCentro$lkbSalvarInferir'

br.submit()


#br.back()
#print br.response().read()
print br.geturl()

for index, cookie in enumerate(cj):
    print index, ' : ', cookie

#print br['ctl00$cphCentro$txbJogo254577']
#print br['__EVENTTARGET']
#print br['__EVENTVALIDATION']

print 'end'