# duplicates_kijiji
Duplicate finder for job ads on kijiji.com, using shingling, min-hashing and locality sensitive hashing.

kiji_ads.tsv is a tab separated file containing ads to be checked for duplicates in the form: 
<title> /t <description> /t <where> /t <date> /t <ad URL> /t <full description>

shingles.py does the shingling of the full descriptions of every ad, it can be done also in an hash-based way.

minhash.py does the minhash signature of a shingle set, with variable signature length and using a random
hash funcion family created by hashFamily.py.

lsh_main.py defines the class LSH that implemente locality sensitive hashing of the minhash signatures and hosts the starting point of the application.
