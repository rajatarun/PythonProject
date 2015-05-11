'''
Created on Dec 16, 2014

@author: rajatarun
'''
import matplotlib.pyplot as mp;
import numpy as np;
class DiscreteMath():
    def affineciper(self,a,b):
        while True:
            try:
                modulo = 26
                #modulo = 12
                final1 = dict();
                result = [];
                for i in range(modulo):
                    result.append((a*i)%modulo);
                final = [];
                for i in range(modulo):
                    if result[i] == 1:
                        final.append(i);
                #print(final);
                var = (-(final[0]*b))%modulo;
                print("x = {}y+{}".format(final[0],var));
                break;
            except IndexError:
                print("number {} has no inverse".format(a));
                break;
    def andgate(self):    
        def andg(inputs):
            counter = 0;
            for i in inputs:
                if(i!=0 and i!= 1):
                    counter = counter+1;
                else:
                    if(i==0):
                        state1 = 0;
                        break;
                    else:
                        state1 = 1;
            if(counter != 0):
                print("enter either 0 or 1");
                    
            else:
                if(state1 == 0):
                    #print('{0}    {1}'.format(inputs,state));
                    return(state1);
                else:
                    #print('{0}    {1}'.format(inputs,1));
                    return(state1);
        while True:
            try:
                inputs = input("enter the inputs to and gate either 0 or 1 : ");
                var = andg(inputs);
                if(var == 0):
                    print('{0}    {1}'.format(inputs,var));
                if(var == 1):
                    print('{0}    {1}'.format(inputs,var));
                if(var == 0 or var ==1):
                    break;
            except NameError:
                print("Enter only numbers try again .. .. ..");
            except TypeError:
                print("Enter either 0 or 1 only seperated by ',' .. .. ..")
    def factorial(self,num):
        product = 1;
        if(num == 0):
            return(1);
        for i in range(1,num+1):
            product = product * i;
        return(product);
    def binomialdistribution(self):
        while True:    
            try:        
                noc = input("give number of cases :  ");
                prob = input("probability of success : ");
                if noc==0:
                    raise ValueError();
                    continue;
                sumof = 0;
                allvalues = [];
                for i in range(0,noc+1):
                    num = self.factorial(noc)/(self.factorial(i)*self.factorial(noc-i));
                    result = 0;
                    probab = (((prob)**(i))*((1-prob)**(noc-i))); 
                    result = num*probab;
                    sumof = sumof +result;
                    allvalues.append(result);
                    print('{0}     {1}'.format(i,result));
                print("total {}".format(sumof));
                index1 = max(allvalues);
                print("max value is {0} at {1} ".format(index1,allvalues.index(index1)));
                mp.plot(allvalues);
                mp.show();
                break;
            except NameError:
                print("Enter only Numbers .. .. ..");
            except TypeError:
                print("Enter valid numbers .. .. ..");
            except SyntaxError:
                print("Please enter some number.. .. ..");
            except ValueError:
                print("number of cases should be greater than zero .. .. ..");
    def circularpermutations(self):
        print("The number of ways to arrange n distinct objects in circle ");
        while True:
            try:
                n = raw_input("enter n: ");  #take the input of number of distinct objects
                if(int(n)>0):
                    result = self.factorial(int(n)-1);#return value to factorial function
                    print("The number of ways to arrange {0} distinct objects in circle          {1}".format(n,result));
                    break;
                else:
                    print("Enter number greater than 0");
            except NameError:
                print("Enter a Integer");
            except ValueError:
                print("Enter a Integer");
    def combinations(self):
        while True:
            try:
                print("enter the numbers in (n r) format");
                n = int(raw_input("enter n: "));
                r = int(raw_input("enter r: "));
                if(n<r):
                    raise NameError;
                result = self.factorial(n)/(self.factorial(r)*self.factorial(n-r));
                print(result); 
                break;
            except ValueError:
                print("Enter only numbers .. .. ..");
            except NameError:
                print("N should be greter than R");
            except SyntaxError:
                print("Only numbers do not enter special characters")   
    def combinationswithrepetetions(self):
        while True:
            try:
                print("enter the numbers in (n r) format");
                n = int(raw_input("enter n: "));
                r = int(raw_input("enter r: "));
                if (n == 0 and r == 0):
                    print("there's only one way to choose nothing from ... nothing... :D ");
                if(n<r):
                    raise RuntimeError();
                result = self.factorial(n+r-1)/(self.factorial(r)*self.factorial(n-1));
                print(result); 
                break;
            except ValueError:
                print("Enter only numbers .. .. ..");
            except RuntimeError:
                print("Enter N greater than R.. .. ..");
    def DoubleFactorialBinomialCoefficients(self):
        def even(num):
            b =(2**(num/2));
            a = (b*self.factorial(num/2));
            return(a);
        def odd(num):
            temp = num+1;
            a =self.factorial(temp)/even(temp);
            return(a);
        def dfbc(num,rec):
            if(num % 2 == 0):
                top=even(num);
                #print(top);
            else:
                top=odd(num);
            if(rec%2 == 0):
                bottom = even(rec);
                #print(bottom);
            else:
                bottom = odd(rec);
            if((num-rec)%2 == 0):
                bottom1 = even(num-rec);
                #print(bottom1);
            else:
                bottom1 = odd(num-rec);
            result = top/(bottom*bottom1);
            print(result);  
        while True:
            try:
                print("enter the numbers in (n r) format");
                n = float(raw_input("enter n: "));
                r = float(raw_input("enter r: "));
                if (n == 0 and r == 0):
                    print("there's only one way to choose nothing from ... nothing... :D ");
                if(n<r):
                    raise RuntimeError();
                dfbc(n,r);
                break;
                #print(n-r);
                #result = factorial(factorial(n))/(factorial(factorial(r))*factorial(factorial(n-r)));
            except ValueError:
                print("Enter only numbers .. .. ..");
            except RuntimeError:
                print("Enter N grater than R.. .. ..");    
    def DoubleFactorial(self):
        def even(num):
            b =(2**(num/2));
            #print(b);
            a = (b*self.factorial(num/2));
            #print(a);
            return(a);
        def odd(num):
            temp = num+1;
            a =self.factorial(temp)/even(temp);
            #print(temp);
            return(a);
        def dfbc(num):
            if(num % 2 == 0):
                top=even(num);
        #print(top);
            else:
                top=odd(num);
            print(top);  
        while True:
            try:
                print("enter the number to calculate double factorial");
                n = float(raw_input("enter n: "));
                if(n<0):
                    raise ZeroDivisionError();
                dfbc(n);
                break;
            except ValueError():
                print("Enter a valid number.. .. ..");
            except ZeroDivisionError():
                print("Enter number greater than zero .. .. ..");
    def factorialPqform(self):
        while True:
            try:
                num =input('enter the numerator numbers:');
                den = input('enter the denominator numbers:');
                if(num >=0 and den >=0):
                    num1 = 1;
                    try:
                        for i in num:
                            num1 = num1 * self.factorial(i);
                        den1 = 1;
                    except TypeError:
                        num1 = self.factorial(num);
                    for i in den:
                        den1 = den1*self.factorial(i);
                    result = num1/den1;
                    print(float(result));
                    break;
            except NameError:
                print("Enter a Integer");
            except ValueError:
                print("Enter a Integer");
    def GeometricDistribution(self):
        while True:
            try:
                noc = input("give at which trial it should occur :  ");
                prob = input("probability of event happening : ");
                probab = ((prob)*((1-prob)**(noc-1))); 
                estimate = 1/prob;
                var = ((1-prob)/(prob**2));    
                print('proability after {0} trials       {1}'.format(noc,probab));
                print('Estimated value                   {0}'.format(estimate));
                print('variance                          {0}'.format(var));
                break;
            except ZeroDivisionError:
                    print("Enter Values Greater than 0 .. .. ..");
                    continue;
            except NameError:
                print("Enter only Numbers .. .. ..");
                continue;
            except TypeError:
                print("Dont use special characters only numbers.. .. ..");
                continue;
            except ValueError():
                print("Enter only numbers.. .. ..");
    def HyperGeometric(self):
        while True:
            try:
                differenttotals = input("Enter the total amount of different objects in total set : ");
                differentdraws = input("Enter the drawn objects from individual sets correspondingly : ");
                if(len(differenttotals) == len(differentdraws)):
                    result = 1;
                    for i in range(0,len(differenttotals)):    
                        result = result*((self.factorial(differenttotals[i])/((self.factorial(differentdraws[i])*self.factorial(differenttotals[i]-differentdraws[i])))));
                    sumo = 0;
                    for i in differenttotals:
                        sumo =sumo+i;
                    sum1 = 0;
                    for i in differentdraws: 
                        sum1 = sum1+i;
                    n = sumo;
                    r = sum1;
                    den = float(self.factorial(n)/(self.factorial(r)*self.factorial(n-r)));
                
                    finalresult = float(result/den);
                    print(finalresult); 
                    break;
                else:
                    print("enter equal number of total objects and drawn objects")
            except TypeError:
                print("Enter multiple sets for single case use combinations .. .. ..")
            except NameError:
                print("Enter  only Numbers.. .. ..");
            except SyntaxError:
                print("Enter only numbers dont use special characters .. .. ..");            
    def Multinomial(self):
        while True:
            try:
                print("multinomial coefficient");
                s =input('enter the numbers:');
                addi = 0;
                for i in s:
                    addi = addi +i;
                den = 1;
                for i in s:
                    den = den*self.factorial(i);
                result = self.factorial(addi)/den;
                print(result);
                break;
            except ValueError:
                print("");
            except TypeError:
                print("enter multiple numbers or use factorial pq .. .. ..");
            except NameError:
                print("Enter only numbers.. .. ..");
            except SyntaxError:
                print("avoid Special characters.. ... ..");    
    def NandGate(self):
        def nandgate(self,inputs):
            counter = 0;
            for i in inputs:
                if(i!=0 and i!= 1):
                    counter = counter+1;
                else:
                    if(i==0):
                        state1 = 0;
                        break;
                    else:
                        state1 =1;
            if(counter != 0):
                print("enter either 0 or 1");
                    
            else:
                if(state1 == 0):
                    #print('{0}    {1}'.format(inputs,state));
                    return(state1);
                else:
                    #print('{0}    {1}'.format(inputs,1));
                    return(state1);
        
        
        while True:
            try:
                inputs = input("enter the inputs to nand gate either 0 or 1 : ");
                var = nandgate(inputs);
                if(var == 0):
                    print('{0}    {1}'.format(inputs,1));
                if(var == 1):
                    print('{0}    {1}'.format(inputs,0));
                break;
            except NameError:
                print("Enter only numbers try again .. .. ..");
            except TypeError:
                print("Enter either 0 or 1 only seperated by ',' .. .. ..");
            except SyntaxError:
                print("Don't enter special characters.. .. ..");
    def NorGate(self):
        def norgate(inputs):
            counter = 0;
            counter1 = 0;
            for i in inputs:
                if(i!=0 and i!= 1):
                    counter = counter+1;
                if(i==0):
                    counter1 = counter1+1;    
            if(counter != 0):
                print("enter either 0 or 1");        
            else:
                if(counter1 == len(inputs)):
                    state = 0;
                    #print('{0}    {state}'.format(inputs,state = 0));
                    return(state);
                else:
                    state =1;
                    #print('{0}    {state}'.format(inputs,state = 1));
                    return(state);

        while True:
            try:
                inputs = input("enter the inputs to and gate either 0 or 1 : ");
                var = norgate(inputs);
                if(var == 0):
                    print('{0}    {1}'.format(inputs,1));
                if(var == 1):
                    print('{0}    {1}'.format(inputs,0));
                break;
            except NameError:
                print("Enter only numbers try again .. .. ..");
            except TypeError:
                print("Enter either 0 or 1 only seperated by ',' .. .. ..");
            except SyntaxError:
                print("Don't Enter Special characters .. .. ..");            
    def InverseOfNumberInMod(self):
        number = input("enter the number to find inverse: ");
        modulo = input("enter modulo : ")
        #modulo = 12
        final1 = dict();
        result = [];
        for i in range(modulo):
            result.append((number*i)%modulo);
        final = [];
        for i in range(modulo):
            if result[i] == 1:
                final.append(i);
        if (final == []):
            print("There is no inverse for this number in mod {}".format(modulo));
        else:
            print(final);
    def OrGate(self):
        def orgate(inputs):
            counter = 0;
            counter1 = 0;
            for i in inputs:
                if(i!=0 and i!= 1):
                    counter = counter+1;
                if(i==0):
                    counter1 = counter1+1;    
            if(counter != 0):
                print("enter either 0 or 1");        
            else:
                if(counter1 == len(inputs)):
                    state = 0;
                    #print('{0}    {state}'.format(inputs,state = 0));
                    return(state);
                else:
                    state =1;
                    #print('{0}    {state}'.format(inputs,state = 1));
                    return(state);
        while True:
            try:
                inputs = input("enter the inputs to and gate either 0 or 1 : ");
                var = orgate(inputs);
                if(var == 0):
                    print('{0}    {1}'.format(inputs,var));
                if(var == 1):
                    print('{0}    {1}'.format(inputs,var));
                break;
            except NameError:
                print("Enter only numbers try again .. .. ..");
            except TypeError:
                print("Enter either 0 or 1 only seperated by ',' .. .. ..");
            except SyntaxError:
                print("Don't Enter special characters.. .. ..");
    def Permutation(self):
        while True:
            try:
                print("enter the numbers in (n r) format");
                n = int(raw_input("enter n: "));
                r = int(raw_input("enter r: "));
                if(n<r):
                    raise NameError;
                result = self.factorial(n)/self.factorial(n-r);
                print(result); 
                break;
            except ValueError:
                print("Enter only numbers .. .. ..");   
            except SyntaxError:
                print("Don't Enter special characters.. .. .. ");
            except NameError:
                print("N should be greater than r");
    def PermutationWithRepetetion(self):
        while True:
            try:
                print("enter the numbers in (n r) format");
                n = int(raw_input("enter the size n: "));
                r = int(raw_input("enter of items to be chosen r: "));
                if(n<r):
                    raise NameError;
                result = n**r;
                print(result);
                break;
            except ValueError:
                print("Enter only numbers .. .. ..");   
            except SyntaxError:
                print("Don't Enter special characters.. .. .. ");
            except NameError:
                print("N should be greater than r"); 
    def Thresholdgate(self):
        def output(w,i,t):
            product = 0;
            if (len(w) == len(i)):
                for j in range(0,len(w)):
                    product = product+(w[j]*int(i[j]));
            else:
                print("inputs and weights do not match");
            if(product >= t):
                #return(1);
                print('{0}     {1}'.format(i,1));
            else:
                #return(0);
                print('{0}     {1}'.format(i,0));
        weights = input("Enter the weights of gate : ");
        #inputs = input("Enter the total number of inputs");
        threshold = input("enter the threshold");
        inputs1 = ['{:0{width}b}'.format(i, width=len(weights)) for i in range(2**len(weights))];
        for i in inputs1:
            out = output(weights,i,threshold);
    def ToutientNumber(self):
        modulo = input("enter modulo : ")
        final1 = dict();
        result = [];
        for j in range(modulo):
            result = [];
            for i in range(modulo):
                result.append((j*i)%modulo);
            final = [];
            for i in range(modulo):
                if result[i] == 1:
                    final.append(i);
            #print(final);
            #final =[i if result[i] == 1 for i in range(modulo)];
            final1[j]= final;
        count = dict();
        for i in final1:
            if(final1[i] != []):
                #print("{} : {}".format(i,final1[i]));
                count[i] = final1[i];
        #select = input("choose 1: inverse of all elemets 2: total number of elements");
        #if(select == 1):
        #    print(count);
        #if(select == 2):
        print("the totient number is {}".format(len(count))); 
    def QuineMcCluskeyAlgo(self):
        def comparearray(a,b):
            import numpy as np
            values = np.array(a);
            searchval = '_'
            i1= np.where(values == searchval);
            values = np.array(b);
            searchval = '_'
            i2= np.where(values == searchval);
            j1 = np.array(i1).tolist()
            j2 = np.array(i2).tolist()
            if (len(j1[0]) == len(j2[0])):
                if (j1[0] == j2[0]):
                    return(True);
                else:
                    return(False);
            else:
                return(False);

        #import pdb;
        def unique_rows(a):
            if(len(a) == 0):
                return(0);
            a = np.ascontiguousarray(a)
            unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
            return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]));
        def check(a,b):
            check1 = 0;
            for i in range(len(a)):
                if((a[i]=='0' and b[i] == '1')):
                    check1 = check1 +1;
                if( (a[i]=='1' and b[i] == '0')):
                    check1 = check1 +1;
            if(check1 <= 1):
                return(True);
            else: 
                return(False);
        def finalprint(y):
            checked = dict();
            unchecked = dict();
            import operator;
            v=[];
            for i in range(len(y)):
                unchecked[i] = y[i].tolist();
                checked[i] = unchecked[i].count('_');
            for k in range((checked[checked[max(checked.iteritems(), key=operator.itemgetter(1))[0]]])+2):
                for i in range(0,len(checked)):
                    if(checked[i] == k):
                        v.append(unchecked[i]);
            for i in range(0,len(v)):
                del v[i][0];
                del v[i][0];
                #print(v[i]);
            return(v);    
        def possible_sequences(seq):
            n = seq.count('_')
            seq = seq.replace('_', '{}')
            return [seq.format(*'{:0{width}b}'.format(i, width=n))
                    for i in range(2**n)]
        a =dict();
        b =dict();
        f = raw_input('enter length of bit stream: ');
        j = int(f); 
        d = '#0{}b'.format(f);
        for i in range(0,pow(2,int(f))):
            a[i] = format(i,d);
            a[i] = a[i].zfill(int(f)+2);
            a[i] = a[i].replace('b','0');
            b[i] = a[i].count('1');
        c = [];
        for k in range(0,int(f)):
            for i in b:
                if(k==b[i]):
                    c.append(i);
        
        c.append(pow(2,int(f))-1);
        #print(c);
        e = [];
        for i in c:
            e.append(format(i,d));
        #print(e);
        g = [];
        for i in range(0,len(e)):
            g.append(e[i].zfill(int(f)+2));
        #print(g);
        for i in range(0,len(e)):
            g[i] = g[i].replace('b','0');
        fintable = [];
        for i in range(0,len(g)):
            fintable.append(raw_input('enter the output of {}:  '.format(g[i])));
        #print(fintable);
        #print(g);
        finarray= [];
        for i in range (0,len(fintable)):
            if (fintable[i] == '1'):
                finarray.append(g[i]);
        print(finarray);
        newlist = finarray;
        temp = [];
        primeim = [];
        for l in range(j):
            counter = 0;
            for i in range(0,len(finarray)):
                
                for j in range(i+1,len(finarray)):
                    if(finarray[j].count('1')-finarray[i].count('1') == 1):
                        
                        if (finarray[i].__contains__('_') == True):
                            #counter += 1;
                            if( comparearray(finarray[i],finarray[j]) == True):
                                counter += 1;
                                for k in range(0,int(f)+2):
                                    if(finarray[i][k] != finarray[j][k]):
                                        #pdb.test();
                                        if(check(finarray[i],finarray[j])==True):
                                            #pdb.set_trace();
                                            temp1 = list(finarray[j]);
                                            temp1[k] = '_';
                                            #pdb.set_trace();
                                            temp.append(temp1);
                                        
                            #else:
                            #   if(counter==0):
                            #        primeim.append(finarray[i]);
                            #    continue;
                        else:
                            counter += 1;
                            for k in range(0,int(f)+2):
                                if(check(finarray[i],finarray[j]) == True):
                                    if(finarray[i][k] != finarray[j][k]):
                                            temp1 = list(finarray[j]);
                                            temp1[k] = '_'; 
                                            temp.append(temp1);
                    else:
                        continue;
                if(counter < 1):
                    primeim.append(finarray[i]);
                    
            finarray = temp;
        z = np.array(temp);
        y = unique_rows(z);
        x = np.array(primeim);
        w = unique_rows(x);                   
        #for i in y:
        #    print(i)
        final = finalprint(y);
        str1= [];
        for i in range(len(final)):
            str1.append(''.join(final[i]));
        computed = {v : possible_sequences(v) for v in str1};
        t = [];
        for i in computed:
            t.append(computed[i]);
        
        tn = dict();
        for i in range(len(t)):
            tn[i] = t[i];
        tr = dict();
        for i in range(len(computed)):
            c = [int(j,2) for j in tn[i]];
            tr[i] = c;
        tb = []
        for k in sorted(tr, key=lambda k: len(tr[k]), reverse=False):
                tb.append(tr[k]);
        td = dict();
        for i in range(len(tb)):
            td[i] = tb[i];
        #print(td);
        tb2 = tb[:];
        for m in tb:
                for n in tb2:
                        if (set(m).issubset(set(n)) and m != n):
                            tb2.remove(m)
                            break;
        print(tb2);
        tb3 = []
        for i in tb2:
            for name, age in tr.iteritems():
                    if (age == i ):
                        tb3.append(name);
        tb4 = [];
        tb4.append(computed.keys());
        print("Essential prime implicants")
        for i in tb3:
            print(tb4[0][i]);
        
                    
        print('break');
        
        #for i in w:
        #print(i);
        #if(primeim!=0):
        #    finalprint(primeim);




