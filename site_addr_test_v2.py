def normalize_url(site):
    if "https://" in site:
        return site
    else :
        return "https://" + site
print(normalize_url('htps://testurl.com'))