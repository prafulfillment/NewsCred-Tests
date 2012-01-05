from newscred import *
from prettytable import PrettyTable
from django.utils.encoding import smart_str

access_key = 'your_access_key'

def prettyPrintArticle(a):
    title = smart_str(a.title)
    title = title.replace('[', '(').replace(']', ')').replace('|', '-')
    source = smart_str(a.source_website)
    created_at = smart_str(a.created_at)
    print '|[' + title + '|' + a.link + ']|' + source + '|'  + created_at + '|'    

def prettyPrintArticles(articles_list, qt, is_topic, call, options):
    #foo = PrettyTable(["Title", "Source", "GUID", "Created", "Published", "Link"])
    #foo.set_field_align("Title", "l")
    #foo.set_field_align("Source", "l")
    #foo.set_field_align("Link", "l")

    r = [k + '=' + str(v) for k,v in options.items()]
    r1 = ', '.join(r)
    q_or_t = 'topic' if is_topic else 'query'
    print 'h4. NewsCred: call='+call+', '+ q_or_t +'='+qt+', '+r1 #', categories=business,technology, sort=relevance, pagesize=50, cluster_size=10'
    print '|| Title || Source || Date ||'
    for articles in articles_list: 
        if type(articles) == list:
            print '| *Cluster* | - | - |'
            for a in articles:
                prettyPrintArticle(a)
        else:
            prettyPrintArticle(articles)  
            #foo.add_row([a.title, a.source_website, a.guid, a.created_at, a.published_at, a.link])

    #foo.printt(); 

def NewsCred(qt, is_topic):
    try:
        # API call with default arguments
        # API call with custom arguments
        options = {}
        #options['offset'] = 0
        #options['pagesize'] = 50
        #options['from_date'] = '2011-11-01'
        #options['to_date'] = '2011-11-30'
        options['sort'] = 'relevance'
        #options['sources'] = ['1ce0362f2e764a95b0c7351c05a4eb19', '2c20eeebd3486973559db5b654d87771']
        #options['source_countries'] = ['us', 'uk', 'in', 'qa', 'ca']
        #options['categories'] = ['world', 'u-k', 'u-s', 'sports', 'business', 'technology'] # configurable by user
        options['categories'] = ['business', 'technology']
        options['cluster_size'] = 10 # configurable by user

        if(is_topic):
            topic = NewsCredTopic(access_key=access_key, guid=qt)
            stories_list = topic.get_related_stories(options=options)
            prettyPrintArticles(stories_list, qt, is_topic, 'stories', options)
        else:
            stories_list = NewsCredArticle.search_stories(access_key=access_key, query=qt, options=options)
            prettyPrintArticles(stories_list, qt, is_topic, 'stories', options)
            articles_list = NewsCredArticle.search(access_key=access_key, query=qt, options=options)
            prettyPrintArticles(articles_list, qt, is_topic, 'articles', options)
        print "\n"*2

    except NewsCredError, e:
        # Handle exception here
        pass


def NewsCredQuery(query):
    NewsCred(query, False)

def NewsCredTopicQuery(topic):
    NewsCred(topic, True)

def NewsCredQueryTopic(query):
    topic = NewsCredTopic.search(access_key=access_key, query=query)
    print [(t.guid, t.name) for t in topic]
    #NewsCredTopicQuery(topic[0].guid)
            
NewsCredTopicQuery('e433f506c07964fc0d15ba2d05e7be9d')  #facebook
#NewsCredTopicQuery('95373b5ae74e7c6d379c1155f81a1520')  #twitter 
#NewsCredTopicQuery('c2f34137dd2dbd7347c31f6dbb0eb9b7')  #groupon
#NewsCredTopicQuery('01ef2c22dfd3a37f4cabe8e168a66c24')  #zynga
#NewsCredTopicQuery('43a4f865f880e895e44faba37f8eafce')  #foursquare 
#NewsCredTopicQuery('5f3e10c7119b625c3dffa782519caa2c')  #dropbox
