def fill_field_by_name(self, name, data):
    wd = self.app.wd
    wd.find_element("name", name).click()
    wd.find_element("name", name).clear()
    wd.find_element("name", name).send_keys(data)
