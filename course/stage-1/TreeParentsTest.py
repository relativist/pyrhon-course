main_map = {}
main_map['A']=['B','C']
main_map['B']=['D']
main_map['C']=['D']
main_map['D']=[]

def search_all_predoks(potomok):
    result = [potomok]
    for key, value in main_map.items():
        if potomok in value:
            result.append(key)
            result.extend(search_all_predoks(key))
    return result

print(set(search_all_predoks('D')))