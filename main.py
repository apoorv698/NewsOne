#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import os
import webapp2
import jinja2
import urllib2
import logging
import sys
from xml.dom import minidom

import re
from google.appengine.ext import db

template_dir=os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Intermediat(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class News(object):
    def __init__(self, title, link, imgurl, description):
        self.title=title
        self.link=link
        self.imgurl=imgurl
        self.description=description
	
class MainHandler(Intermediat):
	def get(self):		
		url="https://www.hindustantimes.com/rss/cities/delhi/rssfeed.xml"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			alerts=''
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				description = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				#logging.error(titl)
				#logging.error(data)
				imgurl = it.getElementsByTagName('media:content')[0].getAttribute('url')
				newsitm=News(titl,data,imgurl,description)
				newsItem.append(newsitm)
				#logging.error(News(title,data)))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('index.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)

class National(Intermediat):
	def get(self):		
		url="http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			alerts=''
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				newsitm=News(titl,data,"","")
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('national.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)

class Technology(Intermediat):
	def get(self):		
		url="https://gadgets.ndtv.com/rss/feeds"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			alerts=''
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				imgurl = it.getElementsByTagName('storyimage')[0].childNodes[0].nodeValue
				description = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				newsitm=News(titl,data,imgurl,description)
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('sci.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)
			
class Sports(Intermediat):
	def get(self):		
		url="https://www.hindustantimes.com/rss/sports/rssfeed.xml"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				description = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				#logging.error(titl)
				#logging.error(data)
				imgurl = it.getElementsByTagName('media:content')[0].getAttribute('url')
				newsitm=News(titl,data,imgurl,description)
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('sport.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)
			
class Entertainment(Intermediat):
	def get(self):		
		url="https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			alerts=''
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				imgurl = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				f=0
				i=0
				s=e=0
				for i in range(len(imgurl)):
					if imgurl[i]=='"':
						f+=1
						if f==11:
							s=i
						if f==12:
							e=i
							break
				newsitm=News(titl,data,imgurl[s+1:e],"")
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('national.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)
			
class Business(Intermediat):
	def get(self):		
		url="https://economictimes.indiatimes.com/rssfeedsdefault.cms"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			alerts=''
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				imgurl=""
				try:
					imgurl = it.getElementsByTagName('image')[0].childNodes[0].nodeValue
				except:
					imgurl = ""
				description = " "
				try:
					description = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				except:
					description = ""
				newsitm=News(titl,data,imgurl,description)
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			logging.error("last")
			self.render('business.html',newsItem=newsItem)
			logging.error("final")
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)
			
class Global(Intermediat):
	def get(self):		
		url="https://www.hindustantimes.com/rss/world/rssfeed.xml"
		#logging.error(url)
		try:
			#logging.error(url)
			link=req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			content=urllib2.urlopen(link).read()
			xmlparsed=minidom.parseString(content)
			#logging.error( xmlparsed.toprettyxml())
			upperitems=xmlparsed.getElementsByTagName('channel')[0]
			items=upperitems.getElementsByTagName('item')
			newsItem = []
			#logging.error('fgdg')
			for it in items:
				titl = it.getElementsByTagName('title')[0].childNodes[0].nodeValue
				#logging.error(titl)
				data = it.getElementsByTagName('link')[0].childNodes[0].nodeValue
				#logging.error(data)
				description = it.getElementsByTagName('description')[0].childNodes[0].nodeValue
				#logging.error(titl)
				#logging.error(data)
				imgurl = it.getElementsByTagName('media:content')[0].getAttribute('url')
				newsitm=News(titl,data,imgurl,description)
				newsItem.append(newsitm)
				#logging.error(News(title,data))
			
			#for ni in newsItem:
				#logging.error( ni.title+"    "+ni.link)
			self.render('global.html',newsItem=newsItem)
		except Exception as e:
			logging.error('except case')
			print "Exception occured: "+str(e)

app = webapp2.WSGIApplication([
	('/national.html',National),('/index.html',MainHandler),('/sci.html',Technology),('/sport.html',Sports), ('/entertain.html',Entertainment),('/business.html',Business), ('/global.html', Global)
], debug=True)