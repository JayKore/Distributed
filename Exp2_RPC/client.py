import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

result = proxy.add(5, 10)
resultmultiply = proxy.multiply(5, 10) 
print("Result from server:", result)
print("Multiply Result from server:", resultmultiply)