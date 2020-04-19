import yaml


def get_yml_data_with_filename_key(file_name , key):
    with open("./data/" + file_name + ".yml", 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[key]
        case_data_list = list()

        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list