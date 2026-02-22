import requests

url = "http://127.0.0.1:8000/cafe-menu-pdf/"
try:
    response = requests.get(url, stream=True)
    print(f"Status: {response.status_code}")
    print("Headers:")
    for k, v in response.headers.items():
        print(f"  {k}: {v}")
    
    # Read first 100 bytes
    content = next(response.iter_content(chunk_size=100))
    print(f"First 16 bytes: {content[:16].hex(' ')}")
except Exception as e:
    print(f"Error: {e}")
