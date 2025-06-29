name = input("Enter your name: ")

f_result = len(name)
print(f_result)

s_result = name.find("p")
print(s_result)
# if user input ma yaha vaneko kei parena vane -1 vanera output dekhauchha

t_result = name.rfind("a")
print(t_result)
# yesle pachhadi bata pareko number print garauchha

fo_result = name.find("a")
print(fo_result)
# yesle agadi bata pareko number print garauchha

fi_result = name.capitalize()
print(fi_result)
# yesle suruko alphabet lai matrae capital banauchha

si_result = name.upper()
print(si_result)
# yesle sabae alphabet lai capital banauchha

se_result = name.lower()
print(se_result)
# yesle sabae alphabet lai small banauchha

e_result = name.isdigit
print(e_result)
# yesle if e_result ma sabae number bala input chha vane yes navae no vanera print garauchha

te_result = name.isalpha()
print(te_result)
# yesle if e_result ma sabae alphabet bala input chha vane yes navae no vanera print garauchha

el_result = name.count("a")
print(el_result)



phone_no = input("Enter phone number: ")

result = phone_no.replace("-", "")
print(result)