import sympy

def solve_1_unray(equation,one_unray):
    eq=equation.split(r'=')
    if eq[1]!=r'0':
        if eq[1][0]==r'-':
            eq[0]+=r'+'+eq[1][1:]
            eq[1]='0'
        elif eq[1][0] in ['0','1','2','3','4','5','6','7','8','9','x','y','z']:
            eq[0]+=r'-'+eq[1]
            eq[1]='0'
        else:
            pass
    else:
        pass
    if r'^' in eq[0]:
        eq[0].replace(r'^',r'**')
        #print(eq[0])#--调试用，如未出现报错情况请将此行保持注释状态
    if one_unray:
        x=sympy.Symbol('x')
        print('一般式：',eq[0]+r'='+eq[1])
        solution=sympy.solve(eq[0],x)
        print('方程的解为：',solution)
    else:
        #print(eq[0])#--调试用，如未出现报错情况请将此行保持注释状态
        return eq[0]
def solve_n_unray(equation):
    eq_group=equation.split(r',')
    eq_group_n=[]
    unray_group=[]
    x_undef=True
    y_undef=True
    z_undef=True
    for i in eq_group:
        eq=solve_1_unray(i,False)
        eq_group_n.append(eq)
        if 'x' in eq and x_undef:
            x=sympy.Symbol('x')
            unray_group.append(x)
            x_undef=False
        if 'y' in eq and y_undef:
            y=sympy.Symbol('y')
            unray_group.append(y)
            y_undef=False
        if 'z' in eq and z_undef:
            z=sympy.Symbol('z')
            unray_group.append(z)
            z_undef=False
    #print(eq_group_n)#--调试用，如未出现报错情况请将此行保持注释状态
    #print(unray_group)#--调试用，如未出现报错情况请将此行保持注释状态
    solution=sympy.solve(eq_group_n,unray_group)
    print('方程的解为：',solution)

while True:
    equation=input('输入要计算的方程（如有多个方程请用逗号隔开，未知数只支持小写的xyz，等号右边只能有一项，未知数前的系数与未知数之间需加乘号“*”,输入为空即退出程序）：')
    if equation=='':
        break
    else:
        if r',' in equation:
            solve_n_unray(equation)
        else:
            solve_1_unray(equation,True)
