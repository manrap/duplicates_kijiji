import sys

class Shingle:
    
       
    #hash flag is used to choose between hashed based or normal shingles
    def __init__(self, _file, size, hash_flag):
        j=1
	   
        shingle_set=[]
        
        self.size = size 
     
        f = open(_file,'r')
        j=1  
        for line in f:
          
             doc_sh=[] 
             description = line.split("\t")[5].strip()
             link = line.split("\t")[4].strip()
             
                         
             for i in range(0, len(description)-size+1):
                 
                    if hash_flag==1:
                        
                      doc_sh.append(int(hash(description[i:i+size])% ((sys.maxsize + 1) * 2)))
                    else:
                        
                      doc_sh.append((description[i:i+size]))
                     
             #  set of shingles for a doc
             
             shingle_set.append([j,set(doc_sh)])
             
                   
             j+=1
        
        
        self.shingle_list=shingle_set
         
    def __call__(self):
        
        
        
        return self.shingle_list
if __name__=="__main__":
    
    
    sh = Shingle("kijiji_ads.tsv", 10)
    print 'shingling complete'
    
    shingle_file = open("shingle_test.txt","w")
   
    print len(sh.shingle_list)
    for shingle in sh.shingle_list:
        shingle_file.write("%s\n" % shingle)
    
    shingle_file.close()

