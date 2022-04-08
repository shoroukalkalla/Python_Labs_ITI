import json
#>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<#


class DB:
    def connect_with_data(self, data_path):
        self.data_path = data_path
#########################################################

    def connect_with_project(self, project_path):
        self.project_path = project_path
#########################################################

    def get_user_data(self):
        f = open(self.data_path, "r")
        data = json.load(f)
        f.close()
        return data
#########################################################

    def get_project_data(self):
        f = open(self.project_path, "r")
        project = json.load(f)
        f.close()
        return project
#########################################################

    def store_user_data(self, data):
        get_data = self.get_user_data()
        f = open(self.data_path, "w")
        get_data.append(data)
        json.dump(get_data, f)
        f.close()
#########################################################

    def project_store_data(self, data):
        f = open(self.project_path, "w")
        json.dump(data, f)
        f.close()
