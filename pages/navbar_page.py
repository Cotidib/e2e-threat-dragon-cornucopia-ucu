from pages.base_page import BasePage


class NavbarPage(BasePage):
	def __init__(self, page):
		super().__init__(page)
		# Selectores 
		self.language_toggle_btn = "//div[@class='locale-changer']//button[contains(@class,'dropdown-toggle')]"
		self.language_search_input = "//div[@class='locale-changer']//input[@type='text' and contains(@class,'form-control')]"
		self.dropdown_item_by_label = "//div[@class='dropdown-items-container']//a[contains(@class,'dropdown-item') and normalize-space(text())='{label}']"

	# Métodos
	def open_language_dropdown(self):
		# Abrir con un click simple y esperar que el dropdown esté visible
		toggle = self.page.locator(self.language_toggle_btn).first
		toggle.click()
		# Esperar que el contenedor del dropdown sea visible
		container = self.page.locator("//div[@class='dropdown-items-container']").first
		container.wait_for(state="visible")

	def select_language(self, language_name: str):
		# Asumir que el dropdown ya está abierto (abierto desde los steps)
		# Verificar que el contenedor del dropdown sea visible
		container = self.page.locator("//div[@class='dropdown-items-container']").first
		container.wait_for(state="visible")
		# Enfocar el input de búsqueda y escribir el idioma
		search = self.page.locator(self.language_search_input).first
		search.focus()
		try:
			search.fill("")
		except Exception:
			pass
		search.type(language_name, delay=10)
		# Click en el primer match por etiqueta visible
		xpath = self.dropdown_item_by_label.format(label=language_name)
		self.page.locator(xpath).first.click(force=True)

	def get_current_language_text(self) -> str:
		return self.page.text_content(self.language_toggle_btn).strip()

	def change_language_and_validate(self, target_language: str):
		self.select_language(target_language)
		# Después de la selección, el texto del toggle debe actualizarse
		self.page.wait_for_timeout(200)  # espera breve para que la UI se actualice
		current = self.get_current_language_text()
		assert current.lower() == target_language.lower(), (
			f"Language did not change. Expected '{target_language}', got '{current}'"
		)

