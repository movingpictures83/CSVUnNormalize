
import sys
import numpy

class CSVUnNormalizePlugin:

    def input(self, filename):
        tempstuff = open(filename, 'r')
        self.myfile = tempstuff.readline().strip()
        self.mycountfile = tempstuff.readline().strip()

    def run(self):
        countfilestuff = open(self.mycountfile, 'r')
        counts = dict()
        for line in countfilestuff:
            contents = line.split('\t')
            counts['"' + contents[0] + '"'] = int(float(contents[1].strip()))

        filestuff = open(self.myfile, 'r')
        self.firstline = filestuff.readline()
        lines = []
        for line in filestuff:
            lines.append(line)

        self.m = len(lines)
        self.samples = []
        self.bacteria = self.firstline.split(',')
        if self.bacteria.count('""') != 0:
            self.bacteria.remove('""')
        self.n = len(self.bacteria)
        self.ADJ = numpy.zeros([self.m, self.n])
        i = 0
        for i in range(self.m):
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
                value = float(contents[j + 1])
                self.ADJ[i][j] = int(round(value * counts[contents[0]]))

            i += 1

    def output(self, filename):
        filestuff2 = open(filename, 'w')
        filestuff2.write(self.firstline)
        for i in range(self.m):
            filestuff2.write(self.samples[i] + ',')
            for j in range(self.n):
                filestuff2.write(str(int(self.ADJ[i][j])))
                if j < self.n - 1:
                    filestuff2.write(',')
                else:
                    filestuff2.write('\n')

