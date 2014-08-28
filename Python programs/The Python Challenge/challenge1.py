# Python Challenge 1 --> cryptography, k-->m; o-> q; e-->g (Key:2)
import string

trantab = str.maketrans(string.ascii_letters[0:26], string.ascii_letters[2:26] + string.ascii_letters [0:2])

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print (text.translate(trantab));
print ("map".translate(trantab));


