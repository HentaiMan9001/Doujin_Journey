import ui

__all__ = ['Data_Source','Tableview_Settings']

class Data_Source (object):
	def __init__(self, title = str(), items = None, sets = None):
		self.sets = sets
		self.items = items
		self.title = title
		
	def get_title(self, section):
		title = list(self.sets[section].keys())[0]
		return title

	def tableview_number_of_sections(self, tableview):
		if self.sets != None:
			return len(self.sets)
		else:
			return 1
			
	def delete_item(self, section, row):
		title = self.get_title(section)
		item = self.get_item(section, row)
		self.sets[section][title].remove(item)
		
	def get_item(self, section, row):
		if self.sets is not None:
			title = self.get_title(section)
			item = self.sets[section][title][row]
			return item
		else:
			return self.items[row]
		
	def tableview_number_of_rows(self, tableview, section):
		
		# Return the number of rows in the section
		if self.sets is not None:
			section_in_question = self.sets[section]
			title = self.get_title(section)
			items = section_in_question[title]
			return len(items)
		else:
			return len(self.items)
			
	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		cell = ui.TableViewCell()
		if self.sets == None:
				item = self.items[row]
		else:
			title = self.get_title(section)
			items = self.sets[section][title]
			item = items[row]
		if type(item) is str:
			cell.text_label.text = item
		else:
			cell.add_subview(item)
		return cell

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		if self.sets == None:
			return self.title
		else:
			title = self.get_title(section)
			return title
			
	def tableview_can_delete(self, tableview, section, row):
		# Return True if the user should be able to delete the given row.
		return True
	
	def tableview_can_move(self, tableview, section, row):
		# Return True if a reordering control should be shown for the given row (in editing mode).
		return True
		
	def tableview_delete(self, tableview, section, row):
		# Called when the user confirms deletion of the given row
		#print(section, row)
		if self.sets == None:
			item = self.get_item(section, row)
			self.items.remove(item)
		else:
			self.delete_item(section, row)
		tableview.delete_rows([row])
		
	def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
		# Called when the user moves a row with the reordering control (in editing mode).
		pass

class Tableview_Settings (object):
	def __init__(self, Views):
		self.views = Views
	def tableview_did_select(self, tableview, section, row):
		self.views[row].action()
	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass
	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'
