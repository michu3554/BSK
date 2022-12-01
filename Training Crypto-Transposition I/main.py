text = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wi msdeedrlhe.p"
text_odszyfrowany = ""
for i in range(0, len(text)-1, 2):
    text_odszyfrowany = text_odszyfrowany + text[i+1] + text[i]
print(text_odszyfrowany)

