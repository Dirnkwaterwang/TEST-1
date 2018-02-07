import re
f1 = open('1529_annoted.hg38_multianno.txt','r')
f2 = open('1529_annoted.hg38_multianno_exonic.txt','w')
# firtst part  
k = f1.readlines()
for i in k:
    if i.split('\t')[5]=='Func.refGene':
        f2.write(i)
    elif i.split('\t')[5]=='exonic':
        if i.split('\t')[8]!='synonymous SNV':
            f2.write(i)
    else:
        pass
    
f1.close()
f2.close() # the first part select the exonic and nonsy SNV


f3 = open('1529_annoted.hg38_multianno_exonic.txt','r')
f4 = open('1529_exonic_1%.txt','w')

g = f3.readlines()
for j in g:
    if j.split('\t')[5]=='Func.refGene':
        f4.write(j)
    else:
        if j.split('\t')[45]=='.':
            if j.split('\t')[61]=='.':
                if j.split('\t')[47]=='.':
                    f4.write(j)
                elif float(j.split('\t')[47])<0.01:
                    f4.write(j)
                else:
                    pass
            elif float(j.split('\t')[61])<0.01:
                if j.split('\t')[47]=='.':
                    f4.write(j)
                elif float(j.split('\t')[47])<0.01:
                    f4.write(j)
                else:
                    pass
            else:
                pass
        elif float(j.split('\t')[45])<0.01:
            if j.split('\t')[61]=='.':
                if j.split('\t')[47]=='.':
                    f4.write(j)
                elif float(j.split('\t')[47])<0.01:
                    f4.write(j)
                else:
                    pass

            elif float(j.split('\t')[61])<0.01:
                if j.split('\t')[47]=='.':
                    f4.write(j)
                elif float(j.split('\t')[47])<0.01:
                    f4.write(j)
                else:
                    pass
            else:
                pass
  
 
        else:
            pass 
f3.close()
f4.close()


                  



			
