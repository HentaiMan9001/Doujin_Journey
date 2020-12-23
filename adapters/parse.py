import re

#MainSectionFinder = re.compile(r'(\w+)\{(\S+)\}')
MainSectionFinder = re.compile(r'\w+')
AttributeParser = re.compile('(\w+)\:\((\S+)\)\n')
SubSectionFinder = re.compile(r'')

with open('nhentai.adapter', 'r') as adapter_file:
	text = adapter_file.read()
	adapter_file.close()
	
	stuff = MainSectionFinder.findall(text)
	stuff2 = AttributeParser.findall(text)
	
