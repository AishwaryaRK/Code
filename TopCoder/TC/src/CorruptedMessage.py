
import collections

class CorruptedMessage:
    def reconstructMessage(self, s, k):
        if k==0:
            return s;
        letterFreq = collections.Counter(s);
        for letter in letterFreq:
            if len(s)-letterFreq[letter]==k:
                return letter * len(s)
        for letter in range(ord('a'),ord('z')+1):
            if chr(letter) not in s:
                return chr(letter) * len(s)


print(CorruptedMessage().reconstructMessage("abc",3))