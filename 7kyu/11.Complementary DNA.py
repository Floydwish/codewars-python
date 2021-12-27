'''
11.Complementary DNA

Instructions

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and 
carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); 
you need to get the other complementary side. DNA strand is never empty or 
there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
dnaStrand []        `shouldBe` []
dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]

'''

#solution 1
#1.特殊检查
#2.string转为list
#3.按照对应关系修改list
#4.连接string
def DNA_strand(dna):
    if len(dna)==0: return dna
    l = list(dna)
    for i in range(len(l)):
        if l[i]=='A':
            l[i]='T'
        elif l[i]=='T':
            l[i]='A'
        elif l[i]=='C':
            l[i]='G'
        elif l[i]=='G':
            l[i]='C'
    return ''.join(l)


#solution 2
#0.solution 1优化
#1.将字符一一对应转换,添加到目标string
def DNA_strand(dna):
    ret = ""
    for s in dna:
        if s=='A':
            ret+='T'
        elif s=='T':
            ret+='A'
        elif s=='C':
            ret+='G'
        elif s=='G':
            ret+='C'
    return ret


#solution 3
#1.建立字典结构
#2.循环匹配并从字典中提取对应字符
#3.连接字符
def DNA_strand(dna):
    pairs={'A':'T','T':'A','C':'G','G':'C'};
    return ''.join(pairs[s] for s in dna)


#solution 4
#1.使用string的translate()转换
#2.使用string的maketrans()创建映射表
def DNA_strand(dna):
    return dna.translate(dna.maketrans('ATCG','TAGC'))











