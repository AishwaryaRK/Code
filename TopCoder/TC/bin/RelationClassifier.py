class RelationClassifier:
    def isBijection(self, domain, range):
        # return "Not" if len(set([e for e in domain if domain.count(e) > 1])) > 0 or len(
        #     set([e for e in range if range.count(e) > 1])) > 0 else "Bijection"
        domainLen = len(domain)
        domainSetLen = len(set(domain))
        rangeLen = len(range)
        rangeSetLen = len(set(range))
        print domainLen,domainSetLen,rangeLen,rangeSetLen
        return "Bijection" if domainLen == domainSetLen and rangeLen == rangeSetLen else "Not"


print RelationClassifier().isBijection((1,1), (13, 15))
