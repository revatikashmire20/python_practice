#add sublist [7,8] after 6
#input
#l2 = [1,2,[3,4,5,6],9]
#output
#[1,2,[3,4,5,6,[7,8]],9]

x = [1,2,[3,4,5,6],9]
x[2].append([7,8])
print(x)
