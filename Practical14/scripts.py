from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
#Parse the XML file into a DOM document object
DOMTree = xml.dom.minidom.parse('go_obo.xml')
#get the root element of the document
obo = DOMTree.documentElement
#extract 'term' nodes
terms = obo.getElementsByTagName('term')
#make lists to store id/name/defstr/childnodes
id = []
name = []
defstr1 = []
childnodes= []
for term in terms:
    #count the childnodes
    is_a_nodes = term.getElementsByTagName('is_a')
    count = len(is_a_nodes)
    defs = term.getElementsByTagName('def')
    for Def in defs:
        defstrs = Def.getElementsByTagName('defstr')
        for defstr in defstrs:
            # getElementsByTagName can only get element, childNodes[0] convert >
            if 'autophagosome' in defstr.childNodes[0].data:
                defstr_=defstr.childNodes[0].data
                term_id = term.getElementsByTagName('id')[0].childNodes[0].data
                term_name = term.getElementsByTagName('name')[0].childNodes[0].data
                id.append(term_id)
                defstr1.append(defstr_)
                name.append(term_name)
                childnodes.append(count)


#make a dictionary
data = {'id':id, 'name':name,'definition':defstr1,'childnodes':childnodes}
#make the dictionary into dataframe
df=pd.DataFrame(data)
#import the dataframe into excel
df.to_excel('autophagosome.xlsx',index=False)
