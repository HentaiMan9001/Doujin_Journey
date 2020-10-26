from app_ui.main_view import Main_View
Main_View = Main_View()

from api.api_controller import Client_Controller
client = Client_Controller()


def run():
	Main_View.present('fullscreen',hide_title_bar = True)
