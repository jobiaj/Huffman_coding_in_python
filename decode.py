def decode(tree, str):
	output = ''
	p = tree
	for bit in str:
		if bit == 0:
			p = p[0]
		else:
			p = p[1]
		if type(p) == type(''):
			output +=p
			p = tree
	return output
print decode((15, ((6, ((3, 'a'), (3, ((1, 'g'), (2, 'c'))))), (9, ((4, ((2, 'f'), (2, ((1, 'b'), (1, 'd'))))), (5, 'e')))))
            ,"00000010010100101010111111111101101110111000")
