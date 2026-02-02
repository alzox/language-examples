"""
IO objects can be created using "with" [i/o object] for networking and filesystem behaviour.
"""

import urllib.request

def file_example():
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')
    
    with open('example.txt', 'r') as file:
        content = file.read()
        print(f"File content: {content}")

def network_example():
    with urllib.request.urlopen('https://httpbin.org/json') as response:
        data = response.read()
        print(f"Status: {response.status}")
        print(f"Data: {data.decode('utf-8')}")

if __name__ == "__main__":
    file_example()
    network_example()