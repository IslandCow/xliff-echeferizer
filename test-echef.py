import cheferizer as C

strings = {"Abba", "STOP", "FERROURS", "ferris", "Configuration", "ithaka", "ihiibbkkii", "broke", "chicken", "fairy", "boffin", "courier", "Tariri", "bananna", "aurous", "abbAAbBBBaaaa", "BabbaBBAkkkk", "bathe"}

orig = "Original" 
chef = "ECHEFERIZED:"
for s in strings:
	e = C.EChef()
	print orig.ljust(20) + s
	print chef.ljust(20) + e.parse(s)
