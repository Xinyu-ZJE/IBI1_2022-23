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
childnodes_list = []
parent_dict = {}

for term in terms:
# structure a dictionary, the keys are the id of parentnodes, and values are lists to store chilnodes

    ids = term.getElementsByTagName('id')
    for id in ids:
        node_id = id.childNodes[0].data
# find the parent node
    for child in term.getElementsByTagName('is_a'):
        parent_id = child.childNodes[0].data
# for every new parent_id, create a key
        if parent_id not in parent_dict:
            parent_dict[parent_id] = []
# put the childnodes into corresponding values
        parent_dict[parent_id].append(node_id)

    defstrs = term.getElementsByTagName('defstr')
    for defstr in defstrs:
        # getElementsByTagName can only get element, childNodes[0].data convert it into text
        if 'autophagosome' in defstr.childNodes[0].data:
            defstr_=defstr.childNodes[0].data
            term_id = term.getElementsByTagName('id')[0].childNodes[0].data
            term_name = term.getElementsByTagName('name')[0].childNodes[0].data
            # form lists for id/defstr/name
            id_list.append(term_id)
            defstr_list.append(defstr_)
            name_list.append(term_name)

# Construct recursive functions to count nodes
def count_child_nodes(node_id, parent_dict):
    count = 0
    if node_id in parent_dict:
        count += len(parent_dict[node_id])
        for child_id in parent_dict[node_id]:
            count += count_child_nodes(child_id, parent_dict)
    return count

# use count_child_nodes functions to count nodes in the order of id_list
for nodeid in id_list:
    if nodeid in parent_dict:
        childnodes_list.append(count_child_nodes(nodeid,parent_dict))
    else:
        childnodes_list.append(0)

#make a dictionary
data = {'id':id_list, 'name':name_list,'definition':defstr_list,'childnodes':childnodes_list}
#make the dictionary into dataframe
df=pd.DataFrame(data)
#import the dataframe into excel
df.to_excel('autophagosome.xlsx',index=False)
