website_dict = {
    "first site": {
        "email": "email@gmail.com",
        "password": "G6y8h9%eF7lvp*a"
    },
    "second site": {
        "email": "num2@email.com",
        "password": "GV3kz1(hkh3X$"
    },
    "third site": {
        "email": "3@3.com",
        "password": "a04PQi3dv+pc%*"
    },
    "amazon": {
        "email": "email@gmail.com",
        "password": "u%4whc1Gmi(Q8+d4n"
    }
}

print(type(website_dict))
print(website_dict)

# print sites
print("*** websites ***")
for sites in website_dict.keys():
    print(sites)

# print email
print("*** email ***")
email = website_dict["amazon"]["email"]
print(type(email))
print(email)

# print password
print("*** password ***")
pass1 = website_dict["amazon"]["password"]
print(type(pass1))
print(pass1)

# access all items via for loop
print("\nitems = ", website_dict.items())
for site, info_dict in website_dict.items():
    print("\nsite ", type(site), " = ", site)
    print("  info ", type(info_dict), " = ", info_dict)
    
    for info_key in info_dict:
        print('  ' + info_key + ':', info_dict[info_key])

# search if site exists
site = 'amazon'
print('***** searching for site *****')
if site in website_dict.keys():
    print(site, " found")
else:
    print(site, " not found!!")
