class LoginPage:
	def __init__(self, page):
		self.page = page
		self.baseUrl = "https://xuece-stagingtest1.unisolution.cn/login"
		self.app_download_button = page.locator("css=profile")
		self.username_input = page.get_by_placeholder("请输入账号")
		self.password_input = page.get_by_placeholder("请输入密码")
		self.remember_account_checkbox = page.locator("css=ant-checkbox-input")
		self.forgot_button = page.locator("css=forgot")
		self.login_button = page.locator("[class='login-btn ant-btn ant-btn-block']")
		self.find_account_button = page.locator("css=find-account-row")
		self.login_type_switch_button = page.locator("css=login_type_switch")
		self.qrcode_canvas = page.locator("css=code")

	def navigate(self):
		self.page.goto(self.baseUrl)

	def login(self, username, password):
		self.username_input.fill(username)
		self.password_input.fill(password)
		self.login_button.click()

	def remember_account(self):
		self.remember_account_checkbox.check()

	def switch_login_type(self):
		self.login_type_switch_button.click()