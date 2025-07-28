import requests
def detect_tokens():
    try:
        resp = requests.get("https://pump.fun/api/tokens")
        tokens = resp.json()
        for token in tokens:
            if "trump" in token['name'].lower():
                return token['address']
        return tokens[0]['address'] if tokens else None
    except Exception as e:
        print(f"Error scanning: {e}")
        return None
