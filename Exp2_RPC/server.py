from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    print(f"Server: Adding {a} + {b}")
    return a + b

def multiply(a, b):
    return a * b

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server running on port 8000...")

server.register_function(add, "add")
server.register_function(multiply, "multiply")
server.serve_forever()