import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import plotly.express as px

df=pd.read_csv("StudentsPerformance.csv")
mathscore=df["math score"].tolist()
readingscore=df["reading score"].tolist()
writingscore=df["writing score"].tolist()

mathscoreMean=statistics.mean(mathscore)
mathscoreMedian=statistics.median(mathscore)
mathscoreMode=statistics.mode(mathscore)
mathscoreStdev=statistics.stdev(mathscore)

readingscoreMean=statistics.mean(readingscore)
readingscoreMedian=statistics.median(readingscore)
readingscoreMode=statistics.mode(readingscore)
readingscorestdev=statistics.stdev(readingscore)

writingscoreMean=statistics.mean(writingscore)
writingscoreMedian=statistics.median(writingscore)
writingscoreMode=statistics.mode(writingscore)
writingscorestdev=statistics.stdev(writingscore)

print("Mean Median Mode of Math Score is {},{},{}".format(mathscoreMean,mathscoreMedian,mathscoreMode))
print("Mean Median Mode of Reading Score is {},{},{}".format(readingscoreMean,readingscoreMedian,readingscoreMode))
print("Mean Median Mode of Writing Score is {},{},{}".format(writingscoreMean,writingscoreMedian,writingscoreMode))

firstSdStart,firstSdEnd=mathscoreMean-mathscoreStdev,mathscoreMean+mathscoreStdev
secondSdStart,secondSdEnd=mathscoreMean-(2*mathscoreStdev),mathscoreMean+(2*mathscoreStdev)
thirdSdStart,thirdSdEnd=mathscoreMean-(3*mathscoreStdev),mathscoreMean+(3*mathscoreStdev)

firstSdStart1,firstSdEnd1=readingscoreMean-readingscorestdev,readingscoreMean-readingscorestdev
secondSdStart1,secondSdEnd1=readingscoreMean-(2*readingscorestdev),readingscoreMean+(3*readingscorestdev)
thirdSdStart1,thirdSdEnd1=readingscoreMean-(3*readingscorestdev),readingscoreMean+(3*readingscorestdev)

firstSdStart1,firstSdEnd1=writingscoreMean-writingscorestdev,writingscoreMean-writingscorestdev
secondSdStart1,secondSdEnd1=writingscoreMean-(2*writingscorestdev),writingscoreMean+(3*writingscorestdev)
thirdSdStart1,thirdSdEnd1=writingscoreMean-(3*writingscorestdev),writingscoreMean+(3*writingscorestdev)

mathscorelistonestd=[result for result in mathscore if result>firstSdStart and result<firstSdEnd]
mathscoreliststtwostd=[result for result in mathscore if result>secondSdStart and result<secondSdEnd]
mathscoreliststthreestd=[result for result in mathscore if result>thirdSdStart and result<thirdSdEnd]

readingscoreliststonestd=[result for result in readingscore if result>firstSdStart1 and result<firstSdEnd1]
readingscoreliststtwostd=[result for result in readingscore if result>secondSdStart1 and result<secondSdEnd1]
readingscoreliststthreestd=[result for result in readingscore if result>thirdSdStart1 and result<thirdSdEnd1]

writingscoreliststonestd=[result for result in writingscore if result>firstSdStart1 and result<firstSdEnd1]
writingscoreliststtwostd=[result for result in writingscore if result>secondSdStart1 and result<secondSdEnd1]
writingscoreliststthreestd=[result for result in writingscore if result>thirdSdStart1 and result<thirdSdEnd1]

print("{}% of data for mathscore lies within 1 standard deviation".format(len(mathscorelistonestd)*100.0/len(mathscore)))
print("{}% of data for mathscore lies within 2 standard deviation".format(len(mathscoreliststtwostd)*100.0/len(mathscore)))
print("{}% of data for mathscore lies within 3 standard deviation".format(len(mathscoreliststthreestd)*100.0/len(mathscore)))

print("{}% of data for readingscore lies within 1 standard deviation".format(len(readingscoreliststonestd)*100.0/len(readingscore)))
print("{}% of data for readingscore lies within 2 standard deviation".format(len(readingscoreliststtwostd)*100.0/len(readingscore)))
print("{}% of data for readingscore lies within 3 standard deviation".format(len(readingscoreliststthreestd)*100.0/len(readingscore)))

print("{}% of data for writingscore lies within 1 standard deviation".format(len(writingscoreliststonestd)*100.0/len(writingscore)))
print("{}% of data for writingscore lies within 2 standard deviation".format(len(writingscoreliststtwostd)*100.0/len(writingscore)))
print("{}% of data for writingscore lies within 3 standard deviation".format(len(writingscoreliststthreestd)*100.0/len(writingscore)))

