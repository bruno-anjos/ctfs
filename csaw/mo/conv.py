mod_seqs = ['ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC']
binary1 = ""
binary2 = ""

for mode in mod_seqs:
	if mode == "ECB":
		binary1 += "0"
		binary2 += "1"
	else:
		binary1 += "1"
		binary2 += "0"

print(binary1)
print(binary2)