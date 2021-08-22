from lxml import etree

file = open(file='result.txt', mode='rb')
text = file.read()
dom = etree.HTML(text)
elements = dom.xpath('//body/div[@id="wp"]/div/div/div')
formhash = ''
if len(elements):
    formhash = elements[0].xpath('string(.)')

print(formhash)
