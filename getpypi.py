from bs4 import BeautifulSoup
import requests
import subprocess
import time
import pip
from urllib.request import Request
import urllib.request
import os

savePath = ''

remainingPackages = []

package = []
replicaPackage = []

packageadAptiveTechnologies = []
replicaAdaptiveTechnologies = []

packageArtisticSoftware = []
replicaArtisticSoftware = []

packageComunications = []
replicaComunications = []

packageDatabase = []
replicaDatabase = []

packageDesktopEnvironment = []
replicaDesktopEnvironment = []

packageDocumentation = []
replicaDocumentation = []

packageEducation = []
replicaEducation = []

packagegamesAndEnt = []
replicagamesAndEnt = []

packagehomeAutomation = []
replicahomeAutomation = []

packageinternet = []
replicainternet = []

packagemultimedia = []
replicamultimedia = []

packageofficeAndBusiness = []
replicaofficeAndBusiness = []

packageotherNonListedTopic = []
replicaotherNonListedTopic = []

packageprinting = []
replicaprinting = []

packagereligion = []
replicareligion = []

packagesciAndEngineering = []
replicasciAndEngineering = []

packagesecurity = []
replicasecurity = []

packagesociology = []
replicasociology = []

packagesoftwareDev = []
replicasoftwareDev = []

packagesystem = []
replicasystem = []

packageterminals = []
replicaterminals = []

packagetextEditors = []
replicatextEditors = []

packagetextProcessing = []
replicatextProcessing = []

packageutilities = []
replicautilities = []

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

adaptiveTechnologies = 'https://pypi.python.org/pypi?:action=browse&show=all&c=228'
artisticSoftware = 'https://pypi.python.org/pypi?:action=browse&show=all&c=229'
comunications = 'https://pypi.python.org/pypi?:action=browse&show=all&c=230'
database = 'https://pypi.python.org/pypi?:action=browse&show=all&c=256'
desktopEnvironment = 'https://pypi.python.org/pypi?:action=browse&show=all&c=259'
documentation = 'https://pypi.python.org/pypi?:action=browse&show=all&c=302'
education = 'https://pypi.python.org/pypi?:action=browse&show=all&c=303'
gamesAndEnt = 'https://pypi.python.org/pypi?:action=browse&show=all&c=306'
homeAutomation = 'https://pypi.python.org/pypi?:action=browse&show=all&c=318'
internet = 'https://pypi.python.org/pypi?:action=browse&show=all&c=319'
multimedia = 'https://pypi.python.org/pypi?:action=browse&show=all&c=338'
officeAndBusiness = 'https://pypi.python.org/pypi?:action=browse&show=all&c=372'
otherNonListedTopic = 'https://pypi.python.org/pypi?:action=browse&show=all&c=382'
printing = 'https://pypi.python.org/pypi?:action=browse&show=all&c=383'
religion = 'https://pypi.python.org/pypi?:action=browse&show=all&c=384'
sciAndEngineering = 'https://pypi.python.org/pypi?:action=browse&show=all&c=385'
security = 'https://pypi.python.org/pypi?:action=browse&show=all&c=400'
sociology = 'https://pypi.python.org/pypi?:action=browse&show=all&c=402'
softwareDev = 'https://pypi.python.org/pypi?:action=browse&show=all&c=405'
system = 'https://pypi.python.org/pypi?:action=browse&show=all&c=439'
terminals = 'https://pypi.python.org/pypi?:action=browse&show=all&c=479'
textEditors = 'https://pypi.python.org/pypi?:action=browse&show=all&c=483'
textProcessing = 'https://pypi.python.org/pypi?:action=browse&show=all&c=489'
utilities = 'https://pypi.python.org/pypi?:action=browse&show=all&c=501'

def adaptTech():
    rHead  = requests.get(adaptiveTechnologies)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Adaptive Technologies:',y)
                            package.append(y)
                            packageadAptiveTechnologies.append(y)
    print('Found',len(packageadAptiveTechnologies), 'packages in Adaptive Technologies.')
    time.sleep(1)

def artSoft():
    rHead  = requests.get(artisticSoftware)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Art Software:',y)
                            package.append(y)
                            packageArtisticSoftware.append(y)
    print('Found',len(packageArtisticSoftware), 'packages in Art Software.')
    time.sleep(1)

def com():
    rHead  = requests.get(comunications)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Communications:',y)
                            package.append(y)
                            packageComunications.append(y)
    print('Found',len(packageComunications), 'packages in Communications.')
    time.sleep(1)

def dat():
    rHead  = requests.get(database)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Databases:',y)
                            package.append(y)
                            packageDatabase.append(y)
    print('Found',len(packageDatabase), 'packages in Databases.')
    time.sleep(1)

def de():
    rHead  = requests.get(desktopEnvironment)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Desktop Environment:',y)
                            package.append(y)
                            packageDesktopEnvironment.append(y)
    print('Found',len(packageDesktopEnvironment), 'packages in Desktop Environment.')
    time.sleep(1)

def doc():
    rHead  = requests.get(documentation)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Documents:',y)
                            package.append(y)
                            packageDocumentation.append(y)
    print('Found',len(packageDocumentation), 'packages in Documents.')
    time.sleep(1)

def ed():
    rHead  = requests.get(education)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Education:',y)
                            package.append(y)
                            packageEducation.append(y)
    print('Found',len(packageEducation), 'packages in Education.')
    time.sleep(1)

def ge():
    rHead  = requests.get(gamesAndEnt)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Games & Ent.:',y)
                            package.append(y)
                            packagegamesAndEnt.append(y)
    print('Found',len(packagegamesAndEnt), 'packages in Games & Ent.')
    time.sleep(1)

def aut():
    rHead  = requests.get(homeAutomation)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Home Automation:',y)
                            package.append(y)
                            packagehomeAutomation.append(y)
    print('Found',len(packagehomeAutomation), 'packages in Home Automation.')
    time.sleep(1)

def inter():
    rHead  = requests.get(internet)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Internet:',y)
                            package.append(y)
                            packageinternet.append(y)
    print('Found',len(packageinternet), 'packages in Internet.')
    time.sleep(1)

def multi():
    rHead  = requests.get(multimedia)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Multimedia',y)
                            package.append(y)
                            packagemultimedia.append(y)
    print('Found',len(packagemultimedia), 'packages in Multimedia.')
    time.sleep(1)

def offbus():
    rHead  = requests.get(officeAndBusiness)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Office & Bussiness:',y)
                            package.append(y)
                            packageofficeAndBusiness.append(y)
    print('Found',len(packageofficeAndBusiness), 'packages in Office & Bussiness.')
    time.sleep(1)

def nonlisted():
    rHead  = requests.get(otherNonListedTopic)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Other Topics:,',y)
                            package.append(y)
                            packageotherNonListedTopic.append(y)
    print('Found',len(packageotherNonListedTopic), 'packages in Other Topics.')
    time.sleep(1)

def prin():
    rHead  = requests.get(printing)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Printing:',y)
                            package.append(y)
                            packageprinting.append(y)
    print('Found',len(packageprinting), 'packages in Printing.')
    time.sleep(1)

def rel():
    rHead  = requests.get(religion)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Religion:',y)
                            package.append(y)
                            packagereligion.append(y)
    print('Found',len(packagereligion), 'packages in Religion.')
    time.sleep(1)

def scien():
    rHead  = requests.get(sciAndEngineering)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Science & Engineering:',y)
                            package.append(y)
                            packagesciAndEngineering.append(y)
    print('Found',len(packagesciAndEngineering), 'packages in Science & Engineering.')
    time.sleep(1)

def sec():
    rHead  = requests.get(security)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Security:',y)
                            package.append(y)
                            packagesecurity.append(y)
    print('Found',len(packagesecurity), 'packages in Security.')
    time.sleep(1)

def soc():
    rHead  = requests.get(sociology)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Sociology:',y)
                            package.append(y)
                            packagesociology.append(y)
    print('Found',len(packagesociology), 'packages in Sociology.')
    time.sleep(1)

def sof():
    rHead  = requests.get(softwareDev)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Software Dev.:',y)
                            package.append(y)
                            packagesoftwareDev.append(y)
    print('Found',len(packagesoftwareDev), 'packages in Software Dev.')
    time.sleep(1)

def syst():
    rHead  = requests.get(system)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('System:',y)
                            package.append(y)
                            packagesystem.append(y)
    print('Found',len(packagesystem), 'packages in System.')
    time.sleep(1)

def term():
    rHead  = requests.get(terminals)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Terminal',y)
                            package.append(y)
                            packageterminals.append(y)
    print('Found',len(packageterminals), 'packages in Terminal.')
    time.sleep(1)

def txted():
    rHead  = requests.get(textEditors)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Text Editing:',y)
                            package.append(y)
                            packagetextEditors.append(y)
    print('Found',len(packagetextEditors), 'packages in Text Editing.')
    time.sleep(1)

def txtproc():
    rHead  = requests.get(textProcessing)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Text Processing:',y)
                            package.append(y)
                            packagetextProcessing.append(y)
    print('Found',len(packagetextProcessing), 'packages in Text Processing.')
    time.sleep(1)

def util():
    rHead  = requests.get(utilities)
    data = rHead.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        y = (link.get('href'))
        ignoreA = 'pypi?'
        if ignoreA not in y:
            ignoreB = 'http'
            if ignoreB not in y:
                if y.startswith('/pypi'):
                    if y != '/pypi':
                        y = y.replace('pypi/', '')
                        y = y.replace('/', '')
                        if y not in package:
                            print('Utilities:',y)
                            package.append(y)
                            packageutilities.append(y)
    print('Found',len(packageutilities), 'packages in Utilities.')
    time.sleep(1)
    
def findAllPackages():
    adaptTech()
    artSoft()
    com()
    dat()
    de()
    doc()
    ed()
    ge()
    aut()
    inter()
    multi()
    offbus()
    nonlisted()
    prin()
    rel()
    scien()
    sec()
    soc()
    sof()
    syst()
    term()
    txted()
    txtproc()
    util()
    print('')
    print('-------------------------------------------------')
    print('Package Genre           |  No. Of Packages')
    print('-------------------------------------------------')
    print('Adaptive Technologies:    ',len(packageadAptiveTechnologies))
    print('Artistic Software:        ',len(packageArtisticSoftware))
    print('Communications:           ',len(packageComunications))
    print('Database:                 ',len(packageDatabase))
    print('Desktop Environment:      ',len(packageDesktopEnvironment))
    print('Documentation:            ',len(packageDocumentation))
    print('Education:                ',len(packageEducation))
    print('Games & Entertainment:    ',len(packagegamesAndEnt))
    print('Home Automation:          ',len(packagehomeAutomation))
    print('Internet:                 ',len(packageinternet))
    print('Multimedia:               ',len(packagemultimedia))
    print('Office & Bussiness:       ',len(packageofficeAndBusiness))
    print('Unspecified Topics:       ',len(packageotherNonListedTopic))
    print('Printing:                 ',len(packagereligion))
    print('Religion:                 ',len(packagereligion))
    print('Science & Engineering:    ',len(packagesciAndEngineering))
    print('Security:                 ',len(packagesecurity))
    print('Sociology:                ',len(packagesociology))
    print('Software Development:     ',len(packagesoftwareDev))
    print('System:                   ',len(packagesystem))
    print('Terminals:                ',len(packageterminals))
    print('Text Editors:             ',len(packagetextEditors))
    print('Text Processing:          ',len(packagetextProcessing))
    print('Utilities:                ',len(packageutilities))
    print('')
    print('Total Available:          ',len(package))
    print('-------------------------------------------------')
    print('Download these packages? (y//n)')
    choice = input('Enter: ')
    if choice=='y':
        saveFunction()
    if choice=='n':
        menu()
    else:
        print('Invalid Option!')

def saveFunction():
    global savePath
    savePath = input('Save to: ')
    if os.path.exists(savePath):
        print('saving to:', savePath, '\n')
        getAll()
    elif not os.path.exists(savePath):
        print('please specify a valid path...')
        saveFunction()
        
def getAll():
    global savePath
    a= 0
    b=(len(package))
    count= 1
    for packages in package:
        try:
            print('Processing Package '+ str(count) + '/' + str(b) + ' :  ' + package[a])
            url = 'https://pypi.python.org/pypi/' + package[a] + '/'
            rHead  = requests.get(url)
            data = rHead.text
            soup = BeautifulSoup(data)
            for link in soup.find_all('a'):
                y = link.get('href')
                t = link.text
                t = t.strip()
                t = t.replace('Download', '')
                if t.startswith('\n'):
                    t = t[1:]
                    
                if not 'https://' in t:
                    if not 'http://' in t:
                        if y != None:
                            
                            y = y.strip()
                            if y.endswith('.zip'):
                                fullfilename = os.path.join(savePath, t)
                                if not os.path.exists(fullfilename):
                                    print('saving to:', fullfilename)
                                    urllib.request.urlretrieve(y, fullfilename)
                                elif os.path.exists(fullfilename):
                                    print('skipping existing package name:', t)
                                    
                            if 'tar.gz' in y:
                                fullfilename = os.path.join(savePath, t)
                                if not os.path.exists(fullfilename):
                                    print('saving to:', fullfilename)
                                    urllib.request.urlretrieve(y, fullfilename)
                                elif os.path.exists(fullfilename):
                                    print('skipping existing package name:', t)

                                    
                            if '.whl' in y:
                                fullfilename = os.path.join(savePath, t)
                                if not os.path.exists(fullfilename):
                                    print('saving to:', fullfilename)
                                    urllib.request.urlretrieve(y, fullfilename)
                                elif os.path.exists(fullfilename):
                                    print('skipping existing package name:', t)
                                           
            print('')
        except subprocess.CalledProcessError as e:
            pass
        except KeyboardInterrupt:
            break
        except:
            pass
        
        count += 1
        a += 1
    print('Completed.')
    
def menu():
    print('\nGetPyPi!\n')
    print('Menu:')
    print('0. GetPyPi (Download all code from PyPi)')
    choice = input('Enter: ')
    if choice == '0':
        findAllPackages()
    else:
        print('Invalid Option!')
        menu()
    

q=1
while q==1:
    menu()
