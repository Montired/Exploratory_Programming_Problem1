def string_k(k, str):
    string = []
    text = str.split(" ")
    text.sort()
    for x in text:  
        if len(x) > k:  
            string.append(x) 
    return string
    string.sort()       
k = 8
str ="We have developed speed, but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness"
print(string_k(k, str))
