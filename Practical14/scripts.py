from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
#Parse the XML file into a DOM document object
DOMTree = xml.dom.minidom.parse('go_obo.xml')

#get the root element of the document
obo = DOMTree.documentElement
#extract 'is_a' nodes
nodes = obo.getElementsByTagName('is_a')
#extract 'term' nodes
terms = obo.getElementsByTagName('term')

#make lists/dictionary to store id/name/defstr/childnodes
id_list = []
name_list = []
defstr_list =[]
childnodes_list=[]
childnodes_count= {}

#count the childnodes, and store them in childnodes_count
for node in nodes:
    parent_id = node.childNodes[0].data
    if parent_id in childnodes_count:
        childnodes_count[parent_id] += 1
    else:
        childnodes_count[parent_id] = 1

for term in terms:
    defstrs = term.getElementsByTagName('defstr')
    for defstr in defstrs:
        # getElementsByTagName can only get element, childNodes[0] convert >
        if 'autophagosome' in defstr.childNodes[0].data:
            # count the childnodes
            defstr_=defstr.childNodes[0].data
            term_id = term.getElementsByTagName('id')[0].childNodes[0].data
            term_name = term.getElementsByTagName('name')[0].childNodes[0].data
            id_list.append(term_id)
            defstr_list.append(defstr_)
            name_list.append(term_name)
            # get the values in the dictionary, if key doesn't exist, value=o
            count= childnodes_count.get(term_id,0)
            childnodes_list.append(count)

#make a dictionary
data = {'id':id, 'name':name_list,'definition':defstr_list,'childnodes':childnodes_list}
#make the dictionary into dataframe
df=pd.DataFrame(data)
#import the dataframe into excel
df.to_excel('autophagosome.xlsx',index=False)
