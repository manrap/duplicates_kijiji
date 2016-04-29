import sys
from shingles import Shingle
from hashFamily import hashFamily

class Minhash:
  
    def __init__(self, docs, sig_length):
        
        hash_family = [hashFamily(i) for i in range(0, sig_length)]
        hash_vector=[]
        signature = []
        shingle_hash =[]
        
        j=0
        
        for doc in docs:
            num,shingles=doc
            #hash_vector = [sys.maxint for _ in range(k)]
            column=[]   
            for s in shingles:
                shingle_hash=[]
                for i in range(0,sig_length):
                   shingle_hash.append(hash_family[i](str(s)))
                   
                column.append(min(shingle_hash))
             
            signature.append([num,column])
        """
        for doc in docs:
            link, shingles = doc
            j+=1
            hash_vector = ["FFFFFFFF" for _ in range(0,sig_length)]

            for s in shingles:
                for i in range( len(hash_family)):
                    h = hash_family[i](str(s))
                    if h<hash_vector[i]:
                        hash_vector[i]=h
            item=[link, tuple(hash_vector)]
            print j
            signature.append(item)
         """
        
        self.signature = signature

    def __call__(self):
        return self.signature

if __name__=="__main__":
    
    sh = Shingle("kijiji_Ads.tsv", 10,0)
    print 'shingling complete'
     
    
    minhash = Minhash(sorted(sh.shingle_list), 24)
    #minhash= Minhash( sorted( sh.doc_shingles.items()), 30)
    print 'minhash signature created'
    out_file = open("minhash_test.txt","w")
    
    for sig in minhash.signature:    
            out_file.write("%s\n" % sig)
    

