for i in range(27):
    for i in range(1,50):
        try:
            r=requests.get("http://www.tamildiction.org/simple_sentences/?alphabet_sentences_order="+chr(ord(s)+i)+"&list="+str(j))
            soup = BeautifulSoup(r.text, "lxml")
            review_e=soup.select(".english")
            review_t=soup.select(".tmeaning")
            print(len(review_e))
            if len(review_e)==0:
                print(len(review_e))
                break
            for k in range(len(review_e)):
                e.append(review_e[k].text)
                t.append(review_t[k].text)
        except:
            print(len(e))
            print("Ended page for read")
            break
