import sys
precasc = open('prec.txt', 'r')


temp=[]
dict1={} #for precedence
dict2={}
dict3={} #for associativity
prec=0
operator=[]
for row2 in precasc:
	temp=row2.rstrip('\n')
	temp=temp.split(' ')
	
	for i in range (1,len(temp)):
		dict1[temp[i]]=prec;
		operator.append(temp[i])
	for i in range (1,len(temp)):
		dict3[temp[i]]=temp[0];
	prec=prec+1;
dict1['i']=-1
dict1['$']=50
operator.append('i')
operator.append('$')
size=len(operator)
#print(dict1)
#print(operator)
table=[[0 for x in range(size)] for y in range(size)]
for i in range (0,size):
	for j in range (0,size) :
		if(dict1[operator[i]]>dict1[operator[j]]):
			table[i][j]='<'
		elif(dict1[operator[i]]<dict1[operator[j]]):
			table[i][j]='>'
		else:
			if(operator[i]=='i' and operator[j]=='i'):
				table[i][j]='Error'
			elif(operator[i]=='$' and operator[j]=='$'):
				table[i][j]='Accept'
			elif(dict3[operator[i]]=='l'):
				table[i][j]='>'
			else: 
				table[i][j]='<'
#print(operator)
#print(operator)					
#print(table)
###########################################################################
print("Precedence Table-:(i is treated as 'id') \n")

for i in range(0,len(operator)):
	for j in range(0,len(operator)):
		print(operator[i],operator[j],table[i][j])
print('\n')
print('\n')
###########################################################################
grammar = open('grammar.txt', 'r')
flag=0
for row1 in grammar:
	temp=row1.rstrip('\n')
	temp=temp.rstrip('\r')
	temp=temp.split('->')
	#print(temp)
	if(flag==0):
		start=temp[0]
		flag=1
	dict2[temp[1]]=temp[0]	

#####################################################################
input1 = raw_input();
stack=[]
topter=['$']                             #top terminal stack
ptr=0                           #current pointer
stack.append('$')
input1=input1+'$'
action=''	
while(1):
	if(ptr==len(input1)-1):
		action='REDUCE'
		i=-1;
		temp=''
		while(1):
			if(stack[i]==start and len(stack)==2):
				print("Accepted")
				stack.append('$')
				print(stack)
				#print("The given expression does not belong to the grammar")
				sys.exit()
			if(stack[i]=='$' and len(stack)>2):
				print(" Not Accepted  expression does not belong to the grammar")
				#print("The given expression does not belong to the grammar")
				sys.exit()
			
			temp=temp+stack[i];
			#print(temp)
			if temp in dict2.keys():
				for z in range(0,len(temp)):
					stack.pop()
				stack.append(dict2[temp])
				topter.pop()
				print(stack,input1[ptr:len(input1)],action)
				print('\n')
				break
			i-=1;
		
	
	
	
	else:
		if(dict1[input1[ptr]] < dict1[topter[-1]]):
			action='SHIFT'
			stack.append(input1[ptr])
			topter.append(input1[ptr])
			print(stack,input1[ptr+1:len(input1)],action)
			print('\n')
			ptr+=1;
	
		elif(dict1[input1[ptr]] > dict1[topter[-1]]):
			action='REDUCE'
			i=-1;
			temp=''
			while(1):
				if(stack[i]=='$'):
					print( "Not Accepted  given expression does not belong to the grammar")
					#print("The given expression does not belong to the grammar")
					sys.exit()
			
				temp=temp+stack[i];
				#print(temp)
				if temp in dict2.keys():
					for z in range(0,len(temp)):
						stack.pop()
					stack.append(dict2[temp])
					topter.pop()
					print(stack,input1[ptr:len(input1)],action)
					print('\n')
					break
				i-=1;
		else:
			if(dict3[input1[ptr]]=='r'):
				action='SHIFT'
				stack.append(input1[ptr])
				topter.append(input1[ptr])
				print(stack,input1[ptr+1:len(input1)],action)
				print('\n')
				ptr+=1;
	
			elif(dict3[input1[ptr]]=='l'):
				action='REDUCE'
				i=-1;
				temp=''
				while(1):
					if(stack[i]=='$'):
						print( "Not Accepted Not belongs to this Grammer")
						sys.exit()
			
					temp=temp+stack[i];
					if temp in dict2.keys():
						for z in range(0,len(temp)):
							stack.pop()
						stack.append(dict2[temp])
						topter.pop()
						print(stack,input1[ptr:len(input1)],action)
						print('\n')
						break
					i-=1;
	
print("success")
			
				
		



