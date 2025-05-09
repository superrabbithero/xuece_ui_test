from urllib.parse import urlencode
from typing import Optional

class HomeworkTopicPage:
    def __init__(self, page):
        self.page = page
        self.baseUrl = "https://xuece-stagingtest1.unisolution.cn/home/homework/homework/topic/"
        self.default_params = {
            'gradeDcode': '',
            'homeworkName': '',
            'isManager': 'false'
        }
        self.create_topic_btn = self.page.get_by_role("button",name = "新增专题")


    def navigate(self, topic_id:int, **params):
        url = f"{self.base_url}{topic_id}"
        query_string = urlencode({
            k: v for k, v in query_params.items() 
            if v  # 过滤空值
        })
        self.page.goto(f"{url}?{query_string}" if query_string else url)

    def search_by_homework_name(self, name):
        self.page.wait_for_timeout(500)
        self.filter_input_homework_name.fill(name)
        self.page.wait_for_timeout(500)
        self.search_btn.click()
        self.table.refresh_table()

    
    # class HomeworkTable:
    #     def __init__(self, page):
    #         self.page = page
    #         self._table = page.get_by_role("table")  # 私有属性，以下划线开头
    #         # self._rows = self._table.locator("tbody tr")
    #         self._headers = self._table.locator("thead th")

    #     @property  # 使用属性动态获取
    #     def rows(self):
    #         return self._table.locator("tbody tr")
        
    #     def refresh_table(self):
    #         self._table = self.page.get_by_role("table")
        
    #     def to_menu(self, index):
    #         self.rows.nth(index).get_by_text("目录").click()
    #         self.page.wait_for_url("**/home/homework/homework/topic/**")
            return self.page

    class TopicFormDrawer:
    """专题表单抽屉组件"""
        def __init__(self, page):
            self.page = page
            self.form = page.locator(".ant-drawer-content-wrapper")  # 根据实际DOM调整选择器
            self.name_input = page.get_by_label("专题名称")
            self.topic_type = page.get_by_label("专题类型")
            self.course_select = page.get_by_role("combobox", name="科目")
            self.submit_btn = page.get_by_role("button", name="保存")
            self.topic_access = page.get_by_label("专题公开范围")
            self.video_enable = page.get_by_label("视频")
            self.video_type = page.get_by_label("视频类型")
            self.study_type = page.get_by_label("学习模式")
            self.video_access = page.get_by_label("视频公开范围")
            self.qa_enable = page.get_by_label("答疑")
            self.add_qa_teacher_btn = page.get_by_label("答疑教师").get_by_role("button","添加")
            self.judge_enable = page.get_by_label("学生评价")
            self.pre_access = page.get_by_label("课前公开范围")
            self.post_access = page.get_by_label("课前公开范围")
            self.form_data = {}

        # -------------------- 时间相关字段 --------------------
        @property
        def open_time_start(self) -> Locator:
            """专题开放开始时间"""
            return self._get_time_input("专题开放时间", "开始时间")
        
        @property
        def open_time_end(self) -> Locator:
            """专题开放结束时间"""
            return self._get_time_input("专题开放时间", "结束时间")
        
        @property
        def video_time_start(self) -> Locator:
            """视频播放开始时间"""
            return self._get_time_input("视频播放时间", "开始时间")
        
        @property
        def video_time_end(self) -> Locator:
            """视频播放结束时间"""
            return self._get_time_input("视频播放时间", "结束时间")

        @property
        def qa_time_start(self) -> Locator:
            """视频播放开始时间"""
            return self._get_time_input("答疑时段", "开始时间")
        
        @property
        def qa_time_end(self) -> Locator:
            """视频播放结束时间"""
            return self._get_time_input("答疑时段", "结束时间")
        
        def _get_time_input(self, section: str, time_type: str) -> Locator:
            """通用时间选择器定位方法"""
            return (self.page.get_by_text(section, exact=True)
                    .locator("..")  # 定位到父级form-item
                    .get_by_placeholder(time_type))

        def fill(self, name: str, grade: str = "S02"):
            """填写表单"""
            self.name_input.fill(name)
            self.grade_select.select_option(grade)
        
        def submit(self):
            """提交表单"""
            self.submit_btn.click()
            self.form.wait_for(state="hidden")  # 等待抽屉关闭