import subprocess

def runPerlCollars(outputDir, audioname, oracleRttmFile):
    myoutput = open(outputDir+"NISTEvaluation_2_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.25", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_2_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.20", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.15", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.10", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.05", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.00", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)

#    print("Running md-eval-v21.pl scripts complete")
    return 1

def runPerlCollarsUem(outputDir, audioname, oracleRttmFile):
    myoutput = open(outputDir+"NISTEvaluation_2_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.25", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_2_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.20", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.15", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.10", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.05", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.00", "-u", audioname+".uem", "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)

    print("Running md-eval-v21.pl scripts complete")
    return 1


def runPerlCollarsUem2(outputDir, audioname, oracleRttmFile, uemFile):
    myoutput = open(outputDir+"NISTEvaluation_2_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.25", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_2_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.20", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.15", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_1_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.10", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_5.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.05", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)
    myoutput = open(outputDir+"NISTEvaluation_0_0.txt", 'w')
    subprocess.run(["perl", "md-eval-v21.pl", "-m", "-afc", "-c 0.00", "-u", uemFile, "-r", oracleRttmFile, "-s", outputDir+audioname+".rttm"], stdout=myoutput)

    print("Running md-eval-v21.pl scripts complete")
    return 1



