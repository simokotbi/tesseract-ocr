import re
#text="VG treaty. as\nbaat ID Number / 4, 5) a)\n4 F 784-1987-5702743-2\n- ; Name: Jude Savio Dcoutho\nDate of Birth: 20/07/1987\nNationality: India\n4 issuing Date /))<Y! mG\n"
text = "SS PMICTIL PICTILILY Wai U Wasi ——— “=>\n‘ ID Number / 44 s¢l! ay\n784-1987 -5702743-2\nSIS gab pew sige aw’!\nq\n’!@“Name: Jude Savio Dcoutho id\n"
# SS PMICTIL PICTILILY Wai U Wasi ——— “=>\n‘ ID Number / 44 s¢l! ay\n784-1987 -5702743-2\nSIS gab pew sige aw’!\nq\nName: Jude Savio Dcoutho id\n']
def text_clean_up(text):
    data=[]
    id_regex = r"(\d{3}(?:\s)?-\d{4}(?:\s)?-\d{7}(?:\s)?-\d{1}(?:\s)?)"
    name_regex = r"(?:\n|[\s;]+)[^A-Za-z]*Name: (.+?)$"
    #  |[,;]|[-_s¢l!@“=>‘]
    id_matches = re.findall(id_regex, text, re.MULTILINE)
    name_matches = re.findall(name_regex, text, re.MULTILINE)
    for match in id_matches:
        id_number = match
        # print("ID Number:", id_number)

    for match in name_matches:
        # name = re.sub(r"\s+\S+$", "", match)
        name = match
        # print("Name:", name)

    data.append({'name':name.replace('Name: ', '').replace('\n', ''),'id':id_number.replace('\n', '')})
    return data

