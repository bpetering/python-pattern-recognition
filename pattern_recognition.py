def constant(diffs):
    val = diffs.pop()
    for d in diffs:
        if d != val:
            return False
    return val

def pat1(seq):      # consider two elements at a time
    diffs = []
    for i in xrange(1, len(seq)):
        diffs.append( seq[i] - seq[i-1] )       # implicit directionality - factor out
    return constant(diffs)

# representation of the pattern for pat1 was easy. how can we represent
# more complex patterns?

class Pattern(object):

    (PAT_INT_ADD, PAT_INT_MULT, PAT_INT_POW) = range(3)

    # TODO how does panda3d get constants?
    def __init__(self, pat_type, pat_vals, prev_data, over=2, *args, **kwargs):
        self.pat_type   = pat_type
        self.over       = over
        self.prev_data  = prev_data
        self.pat_vals    = pat_vals

    def next(self):
        if self.pat_type == Pattern.PAT_INT_ADD:
            tmp = self.prev_data[-1] + self.pat_vals[0]        # TODO how much prev_data to keep?
            self.prev_data.append(tmp)
            return tmp

class PatternSeq(object):

    def __init__(self, *args, **kwargs):
        self.pattern = None

    def have_pattern(self):
        return self.pattern is not None

    def infer(self, seq):
        v = pat1(seq)
        if v is not False:
            self.pattern = Pattern(pat_type=Pattern.PAT_INT_ADD, pat_vals=[v], prev_data=seq)      #   TODO generalize
        else:
            raise Exception("NYI")

    def extend(self, n):
        if self.have_pattern():
            x = []
            for i in xrange(n):
                x.append(self.pattern.next())
            return x
        else:
            raise Exception("ALSDKJLASKJD")

# def pat2(seq):      # consider three elements at a time
#     diffs = []
#     for i in xrange(1, len(seq)):
#         diffs.append( seq[i] - seq[i-1] )       # implicit directionality - factor out
#     val = constant(diffs)
#     if val is False:
#         print 'no pattern'
#     else:
#         print val

# TODO look at sympy interface, requests interface

# TODO detect pattern with certain number of anomalous values:
# e.g. 2,4,6,8,11

ps = PatternSeq()
ps.infer([2,4,6,8,10])
print "have pattern:", ps.have_pattern()
print "next 10 vals:", ps.extend(10)
