#!/usr/bin/env python
import sys
import os
import os.path
import xml.dom.minidom

if os.environ["TRAVIS_SECURE_ENV_VARS"] == "false":
  print "no secure env vars available, skipping deployment"
  sys.exit()
  
distRepoId = ""

print "Branch: " + os.environ["TRAVIS_BRANCH"] + "\n"
print "Branch is master: " + (os.environ["TRAVIS_BRANCH"] == "master")
print "Branch is develop: " + (os.environ["TRAVIS_BRANCH"] == "develop")

if os.environ["TRAVIS_BRANCH"] == "master":
  deployDest = "jebapi-releases"
if os.environ["TRAVIS_BRANCH"] == "develop":
  deployDest = "jebapi-snapshots"

homedir = os.path.expanduser("~")

m2 = xml.dom.minidom.parse(homedir + '/.m2/settings.xml')
settings = m2.getElementsByTagName("settings")[0]

serversNodes = settings.getElementsByTagName("servers")
if not serversNodes:
  serversNode = m2.createElement("servers")
  settings.appendChild(serversNode)
else:
  serversNode = serversNodes[0]

sonatypeServerNode = m2.createElement("server")
sonatypeServerId = m2.createElement("id")
sonatypeServerUser = m2.createElement("username")
sonatypeServerPass = m2.createElement("password")

idNode = m2.createTextNode(distRepoId)
userNode = m2.createTextNode(os.environ["SONATYPE_USERNAME"])
passNode = m2.createTextNode(os.environ["SONATYPE_PASSWORD"])

sonatypeServerId.appendChild(idNode)
sonatypeServerUser.appendChild(userNode)
sonatypeServerPass.appendChild(passNode)

sonatypeServerNode.appendChild(sonatypeServerId)
sonatypeServerNode.appendChild(sonatypeServerUser)
sonatypeServerNode.appendChild(sonatypeServerPass)

serversNode.appendChild(sonatypeServerNode)

m2Str = m2.toxml()
#print m2Str
f = open(homedir + '/.m2/settings.xml', 'w')
f.write(m2Str)
f.close()