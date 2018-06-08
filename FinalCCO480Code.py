import scipy.stats #module used for ttest
import numpy as np #module used to contain values in array for ttest

#protein sequences copied from various links

cGMP = ("AUGAAGACAAAUAUUAUCAAUACGUGGCACUCCUUCGUAAAUAUCCCCAACGUGGUUGUA"
        "CCAGCUAUCGAAAAGGAAAUUCGACGCAUGGAAAAUGGGGCGUGCAGCUCAUUUUCUGAC"
        "AAUGACAAUGGCUCUCUGUCUGAAGAAUCAGAGAAUGAGGACUCUCUCUUUAGAAGCAAC"
        "UCAUACAGAAGGCGAGGACCAUCCCAGAGGGAGCAUUACUUGCCAGGCACCAUGGCUCUU"
        "UUCAAUGUUAACAACAGCAGCAACAAAGACCAAGACCCAAAGGAGAAAAAGAAAAAGAAA"
        "AAGGAAAAGAAGAGCAAGGCCGAUGAUAAAAAGGAAAGUAAAAAGGACCCAGAGAAGAAA"
        "AAAAAGAAGGAAAAGGAAAAAGAGAAGAAAAAGGAGGAGAAACCCAAGGAAAAGAAAGAA"
        "GAGGAGAAAAAAGAGGUGGUUGUUAUUGACCCUUCAGGAAACAUGUACUACAACUGGCUG"
        "UUUUGUAUCACUUUACCUGUGAUGUACAACUGGACGAUGAUCAUUGCAAGAGCAUGUUUU"
        "GAUGAACUCCAGUCUGAUUACCUAGAAUAUUGGCUCAUUUUUGAUUACGUAUCAGAUGUA"
        "GUCUACCUUGCUGAUAUGUUUGUACGGACAAGGACAGGUUACCUGGAACAAGGGUUGCUA"
        "GUGAAGGACGAACUGAAACUCAUAGAGAAGUACAAAGCAAACCUGCAGUUUAAACUUGAC"
        "GUUCUGUCAGUGAUACCGACCGACCUGCUGUAUUUCAAGUUUGGGUGGAACUAUCCAGAA"
        "AUCAGGUUGAACCGGCUGUUAAGAAUCUCUCGGAUGUUUGAGUUCUUCCAGAGGACAGAG"
        "ACAAGGACCAACUACCCGAACAUCUUUAGGAUCUCAAACCUUGUGAUGUACAUUGUCAUC"
        "AUCAUCCACUGGAACGCGUGUGUGUACUACUCCAUCUCAAAAGCUAUUGGAUUUGGGAAU"
        "GACACAUGGGUCUACCCUGAUGUUAAUGAUCCUGAAUUUGGCCGUUUGGCUAGAAAAUAC"
        "GUCUACAGCCUUUAUUGGUCUACCUUGACUUUGACGACCAUUGGAGAAACCCCACCCCCC"
        "GUGCUGGAUUCCGAGUAUGUCUUUGUGGUGGUAGACUUCUUAAUUGGAGUUUUAAUUUUU"
        "GCCACCAUUGUCGGUAACAUAGGCUCCAUGAUUUCCAAUAUGAAUGCAGCCCGGGCAGAA"
        "UUUCAAUCAAGAGUUGAUGCUAUCAAACAGUACAUGAAUUUUCGAAAUGUGAGCAAAGAC"
        "AUGGAAAAGAGAGUUAUUAAAUGGUUUGACUACCUGUGGACCAACAAAAAGACAGUCGAU"
        "GAGAGAGAAGUUCUGAGAUACCUCCCUGACAAACUCAGGGCAGAGAUUGCCAUCAAUGUU"
        "CACCUAGACACGUUAAAAAAGGUUCGUAUCUUUGCUGACUGUGAGGCUGGUCUGUUGGUG"
        "GAGUUGGUGUUGAAAUUACAACCCCAGGUGUACAGUCCUGGAGAUUACAUAUGCAAGAAA"
        "GGGGACAUUGGGCGGGAGAUGUACAUCAUCAAGGAAGGCAAACUUGCUGUGGUGGCAGAC"
        "GACGGAAUCACACAGUUUGUGGUGUUGAGUGACGGCAGCUACUUUGGCGAGAUCAGCAUU"
        "CUUAACAUCAAAGGCAGCAAGGCUGGCAACCGAAGAACAGCCAAUAUUAAGAGCAUUGGC"
        "UACUCGGACCUGUUCUGCCUCUCAAAGGAUGACCUCAUGGAAGCUCUUACAGAGUACCCA"
        "GAUGCCAAAACUAUGUUGGAGGAGAAAGGGAGGCAGAUCUUAAUGAAAGACGGUCUACUG"
        "GAUAUAAACAUUGCGAAUUUGGGCAGUGACCCUAAAGACCUGGAAGAGAAGGUCACUCGA"
        "AUGGAGGGGUCAGUGGACCUCCUGCAAACACGAUUUGCCCGAAUCUUGGCUGAGUAUGAA"
        "UCGAUGCAGCAGAAACUCAAGCAAAGAUUAACCAAGGUUGAGAAAUUCUUGAAACCACUU"
        "AUUGAAACUGAAUUUUCAGCCCUUGAGGAACCCGGAGGAGAAAGUGAACCCACAGAGUCU"
        "CUACAGGGCUAA")

PKCTH = ("AUGUCGCCAUUUCUUCGGAUUGGCUUGUCCAACUUUGACUGCGGGUCCUGCCAGUCUUGU"
         "CAGGGCGAGGCUGUUAACCCUUACUGUGCUGUGCUCGUCAAAGAGUAUGUCGAAUCAGAG"
         "AACGGGCAGAUGUAUAUCCAGAAAAAGCCUACCAUGUACCCACCCUGGGACAGCACUUUU"
         "GAUGCCCAUAUCAACAAGGGAAGAGUCAUGCAGAUCAUUGUGAAAGGCAAAAACGUGGAC"
         "CUCAUCUCUGAAACCACCGUGGAGCUCUACUCGCUGGCUGAGAGGUGCAGGAAGAACAAC"
         "GGGAAGACAGAAAUAUGGUUAGAGCUGAAACCUCAAGGCCGAAUGCUAAUGAAUGCAAGA"
         "UACUUUCUGGAAAUGAGUGACACAAAGGACAUGAAUGAAUUUGAGACGGAAGGCUUCUUU"
         "GCUUUGCAUCAGCGCCGGGGUGCCAUCAAGCAGGCAAAGGUCCACCACGUCAAGUGCCAC"
         "GAGUUCACUGCCACCUUCUUCCCACAGCCCACAUUUUGCUCUGUCUGCCACGAGUUUGUC"
         "UGGGGCCUGAACAAACAGGGCUACCAGUGCCGACAAUGCAAUGCAGCAAUUCACAAGAAG"
         "UGUAUUGAUAAAGUUAUAGCAAAGUGCACAGGAUCAGCUAUCAAUAGCCGAGAAACCAUG"
         "UUCCACAAGGAGAGAUUCAAAAUUGACAUGCCACACAGAUUUAAAGUCUACAAUUACAAG"
         "AGCCCGACCUUCUGUGAACACUGUGGGACCCUGCUGUGGGGACUGGCACGGCAAGGACUC"
         "AAGUGUGAUGCAUGUGGCAUGAAUGUGCAUCAUAGAUGCCAGACAAAGGUGGCCAACCUU"
         "UGUGGCAUAAACCAGAAGCUAAUGGCUGAAGCGCUGGCCAUGAUUGAGAGCACUCAACAG"
         "GCUCGCUGCUUAAGAGAUACUGAACAGAUCUUCAGAGAAGGUCCGGUUGAAAUUGGUCUC"
         "CCAUGCUCCAUCAAAAAUGAAGCAAGGCCGCCAUGUUUACCGACACCGGGAAAAAGAGAG"
         "CCUCAGGGCAUUUCCUGGGAGUCUCCGUUGGAUGAGGUGGAUAAAAUGUGCCAUCUUCCA"
         "GAACCUGAACUGAACAAAGAAAGACCAUCUCUGCAGAUUAAACUAAAAAUUGAGGAUUUU"
         "AUCUUGCACAAAAUGUUGGGGAAAGGAAGUUUUGGCAAGGUCUUCCUGGCAGAAUUCAAG"
         "AAAACCAAUCAAUUUUUCGCAAUAAAGGCCUUAAAGAAAGAUGUGGUCUUGAUGGACGAU"
         "GAUGUUGAGUGCACGAUGGUAGAGAAGAGAGUUCUUUCCUUGGCCUGGGAGCAUCCGUUU"
         "CUGACGCACAUGUUUUGUACAUUCCAGACCAAGGAAAACCUCUUUUUUGUGAUGGAGUAC"
         "CUCAACGGAGGGGACUUAAUGUACCACAUCCAAAGCUGCCACAAGUUCGACCUUUCCAGA"
         "GCGACGUUUUAUGCUGCUGAAAUCAUUCUUGGUCUGCAGUUCCUUCAUUCCAAAGGAAUA"
         "GUCUACAGGGACCUGAAGCUAGAUAACAUCCUGUUAGACAAAGAUGGACAUAUCAAGAUC"
         "GCGGAUUUUGGAAUGUGCAAGGAGAACAUGUUAGGAGAUGCCAAGACGAAUACCUUCUGU"
         "GGGACACCUGACUACAUCGCCCCAGAGAUCUUGCUGGGUCAGAAAUACAACCACUCUGUG"
         "GACUGGUGGUCCUUCGGGGUUCUCCUUUAUGAAAUGCUGAUUGGUCAGUCGCCUUUCCAC"
         "GGGCAGGAUGAGGAGGAGCUCUUCCACUCCAUCCGCAUGGACAAUCCCUUUUACCCACGG"
         "UGGCUGGAGAAGGAAGCAAAGGACCUUCUGGUGAAGCUCUUCGUGCGAGAACCUGAGAAG"
         "AGGCUGGGCGUGAGGGGAGACAUCCGCCAGCACCCUUUGUUUCGGGAGAUCAACUGGGAG"
         "GAACUUGAACGGAAGGAGAUUGACCCACCGUUCCGGCCGAAAGUGAAAUCACCAUUUGAC"
         "UGCAGCAAUUUCGACAAAGAAUUCUUAAACGAGAAGCCCCGGCUGUCAUUUGCCGACAGA"
         "GCACUGAUCAACAGCAUGGACCAGAAUAUGUUCAGGAACUUUUCCUUCAUGAACCCCGGG"
         "AUGGAGCGGCUGAUAUCCUGA")

AlaninetRNA = ("AUGGCAGCGUCAGUGGCAGCUGCAGCCCGGAGGCUGCGGCGGGCCAUUCGAAGGUCG"
               "CCCGCAUGGCGGGGCCUCAGCCAUCGGCCGCUCUCAUCGGAGCCCCCUGCAGCCAAGGCC"
               "UCGGCCGUGAGGGCCGCCUUUCUGAACUUCUUUCGGGACCGCCAUGGCCACCGGCUGGUG"
               "CCCUCCGCUUCCGUGCGGCCCCGCGGCGACCCCAGUUUGCUUUUUGUCAAUGCGGGCAUG"
               "AACCAGUUCAAGCCAAUCUUUCUGGGCACCGUGGAUCCACGAAGCGAGAUGGCAGGCUUC"
               "CGACGUGUGGCCAACAGCCAGAAAUGUGUGAGAGCUGGAGGACACCAUAACGACCUGGAA"
               "GAUGUGGGUCGAGACCUUUCCCAUCAUACCUUCUUUGAAAUGCUUGGCAAUUGGGCCUUU"
               "GGGGGUGAAUAUUUUAAGGAGGAGGCUUGUAACAUGGCCUGGGAACUGCUGACUCAGGUC"
               "UAUGGGAUCCCUGAGGAAAGGCUCUGGAUCUCCUACUUUGAUGGUGACCCCAAGGCAGGG"
               "CUGGACCCAGACCUGGAGACCAGGGACAUCUGGCUGAGCUUAGGGGUGCCUGCUAGCCGU"
               "GUGCUUUCCUUUGGACCACAAGAGAACUUCUGGGAGAUGGGGGAUACUGGCCCUUGUGGG"
               "CCCUGUACUGAGAUCCACUACGACCUUGCUGGUGGGGUGGGAGCCCCCCAGCUGGUAGAG"
               "CUUUGGAACCUGGUCUUCAUGCAACACAACAGAGAGGCAGAUGGAAGCCUGCAGCCCCUG"
               "CCCCAGCGGCAUGUGGACACAGGAAUGGGCCUGGAAAGGCUGGUGGCUGUGCUGCAAGGC"
               "AAACACUCCACCUAUGACACUGACCUCUUUUCCCCGCUGCUCAACGCCAUACAGCAGGGC"
               "UGCAGGGCACCCCCUUACUUGGGCCGAGUAGGGGUGGCAGACGAGGGGCGCACAGACACA"
               "GCGUACCGCGUGGUGGCUGACCACAUCCGCACACUCAGUGUCUGCAUCUCUGAUGGCGUC"
               "UUCCCUGGGAUGUCAGGUCCCCCGCUGGUUCUUCGUCGGAUCCUGCGUCGAGCUGUGCGU"
               "UUCUCCAUGGAGAUCUUAAAGGCACCACCUGGCUUCCUAGGCAGCCUGGUACCUGUAGUG"
               "GUGGAGACACUGGGAGAUGCUUAUCCAGAACUGCAAAGGAACUCAGCCCAGAUCGCCAAC"
               "CUGGUGUCAGAGGACGAGGCAGCCUUCCUGGCCUCCCUGGAGCGGGGUAGGCGGAUCAUU"
               "GAUCGGACUCUGAGGACCCUGGGGCCUUCAGAUAUGUUCCCUGCUGAAGUGGCCUGGUCC"
               "UUGUCACUGUGUGGAGACCUGGGACUCCCCUUGGACAUGGUAGAGCUGAUGCUGGAGGAG"
               "AAAGGGGUCCAGCUAGACUCCGCUGGACUGGAGCGGUUGGCCCAAGAGGAGGCCCAGCAC"
               "CGGGCACGGCAGGCUGAGCCAGUUCAGAAGCAGGGAUUGUGGCUUGAUGUCCAUGCGCUU"
               "GGGGAGCUGCAGCGCCAAGGAGUGCCCCCAACUGACGACAGCCCCAAGUACAACUACUCC"
               "CUGCGACCCAGCGGAAGUUAUGAGUUCGGCACCUGUGAGGCCCAGGUGUUGCAACUGUAU"
               "ACAGAGGACGGGACAGCAGUGGCCUCCGUGGGGAAAGGCCAGCGCUGUGGCCUCCUCUUG"
               "GACAGGACCAACUUCUACGCAGAACAGGGGGGCCAGGCUUCAGACCGUGGCUACCUGGUG"
               "CGGGCAGGGCAAGAGGACGUGCUGUUCCCAGUAGCCCGGGCCCAGGUCUGUGGAGGUUUC"
               "AUCCUGCAUGAGGCAGUAGCCCCUGAGUGCCUGCGGUUAGGGGACCAGGUGCAGCUGCAU"
               "GUGGAUGAGGCCUGGCGUCUAGGCUGCAUGGCGAAGCAUACGGCCACCCACCUGCUGAAC"
               "UGGGCACUGAGGCAGACCCUGGGCCCUGGCACAGAGCAGCAGGGCUCCCAUCUCAAUCCU"
               "GAGCAGCUGCGCUUGGAUGUGACCACCCAGACCCCAUUGACCCCAGAGCAGCUCCGGGCA"
               "GUGGAGAACACUGUGCAGGAGGCCGUGGGGCAGGAUGAGGCUGUGUACAUGGAGGAGGUG"
               "CCCCUGGCGCUCACUGCCCAGGUCCCUGGCCUGCGCUCUCUGGAUGAGGUUUACCCAGAC"
               "CCUGUGCGGGUGGUAUCAGUGGGGGUGCCCGUGGCCCAUGCAUUGGACCCAGCCUCCCAA"
               "GCCGCACUGCAGACCUCUGUGGAGCUAUGCUGUGGGACGCACCUGUUACGUACUGGGGCU"
               "GUAGGGGACCUGGUUAUCAUCGGGGACCGCCAGCUUUCCAAGGGCACUACCCGCCUGCUG"
               "GCCGUCACUGGGGAGCAGGCCCAGCAGGCCCGAGAGCUAGGCCAGAGCCUGGCCCAGGAA"
               "GUGAAAGCGGCCACUGAGCGGCUGAGUCUGGGGAGCCGGGAUGUGGCGGAGGCACUGAGG"
               "CUGUCCAAGGACAUAGGACGACUCAUUGAAGCUGUGGAAACUGCUGUGAUGCCCCAGUGG"
               "CAGCGGCGGGAGCUGCUGGCCACAGUGAAGAUGCUGCAGCGGCGUGCCAACACUGCCAUC"
               "CGUAAGCUGCAAAUGGGACAGGCUGCAAAAAAAACUCAGGAGCUGCUGGAGCGGCACUCG"
               "AAGGGGCCUCUGAUUGUGGACACAGUCUCUGCUGAGUCUCUCUCAGUGCUGGUGAAGGUG"
               "GUACGGCAGCUGUGUGAGCAGGCCCCCAGCACGUCUGUGCUCCUACUCAGCCCCCAGCCC"
               "AUGGGGAAGGUGCUGUGUGCCUGUCAGGUGGCCCAGGGUGCCAUGCCCACCUUCACAGCA"
               "GAGGCCUGGGCACUGGCAGUGUGCAGCCACAUGGGGGGCAAGGCGUGGGGCUCGCGAGUG"
               "GUGGCCCAAGGCACCGGAAGCACUACUGACCUGGAAGCUGCCCUCAGUAUAGCCCAAACC"
               "UAUGCCCUCAGCCAGCUCUGA")

Insulin = ("AUGGCCCUGUGGAUGCGCCUCCUGCCCCUGCUGGCGCUGCUGGCCCUCUGGGGACCUGAC"
           "CCAGCCGCAGCCUUUGUGAACCAACACCUGUGCGGCUCACACCUGGUGGAAGCUCUCUAC"
           "CUAGUGUGCGGGGAACGAGGCUUCUUCUACACACCCAAGACCCGCCGGGAGGCAGAGGAC"
           "CUGCAGGGCAGCCUGCAGCCCUUGGCCCUGGAGGGGUCCCUGCAGAAGCGUGGCAUUGUG"
           "GAACAAUGCUGUACCAGCAUCUGCUCCCUCUACCAGCUGGAGAACUACUGCAACUAG")

DNAPolymeraseV = ("CGCAUCAUCUACGGGGACACGGACUCCAUAUUUGUGCUGUGCCGCGGCCUCACGGCCGCC"
                 "GGGCUGACGGCCGUGGGCGACAAGAUGGCGAGCCACAUCUCGCGCGCGCUGUUUCUGCCC"
                 "CCCAUCAAACUCGAGUGCGAAAAGACGUUCACCAAGCUGCUGCUGAUCGCCAAGAAAAAG"
                 "UACAUCGGCGUCAU")

#Tuple which represents genetic code table. Used throughout program for population of dictionaries for proteins.
genetic_table1 = ((('GCU', 'GCC', 'GCA', 'GCG'), 'Alanine'),
               (('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'), 'Leucine'),
               (('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'), 'Arginine'),
               (('AAA', 'AAG'), 'Lysine'),
               (('AAU', 'AAC'), 'Asparagine'),
               (('AUG',), 'Methionine'),
               (('GAU', 'GAC'), 'Aspartic acid'),
               (('UUU', 'UUC'), 'Phenylalanine'),
               (('UGU', 'UGC'), 'Cysteine'),
               (('CCU', 'CCC', 'CCA', 'CCG'), 'Proline'),
               (('CAA', 'CAG'), 'Glutamine'),
               (('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'), 'Serine'),
               (('GAA', 'GAG'), 'Glutamic acid'),
               (('ACU', 'ACC', 'ACA', 'ACG'), 'Threonine'),
               (('GGU', 'GGC', 'GGA', 'GGG'), 'Glycine'),
               (('UGG',), 'Tryptophan'),
               (('CAU', 'CAC'), 'Histidine'),
               (('UAU', 'UAC'), 'Tyrosine'),
               (('AUU', 'AUC', 'AUA'), 'Isoleucine'),
               (('GUU', 'GUC', 'GUA', 'GUG'), 'Valine'),
               (('UAA', 'UGA', 'UAG'), 'STOP'))


aminoacids = ('Alanine', 'Leucine', 'Arginine', 'Lysine', 'Asparagine', 'Methionine',
              'Aspartic acid', 'Phenylalanine', 'Cysteine', 'Proline','Glutamine', 'Serine',
              'Glutamic acid', 'Threonine', 'Glycine', 'Tryptophan', 'Histidine', 'Tyrosine',
              'Isoleucine', 'Valine', 'STOP') #seperate tuple used to call for printing amino acid names to output

protein_table1 = ((('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Alanine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Leucine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Arginine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Lysine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Asparagine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Methionine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Aspartic acid'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Phenylalanine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Cysteine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Proline'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Glutamine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Serine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Glutamic acid'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Threonine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Glycine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Tryptophan'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Histidine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Tyrosine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Isoleucine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'Valine'),
               (('cGMP', 'PKCTH', 'AlaninetRNA', 'Insuline','DNAPolymerase'), 'STOP')) #Tuple which represents our protein samples. 
                        # Used throughout program for population of dictionaries for proteins.

frequencyTable = {'Alanine': 0.0625,'Leucine': 0.09375,'Arginine': 0.09375,'Lysine': 0.03125,'Asparagine': 0.03125,
                  'Methionine': 0.015625,'Aspartic acid': 0.03125,'Phenylalanine': 0.03125,
                  'Cysteine': 0.03125,'Proline': 0.0625,'Glutamine': 0.03125,'Serine': 0.09375,'Glutamic acid': 0.03125,
                  'Threonine': 0.0625,'Glycine': 0.0625,'Tryptophan': 0.015625,'Histidine': 0.03125,'Tyrosine': 0.03125,
                  'Isoleucine': 0.046875,'Valine': 0.0625,'STOP': 0.046875}#Dictionary used to hold expected frequencies of amino acids in proteins. 
                        # Values gotten from dividing the number of times an amino acid is encoded with a base by size of table
                        #Or n/64 for short


def sequenceDecoder(sequence, sequence2, sequence3, sequence4, sequence5):

    cGMP_dictionary = {}#creates empty dictionary which will hold the total number of times a base was found in a particular sequence
                  #the dictionaries will used the amino acids as keys and the values will be the number of times it was found
    PKCTH_dictionary = {}
    AlaninetRNA_dictionary = {}
    Insulin_dictionary = {}
    DNAPolymeraseV_dictionary = {}
    protein_dictionary = {} #creates empty dictionary which will hold the frequency of amino acids for all proteins. Amino acids acting as keys, while the proteins with the frequency acting as values
                      #This is the most important structure as it will hold all our final calculations for use in the ttest  
    for a in range(len(genetic_table1)):
        cGMP_dictionary[genetic_table1[a][1]] = {x: 0 for x in genetic_table1[a][0]} #Starts populating our dictionaries with locations. Example, Alanine (GCT, GCC, GCA, GCG) : "total number of times found"
        PKCTH_dictionary[genetic_table1[a][1]] = {x: 0 for x in genetic_table1[a][0]}
        AlaninetRNA_dictionary[genetic_table1[a][1]] = {x: 0 for x in genetic_table1[a][0]}
        Insulin_dictionary[genetic_table1[a][1]] = {x: 0 for x in genetic_table1[a][0]}
        DNAPolymeraseV_dictionary[genetic_table1[a][1]] = {x: 0 for x in genetic_table1[a][0]}
        protein_dictionary[protein_table1[a][1]] = {x: 0 for x in protein_table1[a][0]} #Starts populating our dictionary with locations. Example, Alanine ("cGMP": Frequency, "PKCTH": Frequency, "AlaninetRNA": Frequency, "Insulin": Frequency, "DNAPolymeraseV": Frequency)

    def FindandAddInTab(trip):  # takes our current codon and then searches our sequence to add to the corresponding section of our dictionary
        #   Method to find and add for cGMP
        for cod in range(len(genetic_table1)):
            if trip in genetic_table1[cod][0]:#checks if codon was found in particular row of the genetic table and if found
                cGMP_dictionary[genetic_table1[cod][1]][trip] += 1#Adds to the total number of times it was found during the sequence to it's respective codon and total times as an amino acid
                return
    def FindandAddInTab2(trip):  # takes our current codon and then searches our sequence to add to the corresponding section of our dictionary
        #   Method to find and add for PKCTH
        for cod in range(len(genetic_table1)):
            if trip in genetic_table1[cod][0]:#checks if codon was found in particular row of the genetic table and if found
                PKCTH_dictionary[genetic_table1[cod][1]][trip] += 1#Adds to the total number of times it was found during the sequence to it's respective codon and total times as an amino acid
                return
    def FindandAddInTab3(trip):  # takes our current codon and then searches our sequence to add to the corresponding section of our dictionary
        #   Method to find and add for AlaninetRNA
        for cod in range(len(genetic_table1)):
            if trip in genetic_table1[cod][0]:#checks if codon was found in particular row of the genetic table and if found
                AlaninetRNA_dictionary[genetic_table1[cod][1]][trip] += 1#Adds to the total number of times it was found during the sequence to it's respective codon and total times as an amino acid
                return
    def FindandAddInTab4(trip):  # takes our current codon and then searches our sequence to add to the corresponding section of our dictionary
        #   Method to find and add for Insulin
        for cod in range(len(genetic_table1)):
            if trip in genetic_table1[cod][0]:#checks if codon was found in particular row of the genetic table and if found
                Insulin_dictionary[genetic_table1[cod][1]][trip] += 1#Adds to the total number of times it was found during the sequence to it's respective codon and total times as an amino acid
                return
    def FindandAddInTab5(trip):  # takes our current codon and then searches our sequence to add to the corresponding section of our dictionary
     #   Method to find and add for DNAPolymeraseV
        for cod in range(len(genetic_table1)):
            if trip in genetic_table1[cod][0]:#checks if codon was found in particular row of the genetic table and if found
                DNAPolymeraseV_dictionary[genetic_table1[cod][1]][trip] += 1#Adds to the total number of times it was found during the sequence to it's respective codon and total times as an amino acid
                return
            
    tim = 0 #Variable used to go from letter to letter until reaching 3 to form our codon
    tem = "" #Variable used to hold our three bases as a codon
    for a in sequence: #loop used to go from base to base in sequence and create codons
        #   Loop to find and add for
        tim += 1 #adds by 1 each time a base is found
        tem += a #adds current base to variable to hold our codon
        if tim >= 3: #once we've reached 3, resets the number of times we've found a base and our variable used to hold the codon.
            tim = 0
            FindandAddInTab(tem)#Calls method to find and add
            tem = "" #resets the variable for the current codon to be used again for another search

    for a in sequence2:  # loop used to go from base to base in sequence and create triplets
        tim += 1  # adds by 1 each time a base is found
        tem += a  # adds current base to variable to hold our codon
        if tim >= 3:  # once we've reached 3, resets the number of times we've found a base and our variable used to hold the codon.
            tim = 0
            FindandAddInTab2(tem)  # Calls method to find and add
            tem = ""  # resets the variable for the current codon to be used again for another search
           
    for a in sequence3:  # loop used to go from base to base in sequence and create triplets
        tim += 1  # adds by 1 each time a base is found
        tem += a  # adds current base to variable to hold our codon
        if tim >= 3:  # once we've reached 3, resets the number of times we've found a base and our variable used to hold the codon.
            tim = 0
            FindandAddInTab3(tem)  # Calls method to find and add
            tem = ""  # resets the variable for the current codon to be used again for another search

    for a in sequence4:  # loop used to go from base to base in sequence and create triplets
        tim += 1  # adds by 1 each time a base is found
        tem += a  # adds current base to variable to hold our codon
        if tim >= 3:  # once we've reached 3, resets the number of times we've found a base and our variable used to hold the codon.
            tim = 0
            FindandAddInTab4(tem)  # Calls method to find and add
            tem = ""  # resets the variable for the current codon to be used again for another search

    for a in sequence5:  # loop used to go from base to base in sequence and create triplets
        tim += 1  # adds by 1 each time a base is found
        tem += a  # adds current base to variable to hold our codon
        if tim >= 3:  # once we've reached 3, resets the number of times we've found a base and our variable used to hold the codon.
            tim = 0
            FindandAddInTab5(tem)  # Calls method to find and add
            tem = ""  # resets the variable for the current codon to be used again for another search

    #for a,b in cGMP_dictionary.items(): #method used to print out the total number of times codons were found and the frequency of amino acid for a sequence, output in original program
     #  print(a,":",b)#Prints out the amino acid (a) and the corresponding values for the respective codon (b).
     #   print(a, ":", sum(b.values()), sum(b.values()) / ((len(sequence1))/3))#Prints totals number of times amino acid was found and calculates frequency of all amino acids

    for a,b in cGMP_dictionary.items(): #populates our protein dictionary with the relative frequency of amino acids for the respective sequences
        protein_dictionary[a]["cGMP"] = sum(cGMP_dictionary[a].values())/((len(sequence))/3)
    for a,b in PKCTH_dictionary.items():
        protein_dictionary[a]["PKCTH"] = sum(PKCTH_dictionary[a].values())/((len(sequence2))/3)
    for a,b in AlaninetRNA_dictionary.items():
        protein_dictionary[a]["AlaninetRNA"] = sum(AlaninetRNA_dictionary[a].values())/((len(sequence3))/3)
    for a,b in Insulin_dictionary.items():
        protein_dictionary[a]["Insuline"] = sum(Insulin_dictionary[a].values())/((len(sequence4))/3)
    for a,b in DNAPolymeraseV_dictionary.items():
        protein_dictionary[a]["DNAPolymerase"] = sum(DNAPolymeraseV_dictionary[a].values())/((len(sequence5))/3)
    c = 0 #variable used to call for amino acid title during printing loop of results

    for a,b in protein_dictionary.items(): #Loop where ttest and output of results take place
        acquiredfrequency = (sum(b.values()))/5 #Relative frequency of amino acid for sample
        d = list(b.values()) #List of relative frequency of all amino acids in a row. Starts with Alinine and goes on until STOP
        array = np.array(d) #Takes the list above and converts it into an array for use in the one sample ttest
        difference = acquiredfrequency - frequencyTable[a] #Subtraction which helps us see first hand the difference in both frequencies
        print(" ")
        print(aminoacids[c],"relative frequency from 5 protein samples:", round(acquiredfrequency, 3), "Expected Frequency:",
              round(frequencyTable[a],3)) #Prints out frequencies rounded to third decimal place
        print("Difference between frequencies:", round(difference, 3)) #prints the single glance difference rounded to third decimal place
        print(" ")#makes a little space, looks nice
        print(scipy.stats.ttest_1samp(array, frequencyTable[a]))#One sample ttest which takes the array consisting of the current amino acid.
                                                                  # in the loop and it's relative frequency across proteins as our sample mean.
                                                                    # The population mean will be the expected frequency for the current amino acid.
                                                                # For every instance of the loop it will output the nonrounded (not possible to round with module)
                                                                  #t statistic and p value for each amino acid until reaching the end of the dictionary thus concluding the execution of our program.
        print("-------------------------------------------------------------------------------------")
        c += 1#Increments variable used for calling amino acids name in printing of frequencies


sequenceDecoder(cGMP, PKCTH, AlaninetRNA, Insulin, DNAPolymeraseV)#Begins program by calling to look over provided sequences.

