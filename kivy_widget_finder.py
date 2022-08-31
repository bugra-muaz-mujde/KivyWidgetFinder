

class KivyWidgetFinder:
    def __init__(self, instance):
        self.instance = instance
        self.set_instance_to_main_widget()
        self.widget_list = {}

    def set_instance_to_main_widget(self):
        while True:
            if self.instance.parent:
                self.instance = self.instance.parent
                if type(self.instance).__name__ == "WindowSDL":
                    break
            else:
                self.instance = None

    def explore_widget_tree(self, children):
        children_list = children
        for child in children_list:
            self.append_widget_to_list(child)
            if child.children:
                self.explore_widget_tree(child.children)

    def append_widget_to_list(self, instance):
        self.widget_list[instance] = str(type(instance).__name__)


"""
    def explore_widget_tree(self):
        count = 0
        while True:
            for child in self.instance.children:
                if child.children:
                    count = child.children
                else:
                    count = 0
                self.widget_list[type(child).__name__] = {child: count}
"""
