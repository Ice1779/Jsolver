__author__="icelain17l"
__version__="0.1.3"

from collections import OrderedDict
import colorama
from progress import bar
import argparse,sys,subprocess
from itertools import permutations


def __banner__():
    print(colorama.Fore.CYAN)
    subprocess.call(["banner","Jsolver"])
    print(colorama.Style.RESET_ALL)


colorama.init()


if sys.platform=="linux":
    try:
        __banner__()

    except:
        try:
            subprocess.call("sudo apt-get install sysvbanner")
            __banner__()

        except:
            print("Even after a lot of effort, we still haven't been able to display our banner on your linux machine. Something is seriously wrong with it(or you probably use arch or fedora)")

elif sys.platform=="win32":
    print("Windows non-unix folk, sorry we can't display our banner on your computer.")
elif sys.platform=="darwin":
    print("Mac users, I could have probably ran a workaround on your system to display our banner, but I am to lazy to do so.")    



mainlist=[]
def r_through(st):
    ml=[]
    with open(r"corncob_lowercase.txt","r") as file:

        for i in file.readlines():
            ml.append(i.strip("\n"))
    if st in ml:
        mainlist.append(st)


def main(lst):
    counter=0
    varlist=[]
    var=""

    l=list(lst.lower())
    t2lst = list(permutations(l, len(l)))
    try:
        for i in t2lst:
            for j in i:
                var=var+j
            varlist.append(var)
            var=""

        barl=bar.Bar(colorama.Fore.CYAN+"Searching-- ",max=len(varlist))
        for string in varlist:
            r_through(string)


            barl.next()
        mainl=list(OrderedDict.fromkeys(mainlist))
        if len(mainl)>0:
            print(colorama.Fore.YELLOW,"\nAll results found:")
            for i in mainl:
                print(colorama.Fore.GREEN,i)
        else:
            print(colorama.Fore.YELLOW,"\nSorry, no results found.")
    except KeyboardInterrupt:
        print(colorama.Fore.RED,"\nYou stopped the search")




if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("word",help="The main input")
    args=parser.parse_args()
    main(args.word)
