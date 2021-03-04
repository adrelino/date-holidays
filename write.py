import json

def read_json():
	flat = []
	with open("data/holidays.json") as f:
		data = json.load(f)
		for p in data['holidays']:
			flat.append(p)
			c = data['holidays'][p]
			k = "states"
			if c.get(k):
				for s in c[k]:
					flat.append(p+"-"+s)
	return flat

def write_json(data,filename):
    with open (filename,'w') as outfile:
        json.dump(data,outfile,indent=4,sort_keys=True)

def load_all():
    regions = read_json()
    keys = sorted(regions)
    for k in keys:
        print('%s' % k)
    write_json(regions,"regions-and-subregions.json")


if __name__ == '__main__':
    load_all()