import getopt
import sys
import random

def random_author_order(argv):

    seed = 666

    try:
        opts, args = getopt.getopt(argv,"hi:s:",["ifile=","seed="])
    except getopt.GetoptError:
        print 'random_author_order.py -i <inputfile> -s <seed>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'random_author_order.py -i <inputfile> -s <seed>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            author_file = arg
            sys.stderr.write('\nAuthor file is: %s'%(author_file))
        elif opt in ("-s", "--seed"):
            try:
                int(arg)
                seed = arg
                
            except ValueError:
                print '\nInvalid seed: "%s"\nSwitching seed to 666'%(arg)

    sys.stdout.write('\nSeed: %s'%(seed))           

    def unique(o, idfun=repr):
        """Reduce a list down to its unique elements."""
        seen = {}
        return [seen.setdefault(idfun(e),e) for e in o if idfun(e) not in seen]

    affils={}
    authors=[]

    ## load authors and affiliations
    for line in open(author_file,'r'):
        author,affiliation=line.strip('\n').split('\t')
        authors.append(author)

        ## multiple affiliations are separated by semicolons
        affiliation = [x.strip(' ') for x in affiliation.split(';')]
        
        affils[author]=affiliation

    ## set seed, shuffle authors list in place
    random.seed(seed)
    random.shuffle(authors)

    ## establish order of affiliations based on author order
    affil_order=[]

    for i in authors:
        for aff in affils[i]:
            affil_order.append(aff)

    ## reduce affiliation list down to unique entries
    affil_order=unique(affil_order)
    
    sys.stdout.write('\n\n')

    for i in authors:
        ## get indices of each person's affiliations
        affil_indices=','.join([str(affil_order.index(x)+1) for x in affils[i]])
        
        sys.stdout.write('%s\t%s\n'%(i,affil_indices))

    ## write out order of affiliations
    sys.stdout.write('\n%s'%(', \n'.join(['%s %s'%(i+1,x) for i,x in enumerate(affil_order)])))

    sys.stdout.write('\n\n')
    
if __name__ == "__main__":
    random_author_order(sys.argv[1:])
