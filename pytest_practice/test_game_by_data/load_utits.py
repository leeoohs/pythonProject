import yaml


class LoadUitls:
    # 如果此类中的数据，不需要被其他的方法使用，则可以利用累方法
    # 应用场景：工具类。
    @classmethod
    def load_yaml(self, yaml_path):
        # return data
        return yaml.safe_load(open(yaml_path))

    def load_excel(self):
        return


if __name__ == '__main__':
    # 不使用类方法的方式
    # load_uitls = LoadUitls()
    # load_uitls.load_yaml()
    # 使用累方法调用
    print(LoadUitls.load_yaml("volume_data.yaml"))