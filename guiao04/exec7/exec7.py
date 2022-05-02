from lxml import etree

def main():
    xml = etree.parse("conf.xml")
    root = xml.getroot()
    print(root.tag)
    for child in root:
        print(child.tag, child.attrib, child.text)
        for grandchild in child:
            print(grandchild.tag, grandchild.attrib, grandchild.text)

main()