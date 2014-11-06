import urllib2
import xml.etree.ElementTree as ET
from datetime import date

today = date.today().strftime('%d/%m/%y')
today = today[:-2] + '20' + today[-2:]
print today, '\n'

url = "http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=" + today
source = urllib2.urlopen(url).read()
f = open('test.xml', 'w')
f.write(source)
f.close()

tree = ET.parse('test.xml')
root = tree.getroot()
for valute in root.findall('Valute'):
    nominal = valute.findall('Nominal')[0].text
    char_code = valute.findall('CharCode')[0].text
    value = valute.findall('Value')[0].text
    print '%s %s = %s RUB' % (nominal, char_code, value)
