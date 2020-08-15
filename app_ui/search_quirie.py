import ui
import dialogs
fields = list()

max_field = {
	'title':'max',
	'accessory_type':'disclosure_indicator',
}
fields.append(max_field)

min_field = {
	'title':'min',
	'accessory_type':'checkmark',
}
fields.append(min_field)
language_field = {
	'title':'Language',
	'accessory_type':'none'
}
fields.append(language_field)

#h = dialogs.form_dialog(title = 'test', sections = [('Pages',[max_field,min_field]),('Language',[language_field])])

source = ui.ListDataSource(items = fields)

#dialogs.list_dialog(title = 'test', items = fields)

table = ui.TableView()

table.data_source = source

table.present()


