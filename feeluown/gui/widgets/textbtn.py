from PyQt5.QtWidgets import QPushButton


class TextButton(QPushButton):
    def __init__(self, *args, height=None, **kwargs):
        """
        .. versionadded:: 3.9
            The *height* argument.
        """
        super().__init__(*args, **kwargs)

        if height:
            self.setFixedHeight(height)
