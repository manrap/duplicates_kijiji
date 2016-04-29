from collections import defaultdict
from shingles import Shingle
from minhash import Minhash
from Jaccard_Sim import jaccardSim 
import time

class LSH:
    """
    
    formula to estimate the rows and bands given the jacc similarity treshold and the signature length
    (1/x)^(1/y) = 0.8, x*y = sig_length
    """
    def __init__(self, minhash_sig, bands, rows): 
        
        self.bands=bands
        self.rows=rows
        
        sig_length = bands*rows
        i=0
        pairs = set()
        duplicates = set()
        
        #for every band
        while (i<sig_length):
            j=0
            
            #temporary list with all the doc for a particular lsh hash
            band_dict=defaultdict(list)
            for signature in minhash_sig:
                num,sig=signature  
                #for each document
                column = sig[i:i+rows]
                
                temp_hash=""                              
                for row in column:
                   
                    temp_hash=temp_hash+str(row)
                
                #bandHash the hash of one band of document j
                bandHash = hash(temp_hash) 
                
                #for every hash i append the documents that hash to that value
                band_dict[bandHash].append(j)
                j=j+1

            

            
            for bucket in band_dict.values():

                #if a bucket has only 1 document it won't have any duplicate  
                if len(bucket)!=1: 
                   
                    for doc in bucket:

                        for doc2 in bucket:
                          
                            if doc<doc2: 
                                    duplicates.add(doc2)
                        
                                    pairs.add(tuple([doc,doc2])) 


            i = i+rows

        self.pairs= pairs
        self.duplicates=duplicates
              
          
    def __call__(self):
        return self.duplicates
    

                
if __name__=="__main__":
    print "Starting..."
    
    # '0' measn unhashed shingles, put '1' to hash the shingles
    sh = Shingle("kijiji_ads.tsv", 10,0)
    print "shingling complete"
    
    print "starting Jaccard similarity comparison"
    start = time.time()
    
    J_sim = jaccardSim()
    print "Pairs which have at least 80% Jaccard similarity"
    jac_list = J_sim.Jacc_sim(sorted(sh.shingle_list), 0.8)    
    
    #ads which have at least 1 duplicate
    print "Jaccard similarity duplicate ads: "+str(len(jac_list))
    print "Jaccard similarity time: "+str(time.time() - start)    
    
    print "starting minhashing.."
    start = time.time()
    minhash = Minhash (sorted(sh.shingle_list), 24)
    print 'minhash signature created'
    print "minhash time: "+str(time.time() - start)
    
    start = time.time()
    print "starting LSH.."
    
    #LSH(sig,b,r)
    
    lsh = LSH(minhash.signature, 6,4)
    
    #occurences of duplicates
    print "LSH pairs: "+str(len(lsh.pairs))
    
    #ads which are duplicated at least once
    print "LSH near duplicates: "+str(len(lsh.duplicates))
    print "LSH time: "+str(time.time()-start)    
     
    print "Intersection between LSH and Jaccard similarity duplicates: "+str(len((lsh.duplicates.intersection(jac_list))))
 
