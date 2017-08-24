import tornado.web

LIST_INFO = [
    {'username':'kevin','email':'kevin@126.com'},
]
for i in range(300):
    temp = {'username':'kevin'+str(i),'email':str(i) + '123@126.com'}
    LIST_INFO.append(temp)

class Pageination:
    def __init__(self,current_page,all_item):

        all_pager,c = divmod(all_item,5)
        if c > 0:
            all_pager += 1
        self.all_pager = all_pager

        try:
            current_page = int(current_page)
        except:
            current_page = 1

        if  current_page < 1 and current_page>self.all_pager:
            current_page = 1
        self.current_page = current_page

    @property
    def start(self):
        return (self.current_page-1)*5

    @property
    def end(self):
        return self.current_page*5

    def page_str(self,base_url):    #base_url, url设置
        list_page = []

        if self.all_pager <11:
            s = 1
            t = self.all_pager
        else:
            if self.current_page <= 6:
                s = 1
                t = 11
            else:
                if (self.current_page+5) > self.all_pager:
                    s = self.all_pager - 10
                    t = self.all_pager
                else:
                    s = self.current_page - 5
                    t = self.current_page + 5

        #首页
        first_page = '<a href="%s1">首页</a>' % (base_url)
        list_page.append(first_page)
        #上一页
        if self.current_page == 1:
            prev_page = '<a href="javascript:void(0);">上一页</a>'
        else:
            prev_page = '<a href="%s%s">上一页</a>' %(base_url,self.current_page-1)
        list_page.append(prev_page)

        for p in range(s, t+1):
            if p == self.current_page:
                temp = '<a class="active" href="%s%s">%s</a>' % (base_url,p, p)
            else:
                temp='<a href="%s%s">%s</a>' %(base_url,p,p)
            list_page.append(temp)
        # 下一页
        if self.current_page >= self.all_pager:
            next_page = '<a href="javascript:void(0);">下一页</a>'
        else:
            next_page = '<a href="%s%s">下一页</a>' % (base_url, self.current_page + 1)
        list_page.append(next_page)
            # 尾页
        first_page = '<a href="%s%s">尾页</a>' % (base_url,self.all_pager)
        list_page.append(first_page)

        #页面跳转
        jump = """<input type='text' /><a onclick="Jump('%s',this);">GO</a>""" % (base_url,)
        script = """<script>
            function Jump(baseUrl,ths){
                var val = ths.previousElementSibling.value;
                if(val.trim().length>0){
                    location.href = baseUrl + val;
                }
            }
            </script>"""
        list_page.append(jump)
        list_page.append(script)

        return "".join(list_page)

class IndexHandler(tornado.web.RequestHandler):

    def get(self, page):

        page_obj = Pageination(page,len(LIST_INFO))
        current_list = LIST_INFO[page_obj.start : page_obj.end]
        str_page = page_obj.page_str('/index/')
        self.render('home/index.html',list_info=current_list,current_page = page_obj.current_page,str_page=str_page)

    def post(self, page):
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {'username':user,'email':email}
        LIST_INFO.append(temp)
        self.redirect("/index/" + page)


#

#---------------封装前----------------

# class IndexHandler(tornado.web.RequestHandler):
#
#     def get(self, page):
        #page为当前页，每页显示5条数据
        #第一页：0-5：LIST_INFO[0:5]，第二页：5-10：LIST_INFO[5:10]
        #start:(page-1)*5, end=page*5

        #模块化需求： 当前页 -- 总页数
        # all_pager,c = divmod(len(LIST_INFO),5)
        # try:
        #     page = int(page)
        # except:
        #     page = 1
        # if page < 1:
        #     page = 1
        # start = (page-1)*5
        # end = page * 5
        # current_list = LIST_INFO[start:end]
        #
        # if c > 0:
        #     all_pager += 1
        # page_obj = Pageination(page,all_pager)
        # current_list = LIST_INFO[page_obj.start : page_obj.end]
        # str_page = page_obj.page_str()

        # list_page = []
        #
        # if all_pager <11:
        #     s = 1
        #     t = all_pager
        # else:
        #     if page <= 6:
        #         s = 1
        #         t = 11
        #     else:
        #         if (page+5) > all_pager:
        #             s = all_pager - 10
        #             t = all_pager
        #         else:
        #             s = page - 5
        #             t = page + 5
        #
        # for p in range(s, t+1):
        #     if p == page:
        #         temp = '<a class="active" href="/index/%s">%s</a>' % (p, p)
        #     else:
        #         temp='<a href="/index/%s">%s</a>' %(p,p)
        #     list_page.append(temp)
        # str_page = "".join(list_page)
        #产出： start，end, str_page

        # self.render('home/index.html',list_info=current_list,current_page = page_obj.current_page,str_page=str_page)
    #
    # def post(self, page):
    #     user = self.get_argument('username')
    #     email = self.get_argument('email')
    #     temp = {'username':user,'email':email}
    #     LIST_INFO.append(temp)
    #     self.redirect("/index/" + page)