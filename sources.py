from newscred import * 

from django.utils.encoding import smart_str, smart_unicode

def article_find(guid):
	a = NewsCredArticle(access_key='5e1b560feaa80a6d7d0d66a201b9cd6d', guid=guid)
	s = smart_str(a.title)
	print '|%s|%s|%s|' %(a.source,s, a.created_at)

article_find('f53b1c74afbf991d8eb5aa1f97a67475')
article_find('5543aafdbb1b03b744f4166c8d42ffe1')
article_find('9a154a059faf032b366d4b32a0fcab93')
article_find('6514759d39eaa5e89fee7b25c1d54828')
article_find('782acd9b1f6bad35819f8d3d5df6bc1f')
article_find('e80c2b33f1ca6182230508018c45522d')
article_find('c1abc0716c6b68f5700a7e2abd4d9200')
article_find('c4fff70d719d92cc4185cdf5576604a0')
article_find('650cf7ea3b2abbc058f5c653cfd5e9f7')
article_find('ebd2f8cea8769453805814f9d54ef06b')
article_find('f7fc2f0a517ef15895b14ee2731ce0a8')
article_find('9d3accd325043003f34f93a3f60ee7ca')
article_find('f38e1d454371fb0b52175d2224448c7d')
article_find('4e66920ce8856f9f4d30f643c65cd9db')
article_find('ae246e9a5fb77351f9532d08bc4a3908')
article_find('5224ead1d08530b7d81a69bed7e87c8a')
article_find('05dabdd6d11d32bcd0df6c253ee3acf9')
article_find('55715e76e29b32cc712a4b1b95251ed2')
article_find('c4775d1ef42dae99909f04eeb225def3')
article_find('3488609ef619fbaec3ec4ce42d11a214')


