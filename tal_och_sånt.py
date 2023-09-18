a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric(), a)
print(b.isnumeric(), b)
print(c.isnumeric(), c)
print(d.isnumeric(), d)
print(e.isnumeric(), e)

new_2 = "2"+ b
print(new_2.isdecimal())
print(new_2.isnumeric())
print(new_2.isdigit())