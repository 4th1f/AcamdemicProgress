def art_count(s): 

    article_count = 0 

    for i in s: 

        i = i.lower() 

        word_list = i.split(" ") 

        for j in word_list: 

            if j == "a" or j == "an" or j == "the": 

                article_count += 1 

    print("The number of articles:",article_count) 

h=input("Enter the text :")
h=list(h)

art_count(h) 
