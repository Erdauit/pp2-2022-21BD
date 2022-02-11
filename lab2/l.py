brackets = input()
while "()" in brackets or "[]" in brackets or "{}" in brackets:
    if "()" in brackets:
        brackets = brackets.replace("()", "")
    if "[]" in brackets:
        brackets = brackets.replace("[]", "")
    if "{}" in brackets:
        brackets = brackets.replace("{}", "")

if len(brackets) > 0:
    print ("No")
elif len(brackets) == 0:
    print ("Yes")