class SearchStringUtility:
    base_url = "https://www.bestbuy.com/site/searchpage.jsp?"
    char_set = "&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"

    def prepare_search_url(self):
        search_keyword = {
            'cstv' : 'curved smart tv',
            'stv' : 'smart tv'
        }
        web_url = {}
        for each_search_term in search_keyword:
            search_string = self.prepare_search_string(search_keyword[each_search_term])
            web_url[each_search_term] = self.base_url + search_string + self.char_set

        return web_url

    def prepare_search_string(self, search_term):

        searh_curve = search_term.split(" ")
        search_list = []
        search_list.append("st=")
        for each_word in searh_curve:
            search_list.append(each_word)
            search_list.append("+")

        search_list.pop()
        return "".join(search_list)

sc = SearchStringUtility()
sc.prepare_search_url()