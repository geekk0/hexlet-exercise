def normalize_url(site):
    prefix = site[:8]
    correct_url = "https:"
    slash = "//"
    if prefix == correct_url + slash:
        print(site)
        return site
    elif "//" in prefix:
         print('Проверьте введенный адрес')
         print(site)
    else:
         site = correct_url + slash + site
         print(site)
         return  correct_url + slash + site
normalize_url('https://testurl.com')

