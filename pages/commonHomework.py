class CommonHomeworkPage:
    def __init__(self, page):
        self.page = page
        self.baseUrl = "https://xuece-stagingtest1.unisolution.cn/home/homework/commonHomework"
        self.filter_input_homework_name = page.get_by_placeholder("输入作业名称")
        self.search_btn = page.get_by_role("button", name="搜索")
        self.table = self.HomeworkTable(page)

    def navigate(self):
        self.page.goto(self.baseUrl)

    def search_by_homework_name(self, name):
        self.page.wait_for_timeout(500)
        self.filter_input_homework_name.fill(name)
        self.page.wait_for_timeout(500)
        self.search_btn.click()
        self.table.refresh_table()

    
    class HomeworkTable:
        def __init__(self, page):
            self.page = page
            self._table = page.get_by_role("table")  # 私有属性，以下划线开头
            # self._rows = self._table.locator("tbody tr")
            self._headers = self._table.locator("thead th")

        @property  # 使用属性动态获取
        def rows(self):
            return self._table.locator("tbody tr")
        
        def refresh_table(self):
            self._table = self.page.get_by_role("table")
        
        def to_menu(self, index):
            self.rows.nth(index).get_by_text("目录").click()
            self.page.wait_for_url("**/home/homework/homework/topic/**")
            return self.page

