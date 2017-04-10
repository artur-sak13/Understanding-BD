import sys
import numpy as np
from Bio import SeqIO

class Needleman_Wunsch(object):

    def __init__(self):
        self.fna1               = list(list(SeqIO.parse(sys.argv[1], "fasta"))[0].seq)
        self.fna2               = list(list(SeqIO.parse(sys.argv[2], "fasta"))[0].seq)
        
        self.gap_p              = int(sys.argv[4])
        self.read_sub_matrix(sys.argv[3])

    def read_sub_matrix(self,fname):
        self.seqs = []
        t_seq = []
        mtrx = []
        first = True
        with open(fname, "r") as f:
            for line in f.readlines():
                if first:
                    self.seqs.append(line.split())
                    first = False
                else:
                    t_seq.append(line.split()[0])
                    mtrx.append(line.split()[1:])
            self.seqs.append(t_seq)
        self.sim_mtx = np.asarray(mtrx)

    def get_score(self, i, j):
        i = self.seqs[0].index(self.fna1[i])
        j = self.seqs[1].index(self.fna2[j])
        return int(self.sim_mtx[i,j])

    def run(self):
        F_mtx = np.zeros((len(self.fna1),len(self.fna2)))
        for i in range(F_mtx.shape[0]):
            for j in range(F_mtx.shape[1]):
                if i == 0:
                    F_mtx[i,j] = self.gap_p * j
                elif j == 0:
                    F_mtx[i,j] = self.gap_p * i
                else:
                    F_mtx[i,j] = max(F_mtx[i-1,j-1]+self.get_score(i,j), F_mtx[i-1,j]+self.gap_p, F_mtx[i,j-1]+self.gap_p)
        self.align(F_mtx)

    def align(self, F):
        A = ""
        B = ""
        i = len(self.fna1) - 1
        j = len(self.fna2) - 1
        score = 0
        while(i > 0 or j > 0):
            if i > 0 and j > 0 and F[i,j] == F[i-1,j-1] + self.get_score(i,j):
                A = self.fna1[i] + A
                B = self.fna2[j] + B
                i -= 1
                j -= 1
                if self.fna1[i] == self.fna2[j]:
                    score += self.get_score(i,j)
            elif i > 0 and F[i,j] == F[i-1,j] + self.gap_p:
                A = self.fna1[i] + A
                B = "-" + B
                i -= 1
            else:
                A = "-" + A
                B = self.fna2[j] + B
                j -= 1

        print "The optimal alignment between the given sequences has score %d." %(score)
        print A + "\n"
        print B








if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("ERROR: %d argument(s) passed, but 4 were expected." %(len(sys.argv) - 1))
    elif sys.argv[1][-3:] != "fna" or sys.argv[2][-3:] != "fna" or sys.argv[3][-3:] != "txt":
        sys.exit("ERROR: Invalid file types passed to program.")
    else:
        try:
            int(sys.argv[4])
        except ValueError:
            raise

        alg = Needleman_Wunsch()
        alg.run()








    
