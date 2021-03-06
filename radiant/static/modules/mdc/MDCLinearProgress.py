"""
Brython MDCComponent: MDCLinearProgress
=======================================


"""


from .core import MDCTemplate
#from .MDCButton import MDCButton,  MDCIconToggle

########################################################################


class MDCLinearProgress(MDCTemplate):
    """"""

    NAME = 'linearProgress', 'MDCLinearProgress'

    CSS_classes = {

        # '_16_9': 'mdc-card__media--16-9',
        # 'square': 'mdc-card__media--square',
    }

    MDC_optionals = {

        'indeterminate': 'mdc-linear-progress--indeterminate',
        'reversed': 'mdc-linear-progress--reversed',

        # 'outlined': 'mdc-card--outlined',
        # 'full_bleed': 'mdc-card__actions--full-bleed',
        # 'icon': '<i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>',
        # 'disabled': 'disabled',

    }

    # ----------------------------------------------------------------------
    def __new__(self, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""

        code = """
            <div role="progressbar" class="mdc-linear-progress  {indeterminate} {reversed}" aria-valuemin="0" aria-valuemax="1" aria-valuenow="0">
              <div class="mdc-linear-progress__buffer">
                <div class="mdc-linear-progress__buffer-bar"></div>
                <div class="mdc-linear-progress__buffer-dots"></div>
              </div>
              <div class="mdc-linear-progress__bar mdc-linear-progress__primary-bar">
                <span class="mdc-linear-progress__bar-inner"></span>
              </div>
              <div class="mdc-linear-progress__bar mdc-linear-progress__secondary-bar">
                <span class="mdc-linear-progress__bar-inner"></span>
              </div>
            </div>
        """

        return cls.render_html(code, context)

    # ----------------------------------------------------------------------

    @classmethod
    def set_progress(cls, element, val, buffer=None):
        """"""
        cls.mdc.progress = val
        if buffer is None:
            buffer = 1
        cls.mdc.buffer = buffer

    # ----------------------------------------------------------------------

    @classmethod
    def set_reverse(cls, element, val):
        """"""
        cls.mdc.reverse = val

    # ----------------------------------------------------------------------

    @classmethod
    def set_determinate(cls, element, val):
        """"""
        cls.mdc.determinate = val

    # ----------------------------------------------------------------------
    # @classmethod
    # def get(self, name):
        # """"""
        # if name is 'progress':
            # return self.element.progress

        # elif name is 'action_buttons':
            # return self.element.select('.mdc-card__action-buttons')[0]

        # elif name is 'action_icons':
            # return self.element.select('.mdc-card__action-icons')[0]

            # ----------------------------------------------------------------------
            # @classmethod
            # def progress(cls, mdc, *args):
                # """"""
                # mdc.progress = *args

    # ----------------------------------------------------------------------
    # @classmethod
    # def title(self, mdc, text):
        # """"""
        #self['title'].text = text


