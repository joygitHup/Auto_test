import configparser

class Myconfig(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionsxfrom(self, optionstr):
        return  optionstr
def inihelper(sections,option):
    cfg=Myconfig()
    cfg.read('E:\DevWorkSpace\pythonWorkSpace\PrcticeProject\config\Elements.ini')
    cfg.sections()
    value=cfg.get(sections,option)
    return  value
def ini_section(sections):
    cfg = Myconfig()
    cfg.read('E:\DevWorkSpace\pythonWorkSpace\PrcticeProject\config\Elements.ini')
    cfg.sections()
    value=cfg.items(sections)
    value=dict(value)
    return value