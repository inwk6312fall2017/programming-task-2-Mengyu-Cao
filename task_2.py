with open('Crime.csv', 'r') as myfile
def out_list(myfile):
	Crime_type=[]
	my_dic={}
	for line in myfile:
		line=line.strip()
		line=line.split()
		Crime_type.append((line[8],line[7]))
	
	for item in Crime_type:
		if item in my_dic:
			my_dic[item]+=1
		else:
			my_dic[item]=1
	
	my_output=my_dic.split()
	return my_output
print(out_list(myfile))
