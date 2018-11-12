import importlib
path = 'src/handler.foo'

parts = path.split('.')

handler = importlib.import_module(parts[0].replace('/', '.'))
fn = getattr(handler, parts[1])

value = fn()
print(value)