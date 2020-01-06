#Pavan A
#Rohan Kumar
#Pratheek SB
kf=1
while(kf==1):
    finali=(input("enter the path of C++ input file:"))
    finalo=input(("enter the path of output file:"))
    if "txt" in finalo:
        finalo=finalo.replace("txt","py")    

        

    import random

    intvar=dict()
    strvar=dict()
    floatvar=dict()
    func_name=list()
    class_list=list()
    local=list()
    #func_var=
    s=''
    fo=open(finalo,"w")

    f=open(finali,'r')
    def fileinput():
        i=f.readline()
        while(i):
            global s
            s=s+i
            i=f.readline()
        
        
    def whileheader(i,indent=0):
       x=i.index('(');y=i.index(')')
       t='';
       for j in range(len(i)):
           if (j>=x and j<=y):
               t=t+i[j]
       t=t.strip('(' );t=t.strip(')')
       if('&&' in t):
           t=t.replace('&&','and')
       if('||' in t):
           t=t.replace('||','or')
       print('\t'*indent,end='',file=fo)
       print("while",'(',t,'):',sep='',file=fo)

    def whileheader1(i,indent=0):
       i=i.strip(';')
       i=i.strip()
       i=i.strip('for')
       i=i.strip('(')
       i=i.strip()
       i=i.strip(')')
       if('&&' in i):
           i=i.replace('&&','and')
       if('||' in i):
           i=i.replace('||','or')
       print('\t'*indent,end='',file=fo)    
       k=i.split(';')[1]
       print('while','(',k,'):',file=fo)
       
    def funcdecider(i):
        if(('int' in i or 'float' in i or 'double' in i or 'char' in i or 'void' in i) and 'main' not in i and '(' in i and ')' in i and ';' in i  and '=' not in i and 'return' not in i and 'cout' not in i):
            func_name.append((i[i.index(' '):(i.index('('))]).strip(' '))
            return 1
        else: return 0

    def funcprinter(j,i,indent=0):
        global countc
        if countc!=0:
            print('\t'*indent,end='',file=fo)
            k=i.replace(j,'');k=k.replace('int','');k=k.replace('double','');k=k.replace('char','');k=k.replace('float','');k=k.replace(' ','');k=k.replace('void','')
            j=j.replace('int','');j=j.replace('double','');j=j.replace('char','');j=j.replace('float','');j=j.replace(' ','');j=j.replace('void','')
            print("def ",j,'(self,',k[k.index('(')+1:],':',sep='',file=fo)
            k=k.replace('(','');k=k.replace(')','');x=k.split(',');local.extend(x)
        else:
           print('\t'*indent,end='',file=fo)
           k=i.replace(j,'');k=k.replace('int','');k=k.replace('double','');k=k.replace('char','');k=k.replace('float','');k=k.replace(' ','');k=k.replace('void','')
           print("def ",j,k,':',sep='',file=fo)
           k=k.replace('(','');k=k.replace(')','');x=k.split(',');local.extend(x)
        
    def random2(i):  
        i=i.strip(';')
        i=i.strip(' ')
        c=0
        j=i.split('%')[1]
        k=j.split('+')
        for l in k:
                if c==0:
                    x=int(l)
                    c+=1
                elif c==1:
                    y=int(l)
                    break
        max1=x+y-1;min1=y+1
        print("random.randint(",min1,",",max1,")",sep="",file=fo)


    def display(ch,j,indent=0):      
        if j==1:
            for i in intvar.keys():
                if i==ch:
                    print('\t'*indent,end='',file=fo)
                    print(ch,'=',intvar[ch],file=fo)
        if j==2:
            for i in strvar.keys():
                if i==ch:
                    print('\t'*indent,end='',file=fo)
                    print(ch,'=',strvar[ch],file=fo)
        if j==3:
            for i in floatvar.keys():
                if i==ch:
                    print('\t'*indent,end='',file=fo)
                    print(ch,'=',floatvar[ch],file=fo)

    def createvariablecheck(i):
        for j in func_name:
            if j in i: return 0
        else: return 1
        
        
    def createvaribles(i,indent=0): 
        if ('int ' in i and createvariablecheck(i) and ',' not in i ) :
            i=i.strip(' ')
            i=i.strip(';')
            if '=' in i:
                    ch=i[i.index('int ')+len('int '):i.index('=')].strip(' ')
                    intvar.setdefault(ch)
                    value=((i.split('=')[1]).strip(' ' and ';'))
                    intvar[ch]=value
            else:
                    ch=i.split(' ')[1].strip(' ')
                    intvar.setdefault(ch)
                    intvar[ch]=0
            display(ch,1,indent)
        if ('char ' in i and createvariablecheck(i) and ',' not in i):
            i=i.strip(' ')
            i=i.strip(';')        
            if '=' in i:
                    ch=i[i.index('char ')+len('char '):i.index('=')].strip(' ')
                    strvar.setdefault(ch)
                    strvar[ch]=(i.split('=')[1]).strip(' ' and ';')
            else:
                    ch=i.split(' ')[1].strip(' ')
                    strvar.setdefault(ch)
                    strvar[ch]='\'\''
            display(ch,2,indent)
        if ('float ' in i and createvariablecheck(i) and ',' not in i):
            i=i.strip(' ')
            i=i.strip(';')
            if '=' in i:
                    ch=i[i.index('float ')+len('float '):i.index('=')].strip(' ')
                    floatvar.setdefault(ch);
                    value=((i.split('=')[1]).strip(' ' and ';'))
                    floatvar[ch]=value
            else:
                    ch=i.split(' ')[1].strip(' ')
                    floatvar.setdefault(ch);
                    floatvar[ch]=0.0
            display(ch,3,indent)
        if ('double ' in i and createvariablecheck(i) and ',' not in i):
            i=i.strip(' ')
            i=i.strip(';')
            if '=' in i:
                    ch=i[i.index('double ')+len('double '):i.index('=')].strip(' ')
                    floatvar.setdefault(ch);
                    value=((i.split('=')[1]).strip(' ' and ';'))
                    floatvar[ch]=value
            else:
                    ch=i.split(' ')[1].strip(' ')
                    floatvar.setdefault(ch);
                    floatvar[ch]=0.0
            display(ch,3,indent)
            
    def createvariables1(i,indent=0):
        if ('int ' in i and createvariablecheck(i) and ',' in i ) :
            val=i[(i.index('=')+1):(i.index(';'))]
            i=i.strip(' ')
            i=i.strip(';');i=i.replace('int ','');ind=i.index('=')
            k=i[:ind].split(',')
            for j in k:
                j=j.strip()
                intvar.setdefault(j)
                intvar[j]=val
                display(j,1,indent)
        if ('double ' in i and createvariablecheck(i) and ',' in i ) :
            val=i[(i.index('=')+1):(i.index(';'))]
            i=i.strip(' ')
            i=i.strip(';');i=i.replace('double ','');ind=i.index('=')
            k=i[:ind].split(',')
            for j in k:
                j=j.strip()
                floatvar.setdefault(j)
                floatvar[j]=val
                display(j,3,indent)
        if ('char ' in i and createvariablecheck(i) and ',' in i ) :
            val=i[(i.index('=')+1):(i.index(';'))]
            i=i.strip(' ')
            i=i.strip(';');i=i.replace('char ','');ind=i.index('=')
            k=i[:ind].split(',')
            for j in k:
                j=j.strip()
                strvar.setdefault(j)
                strvar[j]=val
                display(j,2,indent)
        if ('float ' in i and createvariablecheck(i) and ',' in i ) :
            val=i[(i.index('=')+1):(i.index(';'))]
            i=i.strip(' ')
            i=i.strip(';');i=i.replace('float ','');ind=i.index('=')
            k=i[:ind].split(',')
            for j in k:
                j=j.strip()
                floatvar.setdefault(j)
                floatvar[j]=val
                display(j,3,indent)

    def decl(i,indent=0):
        i=i.strip(';')
        l=i.split('=')
        
        if(l[0].strip(' ') in intvar.keys() or l[0].strip(' ') in strvar.keys() or l[0].strip(' ') in floatvar.keys() or l[0].strip(' ') in local):
            print('\t'*indent,end='',file=fo)
            print(i.strip(' '),file=fo)

    def cout(i,indent=0):
        l=''
        i.strip(';')
        i.strip(' ')
        for j in i.split('<<')[1:]:
            l+=j+','
        l=l.strip(',')
        l=l.strip(';');l=l.replace(';','');l=l.strip(' ')
        print('\t'*indent,end='',file=fo)
        print('print(',l,",end=''",')',sep='',file=fo)
        
    def cin(i,indent=0):
        i=i.strip(';')
        i=i.split('>>')
        for j in i[1:]:
            j=j.replace(' ','')
            if j in intvar.keys():
               print('\t'*indent,end='',file=fo)
               print(j,'=','int(input())',file=fo)
            if j in strvar.keys():
               print('\t'*indent,end='',file=fo)
               print(j,'=','input()',file=fo)
            if j in floatvar.keys():
               print('\t'*indent,end='',file=fo)
               print(j,'=','float(input())',file=fo)
    def ifcond(i,indent=0):
        if('&&' in i):
            i=i.replace('&&','and')
        if('||' in i):
            i=i.replace('||','or')
        i=i.strip()
        print('\t'*indent,end='',file=fo)
        print(i,":",sep="",file=fo)
    def elifcond(i,indent=0):
        if('&&' in i):
            i=i.replace('&&','and')
        if('||' in i):
            i=i.replace('||','or')
        i=i.strip()
        i=i.strip()
        i=i.replace('else if','elif')
        print('\t'*indent,end='',file=fo)
        print(i,":",sep="",file=fo)

    def forheader(i,indent=0):
        l=i
        k1=i    
        fstring=""
        step=0
        f=0
        var=(i[i.index("("):i.index("=")]).strip("(")
        l1=var.replace('int ','')
        t=(i[i.index("="):i.index(";")]).strip("=")
        k=i[i.index(""):i.index(";")]
        i=(i.strip(k)).strip(";")
        k1=k1[k1.index(';',1):k1.index(')')]
        k1=k1.strip(';')
        k1=k1.split(';')[1]
        
        if ("<=" in i):
            phigh=(i[i.index("<="):i.index(";")]).strip("<=")
            fstring=fstring+"for "+str(var).replace('int','')+" in range ("+str(t)+","+str(phigh)+'+1'+","
            f=1
        elif ("<"in i):
            phigh=(i[i.index("<"):i.index(";")]).strip("<=")
            fstring=fstring+"for "+str(var).replace('int','')+" in range ("+str(t)+","+str(phigh)+","
            f=1
        elif (">=" in i):
            plow=(i[i.index(">="):i.index(";")]).strip(">=")
            fstring=fstring+"for "+str(var).replace('int','')+" in range ("+str(t)+","+str(plow)+'-1'+","
            f=1
        elif (">" in i):
            plow=(i[i.index(">"):i.index(";")]).strip(">")
            fstring=fstring+"for "+str(var).replace('int','')+" in range ("+str(t)+","+str(plow)+","
            f=1
        elif ("==" in i or "!=" in i or"&&" in i or "||" in i):
                global countf            
                countf+=1  
                global inc
                inc.append(k1)
                print('\t'*indent,end='',file=fo)            
                print(l1,'=',t,file=fo)
                whileheader1(l,indent)
                return
        
        if f==1:
                k=i[i.index(";"):i.index(")")].strip(";")
                if ("++" in i):
                    step=1
                elif ("--" in i):
                    step=-1
                fstring=fstring+str(step)+"):"
                print('\t'*indent,end='',file=fo)
                print(fstring,file=fo)
        
    def escfixn(i):
        if '\n' in i:
            p=i.split("\n")
            t=""
            for k in p:
                t=t+"\\n"+k
            t=t.strip("\\n")
            i=t
            return (i)
        else:
            return (i)    
    def ret(i,indent=0):
        i=i.strip(';');i=i.strip(' ')
        print('\t'*indent,end='',file=fo)
        print(i,file=fo)

    def escfixt(i):
        if '\t' in i:
            p=i.split("\t")
            t=""
            for k in p:
                t=t+"\\t"+k
            t=t.strip("\\t")
            i=t
            return (i)
        else:
            return (i)    
    def incdre(i,indent=0):
        i=i.strip(';');i=i.replace(';','')
        i=i.strip()
        if ('++' in i):
            i=i.strip('++')
            print('\t'*indent,end='',file=fo)
            print(i,'+=','1',file=fo)
        else:
            i=i.strip('--')
            print('\t'*indent,end='',file=fo)
            print(i,'-=','1',file=fo)
    def funcall(i,indent=0):
        print('\t'*indent,end='',file=fo)
        print(i,file=fo)
       
                    
        
    flag=0
    count=0
    countc=0
    countf=0
    countm=0
    inc=list()
    fileinput()
    for i in s.splitlines():
        i=escfixn(i)
        if ("cout" not in i):
            i=escfixt(i);
        if('//' in i and '=' not in i and "cout" not in i and 'return'not in i ):
            i=i.replace('//','#');print(i,file=fo)
        if "\n" in i:
            i=i.replace("\n","\\n")
        if "\t" in i:
            i=i.replace("\t","\\t")
        if 'main()' in i:
            countm=1
            flag=-1
        if(funcdecider(i)==1):
            pass
        
        for j in func_name:
            if (j in i and ';' not in i and 'return' not in i ) : #diff between function header and function call
                count=flag
                funcprinter(j,i,count)
            if(j in i and ';' in i  and 'int ' not in i and 'char ' not in i and 'float ' not in i and 'double ' not in i and 'void' not in i and 'cout' not in i and 'return' not in i):
                funcall(i.strip(';'),count)
        for j in class_list:
            if(j in i and 'int' not in i and 'float' not in i and 'char' not in i and " " in i and "." not in i and 'double' not in i and j not in func_name and 'cout' not in i and "cin" not in i and 'void' not in i and '=' not in i and ";" in i ):
                k=((i.strip(';')).replace(j,"")).strip(" ")
                print(k,'=',j,'()',file=fo)
        if('cout' in i):
            cout(i,count)        
        if 'class' in i:
            countc+=1
            class_list.append(i.replace('class','').strip())
            print('\t'*flag,end='',file=fo)
            print(i,':',file=fo)
        if('{' in i):
            flag+=1
            count=flag 
        if('}'in i) :
            if countm==0:
               if countf+1==flag and countf!=0:
                    if ('++' in inc[countf-1] or '--' in inc[countf-1]):
                        incdre(inc[countf-1],flag)
                        countf-=1
                    else:
                        print('\t'*(flag),file=fo,end='')
                        print(inc[countf-1],file=fo)
                        countf-=1
            else:
                if countf==flag and countf!=0:
                    if ('++' in inc[countf-1] or '--' in inc[countf-1]):
                        incdre(inc[countf-1],flag)
                        countf-=1
                    else:
                        print('\t'*(flag),file=fo,end='')
                        print(inc[countf-1],file=fo)
                        countf-=1
            if countc==flag and countc!=0:
                    countc-=1
            flag-=1
            count=flag
        if(('int ' in i or 'char ' in i or 'float ' in i or 'double ' in i) and 'for' not in i  ) :
            createvaribles(i,count)
        if(('int ' in i or 'char ' in i or 'float ' in i or 'double ' in i)and '=' in i and ',' in i and 'for' not in i):
            createvariables1(i,count)
        if('if' in i and 'else if' not in i and 'cout' not in i):
            count=flag
            ifcond(i,count)
        if('else if' in i ):
            count=flag
            elifcond(i,count)
        if('else' in i and 'else if' not in i):
            i=i.strip()
            print('\t'*flag,end='',file=fo)
            print(i,':',file=fo)
        if('for' in i and 'cout'not in i ): 
            count=flag
            forheader(i,count)   
        if('cin' in i):
            cin(i,count)
        if('#include<math.h>' in i):
            print('import math',file=fo)
        if('while' in i):
            whileheader(i,count)
        if (('--' in i or '++' in i) and 'for' not in i):
            incdre(i,count) 
        if('=' in i):
            decl(i,count)
        if('random()' in i):
            random2(i)
        if("return" in i):
            ret(i,count)
        
    print('input()',file=fo)    
    f.close()
    fo.close()
    print(intvar)
    print(floatvar)
    print(strvar)
    print(func_name)
    print (class_list)
    print("Coversion successful!")
    kf=int(input("Press 1 for one more conversion\nPress 2 to End:"))

            
            
        
