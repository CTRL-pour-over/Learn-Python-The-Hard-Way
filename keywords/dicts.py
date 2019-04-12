# dicts: stores a key=value mapping of things #
thisdict =	{
  "brand": "Volkswagen",
  "model": "Jetta",
  "year": 2012
}
print thisdict

x = thisdict["model"]
x = thisdict.get("model")

thisdict =	{
  "brand": "Volkswagen",
  "model": "Jetta",
  "year": 2012
}
thisdict["year"] = 2019

for x in thisdict:
    print x

for x in thisdict:
    print thisdict[x]
