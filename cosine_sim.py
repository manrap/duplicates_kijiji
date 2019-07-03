from shingles import Shingle
import time
from collections import defaultdict


class cosineSim:

    def cos_sim(self, docs, t):  
       
       
        #list that contains all duplicated pair occurences
        sim_docs= set()
        
        #list that contains the docs that are duplicated at least 1 time
        single_duplicates=set()


        for num1,shingles1 in docs:
            for num2,shingles2 in docs:
              if num1<num2:   
               intersection = len(shingles1.intersection(shingles2))
               j_sim=intersection / float(len(shingles1) + len(shingles2) - intersection) 
               if j_sim >= t:

                           #sim_docs.add(tuple([num1,num2,j_sim]))
                           sim_docs.add(tuple([num1,num2]))
                                            
            
        print "Jaccard similarity duplicate pairs: "+str(len(sim_docs))       
        
        
        for a,b in sim_docs:            
            
                 single_duplicates.add(b)
    
          
        self.sim_docs=sim_docs
        self.single_duplicates=single_duplicates
        
        return single_duplicates
        
        
if __name__ == "__main__":
    sh = Shingle("kijiji_Ads.tsv", 10)
    start = time.time()

    J_sim = jaccardSim()

    print "Pairs which have at least 80% Jaccard similarity"
    jac_list = J_sim.Jacc_sim(sorted(sh.shingle_list), 0.8)
    
    
    out_file=open("jac_test.txt","w")
    print len(jac_list)
    for pair in J_sim.sim_docs:
        out_file.write(str(pair)+"\n")
       
    end = (time.time() - start)
   
    print len(jac_list)
    print end

