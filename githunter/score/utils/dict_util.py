
def getif(key, data: {}, fallback=None):
    return data[key] if key in data else fallback
