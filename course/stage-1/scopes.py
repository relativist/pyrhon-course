variables = []
childScopes = []
mainScope = {'global': [variables, childScopes]}


def append_child_namespace_to_parent(parent, child):
    for key, value in mainScope.items():
        if parent == key:
            value[1].append(child)


def add_var_to_scope(namespace, var):
    for key, value in mainScope.items():
        if namespace == key:
            value[0].append(var)


def get_var(namespace, var):
    for key, value in mainScope.items():
        if namespace == key:
            for val in value[0]:
                if val == var:
                    return namespace

    for key, value in mainScope.items():
        if namespace in value[1]:
            return get_var(key, var)

    return 'None'


def execute_command(operation, namespace, var):
    if operation == 'create':
        variables = []
        childScopes = []
        mainScope[namespace] = [variables, childScopes]
        append_child_namespace_to_parent(var, namespace)

    if operation == 'add':
        add_var_to_scope(namespace, var)

    if operation == 'get':
        print(get_var(namespace, var))


iter = input()

operations = []
for i in range(0, int(iter)):
    cmd, namesp, arg = input().split()
    operations.append([cmd, namesp, arg])

# operations.append(['create', 'foo', 'global'])
# operations.append(['add', 'global', 'a'])
# operations.append(['add', 'foo', 'b'])
# operations.append(['get', 'global', 'a'])
# operations.append(['get', 'foo', 'b'])
# operations.append(['get', 'foo', 'a'])
#
for operation in operations:
    execute_command(*operation)
