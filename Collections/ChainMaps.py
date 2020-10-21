from collections import ChainMap
dict1={'A':2,'B':2}
dict2={'C':2,'S':2}
dict3={'A':7,'Q':2}

chain=ChainMap(dict1,dict3)
# print(chain)
# print(chain['S'])
# dict2['S']=4
# print(chain['S'])
chain=chain.new_child(dict1)
print(chain['A'])