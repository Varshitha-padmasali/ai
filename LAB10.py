


































def resolve(clause1, clause2):
    resolved = []
    for literal in clause1:
        if literal.startswith('~') and literal[1:] in clause2:
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(literal)
            new_clause.remove(literal[1:])
            resolved.append(new_clause)
        elif ('~' + literal) in clause2:#open bracket
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(literal)
            new_clause.remove('~' + literal)
            resolved.append(new_clause)
    return resolved
def resolution(kb, query):
    neg_query = ['~' + query]
    kb.append(neg_query) #append
    new = [] ####
    while True:
        n = len(kb) #####
        for i in range(n):
            for j in range(i + 1, n):
                resolvents = resolve(kb[i], kb[j]) ####
                for r in resolvents: #####
                    if r == []:
                        return True
                    if r not in kb and r not in new: ####
                        new.append(r)
        if not new: ####
            return False
        kb.extend(new) ###extend
knowledge_base = [
    ['P', 'Q'],
    ['~P', 'R'],
    ['~Q'],
    ['~R']
]
query = 'P'
if resolution(knowledge_base, query):
    print("Query can be proved using Resolution")
else:
    print("Query cannot be proved")