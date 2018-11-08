class DarkTheme(object):
    @staticmethod
    def get_style_sheet():
        return """
            /* QDarkStyleSheet --------------------------------------------------------
            
            This is the main style sheet, the palette has nine main colors.
            It is based on three selecting colors, three greyish (background) colors
            plus three whitish (foreground) colors. Each set of widgets of the same
            type have a header like this:
            
                ------------------
                GroupName --------
                ------------------
            
            And each widget is separated with a header like this:
            
                QWidgetName ------
            
            This makes more easy to find and change some css field. The basic
            configuration is described bellow.
            
                SELECTION ------------
            
                    sel_light  #179AE0 (selection/hover/active)
                    sel_normal #3375A3 (selected)
                    sel_dark   #18465D (selected disabled)
            
                FOREGROUND -----------
            
                    for_light  #EFF0F1 (texts/labels)
                    for_normal #A9A9A9 ()
                    for_dark   #4D545B (disabled texts)
            
                BACKGROUND -----------
            
                    bac_light  #4D545B (unpressed)
                    bac_normal #31363B (border, disabled, pressed)
                    bac_dark   #232629 (background)
            
            If a stranger configuration is required because of a bugfix or anything
            else, keep the comment on that line to nobodys changed it, including the
            issue number.
            --------------------------------------------------------------------------- */
            
            
            
            /* QWidget ---------------------------------------------------------------- */
            
            QWidget {
                background-color: #232629;
                border: 0px solid #31363B;
                padding: 0px;
                color: #EFF0F1;
                selection-background-color: #3375A3;
                selection-color: #EFF0F1;
            }
            
            QWidget:focus {
                border: 1px solid #179AE0;
            }
            
            QWidget:disabled {
                background-color: #232629;
                color: #4D545B;
                selection-background-color: #18465D;
                selection-color: #4D545B;
            }
            
            QWidget:item:selected {
                background-color: #3375A3;
            }
            
            QWidget:item:hover {
                background-color: #179AE0;
                color: #31363B;
            }
            
            /* QMainWindow ------------------------------------------------------------ */
            /* This adjusts the splitter in the dock widget, not qsplitter              */
            
            
            QMainWindow::separator {
                background-color: #31363B;
                border: 0 solid #232629;
                spacing: 0;
                padding: 1px;
                margin: 0;
            }
            
            QMainWindow::separator:hover {
                background-color: #4D545B;
                border: 0px solid #179AE0;
            }
            
            QMainWindow::separator:horizontal {
                width: 5px;
                image: url(:/qss_icons/rc/Vsepartoolbar.png);
            }
            
            QMainWindow::separator:vertical {
                height: 5px;
                image: url(:/qss_icons/rc/Hsepartoolbar.png);
            }
            
            
            /* QToolTip --------------------------------------------------------------- */
            
            QToolTip {
                background-color: #179AE0;
                border: 1px solid #232629;
                color: #232629;
                padding: 0;   /*remove padding, for fix combo box tooltip*/
                opacity: 230; /*reducing transparency to read better*/
            }
            
            /* QStatusBar ------------------------------------------------------------- */
            
            QStatusBar {
                border: 1px solid #31363B;
            }
            
            /* QCheckBox -------------------------------------------------------------- */
            
            QCheckBox {
                background-color: #232629;
                color: #EFF0F1;
                spacing: 4px;
                outline: none;
                padding-top: 4px;
                padding-bottom: 4px;
            }
            
            QCheckBox:focus {
                border: none;
            }
            
            QCheckBox QWidget:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            QCheckBox::indicator {
                margin-left: 4px;
                width: 16px;
                height: 16px;
            }
            
            QCheckBox::indicator:unchecked {
                image: url(:/qss_icons/rc/checkbox_unchecked.png);
            }
            
            QCheckBox::indicator:unchecked:hover,
            QCheckBox::indicator:unchecked:focus,
            QCheckBox::indicator:unchecked:pressed {
                border: none;
                image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);
            }
            
            QCheckBox::indicator:unchecked:disabled {
                image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
            }
            
            QCheckBox::indicator:checked {
                image: url(:/qss_icons/rc/checkbox_checked.png);
            }
            
            QCheckBox::indicator:checked:hover,
            QCheckBox::indicator:checked:focus,
            QCheckBox::indicator:checked:pressed {
                border: none;
                image: url(:/qss_icons/rc/checkbox_checked_focus.png);
            }
            
            QCheckBox::indicator:checked:disabled{
                image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
            }
            
            QCheckBox::indicator:indeterminate {
                image: url(:/qss_icons/rc/checkbox_indeterminate.png);
            }
            
            QCheckBox::indicator:indeterminate:disabled {
                image: url(:/qss_icons/rc/checkbox_indeterminate_disabled.png);
            }
            
            QCheckBox::indicator:indeterminate:focus,
            QCheckBox::indicator:indeterminate:hover,
            QCheckBox::indicator:indeterminate:pressed {
                image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);
            }
            
            /* QGroupBox -------------------------------------------------------------- */
            
            QGroupBox {
                font-weight: bold;
                border: 1px solid #31363B;
                border-radius: 4px;
                padding: 4px;
                margin-top: 16px;
            }
            
            
            
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 3px;
                padding-left: 3px;
                padding-right: 5px;
                padding-top: 8px;
                padding-bottom: 16px;
            }
            
            QGroupBox::indicator {
                margin-left: 4px;
                width: 16px;
                height: 16px;
            }
            
            QGroupBox::indicator {
                margin-left: 2px;
            }
            
            QGroupBox::indicator:unchecked:hover,
            QGroupBox::indicator:unchecked:focus,
            QGroupBox::indicator:unchecked:pressed {
                border: none;
                image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);
            }
            
            QGroupBox::indicator:checked:hover,
            QGroupBox::indicator:checked:focus,
            QGroupBox::indicator:checked:pressed {
                border: none;
                image: url(:/qss_icons/rc/checkbox_checked_focus.png);
            }
            
            QGroupBox::indicator:checked:disabled {
                image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
            }
            
            QGroupBox::indicator:unchecked:disabled {
                image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
            }
            
            /* QRadioButton ----------------------------------------------------------- */
            
            QRadioButton {
                background-color: #232629;
                color: #EFF0F1;
                spacing: 0;
                padding: 0;
                border: none;
                outline: none;
            }
            
            QRadioButton:focus {
                border: none;
            }
            
            QRadioButton:disabled {
                background-color: #232629;
                color: #4D545B;
                border: none;
                outline: none;
            }
            
            QRadioButton QWidget {
                background-color: #232629;
                color: #EFF0F1;
                spacing: 0px;
                padding: 0px;
                outline: none;
                border: none;
            }
            
            QRadioButton::indicator {
                border: none;
                outline: none;
                margin-bottom: 2px;
                width: 25px;
                height: 25px;
            }
            
            QRadioButton::indicator:unchecked {
                image: url(:/qss_icons/rc/radio_unchecked.png);
            }
            
            QRadioButton::indicator:unchecked:hover,
            QRadioButton::indicator:unchecked:focus,
            QRadioButton::indicator:unchecked:pressed {
                border: none;
                outline: none;
                image: url(:/qss_icons/rc/radio_unchecked_focus.png);
            }
            
            QRadioButton::indicator:checked {
                border: none;
                outline: none;
                image: url(:/qss_icons/rc/radio_checked.png);
            }
            
            QRadioButton::indicator:checked:hover,
            QRadioButton::indicator:checked:focus,
            QRadioButton::indicator:checked:pressed {
                border: none;
                outline: none;
                image: url(:/qss_icons/rc/radio_checked_focus.png);
            }
            
            QRadioButton::indicator:checked:disabled {
                outline: none;
                image: url(:/qss_icons/rc/radio_checked_disabled.png);
            }
            
            QRadioButton::indicator:unchecked:disabled {
                image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
            }
            
            /* QMenuBar --------------------------------------------------------------- */
            
            QMenuBar {
                background-color: #31363b;
                padding: 2px;
                border: 1px solid #232629;
                color: #EFF0F1;
            }
            
            QMenuBar:focus {
                border: 1px solid #179AE0;
            }
            
            QMenuBar::item {
                background: transparent;
                padding: 4px;
            }
            
            QMenuBar::item:selected {
                padding: 4px;
                background: transparent;
                border: 0px solid #31363B;
            }
            
            QMenuBar::item:pressed {
                padding: 4px;
                border: 0px solid #31363B;
                background-color: #179AE0;
                color: #EFF0F1;
                margin-bottom: 0px;
                padding-bottom: 0px;
            }
            
            /* QMenu ------------------------------------------------------------------ */
            
            QMenu {
                border: 0px solid #31363B;
                color: #EFF0F1;
                margin: 0px;
            }
            
            QMenu::separator {
                height: 2px;
                background-color: #31363B;
                color: #A9A9A9;
                padding-left: 4px;
                margin-left: 2px;
                margin-right: 2px;
            }
            
            QMenu::icon {
                margin: 0px;
                padding-left:4px;
            }
            
            QMenu::item {
                padding: 4px 24px 4px 24px;
                border: 1px transparent #31363B;  /* reserve space for selection border */
            }
            
            QMenu::item:selected {
                color: #EFF0F1;
            }
            
            
            
            QMenu::indicator {
                width: 12px;
                height: 12px;
                padding-left:6px;
            }
            
            /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */
            
            QMenu::indicator:non-exclusive:unchecked {
                image: url(:/qss_icons/rc/checkbox_unchecked.png);
            }
            
            QMenu::indicator:non-exclusive:unchecked:selected {
                image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
            }
            
            QMenu::indicator:non-exclusive:checked {
                image: url(:/qss_icons/rc/checkbox_checked.png);
            }
            
            QMenu::indicator:non-exclusive:checked:selected {
                image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
            }
            
            /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
            
            QMenu::indicator:exclusive:unchecked {
                image: url(:/qss_icons/rc/radio_unchecked.png);
            }
            
            QMenu::indicator:exclusive:unchecked:selected {
                image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
            }
            
            QMenu::indicator:exclusive:checked {
                image: url(:/qss_icons/rc/radio_checked.png);
            }
            
            QMenu::indicator:exclusive:checked:selected {
                image: url(:/qss_icons/rc/radio_checked_disabled.png);
            }
            
            QMenu::right-arrow {
                margin: 5px;
                image: url(:/qss_icons/rc/right_arrow.png)
            }
            
            /* QAbstractItemView ------------------------------------------------------ */
            
            QAbstractItemView {
                alternate-background-color: #232629;
                color: #EFF0F1;
                border: 1px solid #31363B;
                border-radius: 4px;
            }
            
            QAbstractItemView QLineEdit {
                padding: 2px;
            }
            
            /* QAbstractScrollArea ---------------------------------------------------- */
            
            QAbstractScrollArea {
                background-color: #232629;
                border: 1px solid #31363B;
                border-radius: 4px;
                padding: 4px;
                color: #EFF0F1;
            }
            
            QAbstractScrollArea:disabled {
                color: #4D545B;
            }
            
            /* QScrollArea ------------------------------------------------------------ */
            
            QScrollArea QWidget QWidget:disabled {
                background-color: #232629;
            }
            
            /* QScrollBar ------------------------------------------------------------- */
            
            QScrollBar:horizontal {
                height: 16px;
                margin: 2px 16px 2px 16px;
                border: 1px solid #31363B;
                border-radius: 4px;
                background-color: #232629;
            }
            
            QScrollBar::handle:horizontal {
                background-color: #4D545B;
                border: 1px solid #31363B;
                border-radius: 4px;
                min-width: 8px;
            
            }
            
            QScrollBar::handle:horizontal:hover {
                background-color: #179AE0;
                border: 1px solid #179AE0;
                border-radius: 4px;
                min-width: 8px;
            }
            
            QScrollBar::add-line:horizontal {
                margin: 0px 0px 0px 0px;
                border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
                width: 10px;
                height: 10px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:horizontal {
                margin: 0px 3px 0px 3px;
                border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
                height: 10px;
                width: 10px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:horizontal:hover,
            QScrollBar::add-line:horizontal:on {
                border-image: url(:/qss_icons/rc/right_arrow.png);
                height: 10px;
                width: 10px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:horizontal:hover,
            QScrollBar::sub-line:horizontal:on {
                border-image: url(:/qss_icons/rc/left_arrow.png);
                height: 10px;
                width: 10px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
            
            QScrollBar::up-arrow:horizontal,
            QScrollBar::down-arrow:horizontal {
                background: none;
            }
            
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
            }
            
            QScrollBar:vertical {
                background-color: #232629;
                width: 16px;
                margin: 16px 2px 16px 2px;
                border: 1px solid #31363B;
                border-radius: 4px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #4D545B;
                border: 1px solid #31363B;
                min-height: 8px;
                border-radius: 4px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #179AE0;
                border: 1px solid #179AE0;
                border-radius: 4px;
                min-height: 8px;
            
            }
            
            QScrollBar::sub-line:vertical {
                margin: 3px 0px 3px 0px;
                border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
                height: 10px;
                width: 10px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:vertical {
                margin: 3px 0px 3px 0px;
                border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
                height: 10px;
                width: 10px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:vertical:hover,
            QScrollBar::sub-line:vertical:on {
                border-image: url(:/qss_icons/rc/up_arrow.png);
                height: 10px;
                width: 10px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:vertical:hover,
            QScrollBar::add-line:vertical:on {
                border-image: url(:/qss_icons/rc/down_arrow.png);
                height: 10px;
                width: 10px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }
            
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
            
            /* QTextEdit--------------------------------------------------------------- */
            
            QTextEdit {
                background-color: #232629;
                color: #EFF0F1;
                border: 1px solid #31363B;
            }
            
            QTextEdit:hover {
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QTextEdit:selected {
                background: #3375A3;
                color: #31363B;
            }
            
            /* QPlainTextEdit --------------------------------------------------------- */
            
            QPlainTextEdit {
                background-color: #232629;
                color: #EFF0F1;
                border-radius: 4px;
                border: 1px solid #31363B;
            }
            
            QPlainTextEdit:hover {
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QPlainTextEdit:selected {
                background: #3375A3;
                color: #31363B;
            }
            
            /* QSizeGrip --------------------------------------------------------------- */
            
            QSizeGrip {
                image: url(:/qss_icons/rc/sizegrip.png);
                width: 12px;
                height: 12px;
            }
            
            /* QStackedWidget --------------------------------------------------------- */
            
            QStackedWidget {
                padding: 4px;
                border: 1px solid #31363B;
                border: 1px solid #232629;
            }
            
            /* QToolBar --------------------------------------------------------------- */
            
            QToolBar {
                background-color: #31363B;
                border-bottom: 1px solid #232629;
                padding: 2px;
                font-weight: bold;
            }
            
            QToolBar::handle:horizontal {
                width: 6px;
                image: url(:/qss_icons/rc/Hmovetoolbar.png);
            }
            
            QToolBar::handle:vertical {
                height: 6px;
                image: url(:/qss_icons/rc/Vmovetoolbar.png);
            }
            
            QToolBar::separator:horizontal {
                width: 3px;
                image: url(:/qss_icons/rc/Hsepartoolbar.png);
            }
            
            QToolBar::separator:vertical {
                height: 3px;
                image: url(:/qss_icons/rc/Vsepartoolbar.png);
            }
            
            QToolButton#qt_toolbar_ext_button {
                background: #31363B;
                border: 0px;
                color: #EFF0F1;
                image: url(:/qss_icons/rc/right_arrow.png);
            }
            
            /* QAbstractSpinBox ------------------------------------------------------- */
            
            QAbstractSpinBox {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                padding-top: 2px;     /* This fix  103, 111*/
                padding-bottom: 2px;  /* This fix  103, 111*/
                padding-left: 4px;
                padding-right: 4px;
                border-radius: 4px;
                /* min-width: 5px; removed to fix 109 */
            }
            
            QAbstractSpinBox:up-button {
                background-color: transparent #232629;
                subcontrol-origin: border;
                subcontrol-position: top right;
                border-left: 1px solid #31363B;
                margin: 1px;
            }
            
            QAbstractSpinBox::up-arrow,
            QAbstractSpinBox::up-arrow:disabled,
            QAbstractSpinBox::up-arrow:off {
                image: url(:/qss_icons/rc/up_arrow_disabled.png);
                width: 9px;
                height: 9px;
            }
            
            QAbstractSpinBox::up-arrow:hover {
                image: url(:/qss_icons/rc/up_arrow.png);
            }
            
            QAbstractSpinBox:down-button {
                background-color: transparent #232629;
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                border-left: 1px solid #31363B;
                margin: 1px;
            }
            
            QAbstractSpinBox::down-arrow,
            QAbstractSpinBox::down-arrow:disabled,
            QAbstractSpinBox::down-arrow:off {
                image: url(:/qss_icons/rc/down_arrow_disabled.png);
                width: 9px;
                height: 9px;
            }
            
            QAbstractSpinBox::down-arrow:hover {
                image: url(:/qss_icons/rc/down_arrow.png);
            }
            
            QAbstractSpinBox:hover{
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QAbstractSpinBox:selected {
                background: #3375A3;
                color: #31363B;
            }
            
            /* ------------------------------------------------------------------------ */
            /* DISPLAYS --------------------------------------------------------------- */
            /* ------------------------------------------------------------------------ */
            
            /* QLabel ----------------------------------------------------------------- */
            
            QLabel {
                background-color: #232629;
                border: 0px solid #31363B;
                padding: 2px;
                margin: 0px;
                color: #EFF0F1
            }
            
            QLabel::disabled {
                background-color: #232629;
                border: 0px solid #31363B;
                color: #4D545B;
            }
            
            /* QTextBrowser ----------------------------------------------------------- */
            
            QTextBrowser {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-radius: 4px;
            }
            
            QTextBrowser:disabled {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #4D545B;
                border-radius: 4px;
            }
            
            QTextBrowser:hover,
            QTextBrowser:!hover,
            QTextBrowser::selected,
            QTextBrowser::pressed {
                border: 1px solid #31363B;
            }
            
            /* QGraphicsView --------------------------------------------------------- */
            
            QGraphicsView {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-radius: 4px;
            }
            
            QGraphicsView:disabled {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #4D545B;
                border-radius: 4px;
            }
            
            QGraphicsView:hover,
            QGraphicsView:!hover,
            QGraphicsView::selected,
            QGraphicsView::pressed {
                border: 1px solid #31363B;
            }
            
            /* QCalendarWidget -------------------------------------------------------- */
            
            QCalendarWidget {
                border: 1px solid #31363B;
                border-radius: 4px;
            }
            
            QCalendarWidget:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            /* QLCDNumber ------------------------------------------------------------- */
            
            QLCDNumber {
                background-color: #232629;
                color: #EFF0F1;
            }
            
            QLCDNumber:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            /* QProgressBar ----------------------------------------------------------- */
            
            QProgressBar {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-radius: 4px;
                text-align: center;
            }
            
            QProgressBar:disabled {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #4D545B;
                border-radius: 4px;
                text-align: center;
            }
            
            QProgressBar::chunk {
                background-color: #3375A3;
                color: #232629;
                border-radius: 4px;
            }
            
            QProgressBar::chunk:disabled {
                background-color: #18465D;
                color: #4D545B;
                border-radius: 4px;
            }
            
            
            /* ------------------------------------------------------------------------ */
            /* BUTTONS ---------------------------------------------------------------- */
            /* ------------------------------------------------------------------------ */
            
            /* QPushButton ------------------------------------------------------------ */
            
            QPushButton {
                background-color: #4D545B;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-radius: 4px;
                padding: 3px;
                outline: none;
            }
            
            QPushButton:disabled {
                background-color: #31363B;
                border: 1px solid #31363B;
                color: #4D545B;
                border-radius: 4px;
                padding: 3px;
            }
            
            
            QPushButton:checked {
                background-color: #31363B;
                border: 1px solid #31363B;
                border-radius: 4px;
                padding: 3px;
                outline: none;
            }
            
            QPushButton:checked:disabled {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #4D545B;
                border-radius: 4px;
                padding: 3px;
                outline: none;
            }
            
            QPushButton::menu-indicator {
                subcontrol-origin: padding;
                subcontrol-position: bottom right;
                bottom: 4px;
            }
            
            QPushButton:pressed {
                background-color: #232629;
                border: 1px solid #232629;
            }
            
            QPushButton:hover,
            QPushButton:checked:hover{
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QPushButton:selected,
            QPushButton:checked:selected{
                background: #3375A3;
                color: #31363B;
            }
            
            /* QToolButton ------------------------------------------------------------ */
            
            QToolButton {
                background-color: #31363B;
                border: 1px solid #31363B;
                border-radius: 4px;
                margin: 0px;
                padding: 2px;
            }
            
            QToolButton:checked {
                background-color: #232629;
                border: 1px solid #232629;
            }
            
            QToolButton:disabled {
                background-color: #31363B;
            }
            
            QToolButton:hover,
            QToolButton:checked:hover{
                border: 1px solid #179AE0;
            }
            
            /* the subcontrols below are used only in the MenuButtonPopup mode */
            
            QToolButton[popupMode="1"] {
                padding-right: 12px;     /* only for MenuButtonPopup */
                border: 1px #31363B;   /* make way for the popup button */
                border-radius: 4px;
            }
            
            /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */
            
            QToolButton[popupMode="2"] {
                padding-right: 12px;      /* only for InstantPopup */
                border: 1px #A9A9A9;    /* make way for the popup button */
            }
            
            QToolButton::menu-button {
                border-radius: 4px;
                border: 1px transparent #31363B;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
                /* 16px width + 4px for border = 20px allocated above */
                width: 16px;
                outline: none;
            }
            
            QToolButton::menu-button:hover,
            QToolButton::menu-button:checked:hover {
                border: 1px solid #179AE0;
            }
            
            QToolButton::menu-indicator {
                image: url(:/qss_icons/rc/down_arrow.png);
                top: -8px;     /* shift it a bit */
                left: -4px;    /* shift it a bit */
            }
            
            QToolButton::menu-arrow {
                image: url(:/qss_icons/rc/down_arrow.png);
            }
            
            QToolButton::menu-arrow:open {
                border: 1px solid #31363B;
            }
            
            /* QCommandLinkButton ----------------------------------------------------- */
            
            QCommandLinkButton {
                background-color: #31363B;
                border: 1px solid #31363B;
                border-radius: 4px;
                padding: 0px;
                margin:0px;
            }
            
            /* ------------------------------------------------------------------------ */
            /* INPUTS - NO FIELDS ----------------------------------------------------- */
            /* ------------------------------------------------------------------------ */
            
            /* QCombobox -------------------------------------------------------------- */
            
            QComboBox {
                border: 1px solid #31363B;
                border-radius: 4px;
                selection-background-color: #3375A3;
                padding-top: 2px;     /* This fix  #103, #111*/
                padding-bottom: 2px;  /* This fix  #103, #111*/
                padding-left: 4px;
                padding-right: 4px;
                /* min-width: 75px;  removed to fix 109 */
            }
            
            QComboBox:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            QComboBox:hover{
                border: 1px solid #179AE0;
            }
            
            QComboBox:on {
                selection-background-color: #232629;
            }
            
            QComboBox QAbstractItemView {
                background-color: #232629;
                border-radius: 4px;
                border: 1px solid #31363B;
                selection-color: #179AE0;
                selection-background-color: #31363B;
            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 0px;
                border-left-color: #31363B;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            
            QComboBox::down-arrow {
                image: url(:/qss_icons/rc/down_arrow_disabled.png);
            }
            
            QComboBox::down-arrow:on,
            QComboBox::down-arrow:hover,
            QComboBox::down-arrow:focus {
                image: url(:/qss_icons/rc/down_arrow.png);
            }
            
            /* QSlider ---------------------------------------------------------------- */
            
            QSlider:disabled {
                background: #232629;
            }
            
            QSlider:focus {
                border: none;
            }
            
            QSlider::groove:horizontal {
                background: #4D545B;
                border: 1px solid #31363B;
                height: 4px;
                margin: 0px;
                border-radius: 4px;
            }
            
            QSlider::sub-page:horizontal {
                background: #3375A3;
                border: 1px solid #31363B;
                height: 4px;
                margin: 0px;
                border-radius: 4px;
            }
            
            QSlider::sub-page:horizontal:disabled {
                background: #18465D;
            }
            
            QSlider::handle:horizontal {
                background: #4D545B;
                border: 1px solid #31363B;
                width: 8px;
                height: 8px;
                margin: -8px 0;
                border-radius: 4px;
            }
            
            QSlider::handle:horizontal:hover {
                background: #179AE0;
                border: 1px solid #179AE0;
            }
            
            QSlider::groove:vertical {
                background: #31363B;
                border: 1px solid #31363B;
                width: 4px;
                margin: 0px;
                border-radius: 4px;
            }
            
            QSlider::sub-page:vertical {
                background: #3375A3;
                border: 1px solid #31363B;
                width: 4px;
                margin: 0px;
                border-radius: 4px;
            }
            
            QSlider::sub-page:vertical:disabled {
                background: #18465D;
            }
            
            QSlider::handle:vertical {
                background: #4D545B;
                border: 1px solid #31363B;
                width: 8px;
                height: 8px;
                margin: 0 -8px;
                border-radius: 4px;
            }
            
            QSlider::handle:vertical:hover {
                background: #179AE0;
                border: 1px solid #179AE0;
            }
            
            /* QLine ------------------------------------------------------------------ */
            
            QLineEdit {
                background-color: #232629;
                padding-top: 2px;     /* This QLineEdit fix  103, 111 */
                padding-bottom: 2px;  /* This QLineEdit fix  103, 111 */
                padding-left: 4px;
                padding-right: 4px;
                border-style: solid;
                border: 1px solid #31363B;
                border-radius: 4px;
                color: #EFF0F1;
            }
            
            QLineEdit:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            QLineEdit:hover{
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QLineEdit:selected{
                background: #3375A3;
                color: #31363B;
            }
            
            /* QTabWiget -------------------------------------------------------------- */
            
            QTabWidget {
                padding: 2px;
                border: 1px solid #31363B;
                selection-background-color: #31363B;
            }
            
            QTabWidget::focus QWidget{
                border: none;
            }
            
            QTabWidget::pane {
                border: 1px solid #31363B;
                padding: 2px;
                margin: 0px;
            }
            
            
            QTabWidget:selected {
                background-color: #31363B;
                border: 1px solid #31363B;
            }
            
            
            QTabWidget:focus {
                border: none;
            }
            
            /* QTabBar ---------------------------------------------------------------- */
            
            QTabBar {
                qproperty-drawBase: 0;
                border-radius: 4px;
                border: 0px solid #31363B;
                /* left: 5px; move to the right by 5px - removed for fix */
                }
            
            
            QTabBar::close-button {
                border-radius: 4px;
                border: none;
                padding: 4px;
                image: url(:/qss_icons/rc/close.png);
                background: transparent;
            }
            
            QTabBar::close-button:hover {
                border-radius: 4px;
                border: none;
                padding: 5px;
                image: url(:/qss_icons/rc/close-hover.png);
                background: transparent;
            }
            
            QTabBar::close-button:pressed {
                border-radius: 4px;
                border: none;
                padding: 4px;
                image: url(:/qss_icons/rc/close-pressed.png);
                background: transparent;
            }
            
            
            QTabBar::tab:top:selected:disabled {
                border-bottom: 2px solid #18465D;
                color: #4D545B;
                background-color: #31363B;
            }
            
            QTabBar::tab:bottom:selected:disabled {
                border-top: 2px solid #18465D;
                color: #4D545B;
                background-color: #31363B;
            }
            
            QTabBar::tab:left:selected:disabled {
                border-left: 2px solid #18465D;
                color: #4D545B;
                background-color: #31363B;
            }
            
            QTabBar::tab:right:selected:disabled {
                border-right: 2px solid #18465D;
                color: #4D545B;
                background-color: #31363B;
            }
            
            QTabBar::tab:top:!selected:disabled {
                border-bottom: 2px solid #31363B;
                color: #4D545B;
            }
            
            QTabBar::tab:bottom:!selected:disabled {
                border-top: 2px solid #31363B;
                color: #4D545B;
            }
            
            QTabBar::tab:left:!selected:disabled {
                border-left: 2px solid #31363B;
                color: #4D545B;
            }
            
            QTabBar::tab:right:!selected:disabled {
                border-right: 2px solid #31363B;
                color: #4D545B;
            }
            
            QTabBar::tab:top:!selected {
                border-bottom: 2px solid #31363B;
            }
            
            QTabBar::tab:bottom:!selected {
                border-top: 2px solid #31363B;
            }
            
            QTabBar::tab:left:!selected {
                border-left: 2px solid #31363B;
            }
            
            QTabBar::tab:right:!selected {
                border-right: 2px solid #31363B;
            }
            
            QTabBar::tab:top {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                padding: 2px;
                padding-left: 4px;
                padding-right: 4px;
                min-width: 5px;
                border-bottom: 1px solid #31363B;
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
            }
            
            QTabBar::tab:top:selected {
                background-color: #4D545B;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-bottom: 2px solid #3375A3;
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
            }
            
            QTabBar::tab:top:!selected:hover {
                border: 1px solid #179AE0;
            }
            
            QTabBar::tab:bottom {
                color: #EFF0F1;
                border: 1px solid #31363B;
                border-top: 1px solid #31363B;
                background-color: #232629;
                padding: 2px;
                padding-left: 4px;
                padding-right: 4px;
                border-bottom-left-radius: 3px;
                border-bottom-right-radius: 3px;
                min-width: 5px;
            }
            
            QTabBar::tab:bottom:selected {
                color: #EFF0F1;
                background-color: #4D545B;
                border: 1px solid #31363B;
                border-top: 2px solid #3375A3;
                border-bottom-left-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            
            QTabBar::tab:bottom:!selected:hover {
                border: 1px solid #179AE0;
            }
            
            QTabBar::tab:left {
                color: #EFF0F1;
                border: 1px solid #31363B;
                border-left: 1px solid #31363B;
                background-color: #232629;
                padding: 2px;
                padding-top: 4px;
                padding-bottom: 4px;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
                min-height: 5px;
            }
            
            QTabBar::tab:left:selected {
                color: #EFF0F1;
                background-color: #4D545B;
                border: 1px solid #31363B;
                border-left: 2px solid #3375A3;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            
            QTabBar::tab:left:!selected:hover {
                border: 1px solid #179AE0;
            }
            
            QTabBar::tab:right {
                color: #EFF0F1;
                border: 1px solid #31363B;
                border-right: 1px solid #31363B;
                background-color: #232629;
                padding: 2px;
                padding-top: 4px;
                padding-bottom: 4px;
                border-top-left-radius: 3px;
                border-bottom-left-radius: 3px;
                min-height: 5px;
            }
            
            QTabBar::tab:right:selected {
                color: #EFF0F1;
                background-color: #4D545B;
                border: 1px solid #31363B;
                border-right: 2px solid #3375A3;
                border-top-left-radius: 3px;
                border-bottom-left-radius: 3px;
            }
            
            QTabBar::tab:right:!selected:hover {
                border: 1px solid #179AE0;
            }
            
            QTabBar QToolButton::right-arrow:enabled {
                image: url(:/qss_icons/rc/right_arrow.png);
            }
            
            QTabBar QToolButton::left-arrow:enabled {
                image: url(:/qss_icons/rc/left_arrow.png);
            }
            
            QTabBar QToolButton::right-arrow:disabled {
                image: url(:/qss_icons/rc/right_arrow_disabled.png);
            }
            
            QTabBar QToolButton::left-arrow:disabled {
                image: url(:/qss_icons/rc/left_arrow_disabled.png);
            }
            
            
            /*  Some examples from internet to check
            
            QTabBar::tabButton() and QTabBar::tabIcon()
            QTabBar::tear {width: 0px; border: none;}
            QTabBar::tear {image: url(tear_indicator.png);}
            QTabBar::scroller{width:85pix;}
            QTabBar QToolbutton{background-color:"light blue";}
            
            But that left the buttons transparant.
            Looked confusing as the tab buttons migrated behind the scroller buttons.
            So we had to color the back ground of the scroller buttons
            */
            
            /* QDockWiget ------------------------------------------------------------- */
            
            QDockWidget {
                outline: 1px solid #31363B;
                background-color: #232629;
                border: 1px solid #31363B;
                border-radius: 4px;
                titlebar-close-icon: url(:/qss_icons/rc/close.png);
                titlebar-normal-icon: url(:/qss_icons/rc/undock.png);
            }
            
            QDockWidget::title {
                padding: 6px;   /* better size for title bar */
                border: none;
                background-color: #31363B;
            }
            
            QDockWidget::close-button {
                background-color: #31363B;
                border-radius: 4px;
                border: none;
            }
            
            QDockWidget::close-button:hover {
                border: 1px solid #31363B;
            }
            
            QDockWidget::close-button:pressed {
                border: 1px solid #31363B;
            }
            
            QDockWidget::float-button {
                background-color: #31363B;
                border-radius: 4px;
                border: none;
            }
            
            QDockWidget::float-button:hover {
                border: 1px solid #31363B;
            }
            
            QDockWidget::float-button:pressed {
                border: 1px solid #31363B;
            }
            
            /* QTreeView QTableView QListView ----------------------------------------- */
            
            QTreeView:branch:selected,
            QTreeView:branch:hover {
                background: url(:/qss_icons/rc/transparent.png);
            }
            
            QTreeView::branch:has-siblings:!adjoins-item {
                border-image: url(:/qss_icons/rc/transparent.png);
            }
            
            QTreeView::branch:has-siblings:adjoins-item {
                border-image: url(:/qss_icons/rc/transparent.png);
            }
            
            QTreeView::branch:!has-children:!has-siblings:adjoins-item {
                border-image: url(:/qss_icons/rc/transparent.png);
            }
            
            QTreeView::branch:has-children:!has-siblings:closed,
            QTreeView::branch:closed:has-children:has-siblings {
                image: url(:/qss_icons/rc/branch_closed.png);
            }
            
            QTreeView::branch:open:has-children:!has-siblings,
            QTreeView::branch:open:has-children:has-siblings {
                image: url(:/qss_icons/rc/branch_open.png);
            }
            
            QTreeView::branch:has-children:!has-siblings:closed:hover,
            QTreeView::branch:closed:has-children:has-siblings:hover {
                image: url(:/qss_icons/rc/branch_closed-on.png);
            }
            
            QTreeView::branch:open:has-children:!has-siblings:hover,
            QTreeView::branch:open:has-children:has-siblings:hover {
                image: url(:/qss_icons/rc/branch_open-on.png);
            }
            
            QListView::item:!selected:hover,
            QTreeView::item:!selected:hover,
            QTableView::item:!selected:hover,
            QColumnView::item:!selected:hover {
                outline: 0;
                color: #179AE0;
                background-color: #31363B;
            }
            
            QListView::item:selected:hover,
            QTreeView::item:selected:hover,
            QTableView::item:selected:hover,
            QColumnView::item:selected:hover {
                background: #3375A3;
                color:  #232629;
            }
            
            QTreeView::indicator:checked,
            QListView::indicator:checked {
                image: url(:/qss_icons/rc/checkbox_checked.png);
            }
            
            QTreeView::indicator:unchecked,
            QListView::indicator:unchecked {
                image: url(:/qss_icons/rc/checkbox_unchecked.png);
            }
            
            QTreeView::indicator:checked:hover,
            QTreeView::indicator:checked:focus,
            QTreeView::indicator:checked:pressed,
            QListView::indicator:checked:hover,
            QListView::indicator:checked:focus,
            QListView::indicator:checked:pressed {
                image: url(:/qss_icons/rc/checkbox_checked_focus.png);
            }
            
            QTreeView::indicator:unchecked:hover,
            QTreeView::indicator:unchecked:focus,
            QTreeView::indicator:unchecked:pressed,
            QListView::indicator:unchecked:hover,
            QListView::indicator:unchecked:focus,
            QListView::indicator:unchecked:pressed {
                image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);
            }
            
            QTreeView::indicator:indeterminate:hover,
            QTreeView::indicator:indeterminate:focus,
            QTreeView::indicator:indeterminate:pressed,
            QListView::indicator:indeterminate:hover,
            QListView::indicator:indeterminate:focus,
            QListView::indicator:indeterminate:pressed {
                image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);
            }
            
            QTreeView::indicator:indeterminate,
            QListView::indicator:indeterminate {
                image: url(:/qss_icons/rc/checkbox_indeterminate.png);
            }
            
            QListView,
            QTreeView,
            QTableView,
            QColumnView {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                gridline-color: #31363b;
                border-radius: 4px;
            }
            
            QListView:disabled,
            QTreeView:disabled,
            QTableView:disabled,
            QColumnView:disabled {
                background-color: #232629;
                color: #4D545B;
            }
            
            QListView:selected,
            QTreeView:selected,
            QTableView:selected,
            QColumnView:selected {
                background: #3375A3;
                color: #31363B;
            }
            
            QListView:hover,
            QTreeView::hover,
            QTableView::hover,
            QColumnView::hover {
                background-color: #232629;
                border: 1px solid #179AE0;
            }
            
            QListView::item:pressed,
            QTreeView::item:pressed,
            QTableView::item:pressed,
            QColumnView::item:pressed {
                background-color: #3375A3;
            }
            
            QListView::item:selected:active,
            QTreeView::item:selected:active,
            QTableView::item:selected:active,
            QColumnView::item:selected:active {
                background-color: #3375A3;
            }
            
            QTableCornerButton::section {
                background-color: #232629;
                border: 1px transparent #31363B;
                border-radius: 0px;
            }
            
            /* QHeaderView ------------------------------------------------------------ */
            
            QHeaderView {
                background-color: #31363B;
                border: 0px transparent #31363B;
                padding: 0px;
                margin: 0px;
                border-radius: 0px;
            }
            
            QHeaderView:disabled {
                background-color: #31363B;
                border: 1px transparent #31363B;
                padding: 2px;
            }
            
            QHeaderView::section {
                background-color: #31363B;
                color: #EFF0F1;
                padding: 2px;
                border-radius: 0px;
                text-align: left;
            }
            
            QHeaderView::section:checked {
                color: #EFF0F1;
                background-color: #3375A3;
            }
            
            QHeaderView::section:checked:disabled {
                color: #4D545B;
                background-color: #18465D;
            }
            
            QHeaderView::section::horizontal:disabled,
            QHeaderView::section::vertical:disabled {
                color: #4D545B;
            }
            
            QHeaderView::section::vertical::first,
            QHeaderView::section::vertical::only-one {
                border-top: 1px solid #31363B;
            }
            
            QHeaderView::section::vertical {
                border-top: 1px solid #232629;
            }
            
            QHeaderView::section::horizontal::first,
            QHeaderView::section::horizontal::only-one {
                border-left: 1px solid #31363B;
            }
            
            QHeaderView::section::horizontal {
                border-left: 1px solid #232629;
            }
            
            /* Those settings (border/width/height/background-color) solve bug */
            /* transparent arrow background and size */
            
            QHeaderView::down-arrow {
                background-color: #31363B;
                width: 16px;
                height: 16px;
                border-right: 1px solid #232629;
                image: url(:/qss_icons/rc/down_arrow.png);
            }
            
            QHeaderView::up-arrow {
                background-color: #31363B;
                width: 16px;
                height: 16px;
                border-right: 1px solid #232629;
                image: url(:/qss_icons/rc/up_arrow.png);
            }
            
            /* QToolBox -------------------------------------------------------------- */
            
            QToolBox {
                padding: 0px;
                border: 1px solid #31363B;
            }
            
            QToolBox::selected {
                padding: 0px;
                border: 1px solid #3375A3;
            }
            
            QToolBox::tab {
                background-color: #232629;
                border: 1px solid #31363B;
                color: #EFF0F1;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            
            QToolBox::tab:disabled {
                color: #4D545B;
            }
            
            QToolBox::tab:selected {
                background-color: #31363B;
                border-bottom: 1px solid #3375A3;
            }
            
            QToolBox::tab:!selected {
                background-color: #31363B;
                border-bottom: 1px solid #232629;
            }
            
            QToolBox::tab:selected:disabled {
                border-bottom: 1px solid #18465D;
            }
            
            QToolBox::tab:hover {
                background-color: #179AE0;
                border-color: #179AE0;
                border-bottom: 1px solid #179AE0;
                color: #31363B;
            }
            
            QToolBox QScrollArea QWidget QWidget {
                padding: 0px;
                background-color: #232629;
            }
            
            /* QFrame ----------------------------------------------------------------- */
            
            QFrame {
                border-radius: 4px;
                border: 1px solid #31363B;
            }
            
            QFrame[frameShape="0"] {
                border-radius: 4px;
                border: 1px transparent #31363B;
            }
            
            QFrame[height="3"],
            QFrame[width="3"] {
                background-color: #232629;
            }
            
            /* QSplitter -------------------------------------------------------------- */
            
            QSplitter {
                background-color: #31363B;
                spacing: 0;
                padding: 0;
                margin: 0;
            }
            
            QSplitter::separator {
                background-color: #31363B;
                border: 0 solid #232629;
                spacing: 0;
                padding: 1px;
                margin: 0;
            }
            
            QSplitter::separator:hover {
                background-color: #4D545B;
            }
            
            QSplitter::separator:horizontal {
                width: 5px;
                image: url(:/qss_icons/rc/Vsepartoolbar.png);
            }
            
            QSplitter::separator:vertical {
                height: 5px;
                image: url(:/qss_icons/rc/Hsepartoolbar.png);
            }
            
            
            /* QDateEdit-------------------------------------------------------------- */
            
            QDateEdit {
                selection-background-color: #3375A3;
                border-style: solid;
                border: 1px solid #31363B;
                border-radius: 4px;
                padding-top: 2px;     /* This fix  #103, #111*/
                padding-bottom: 2px;  /* This fix  #103, #111*/
                padding-left: 4px;
                padding-right: 4px;
                min-width: 10px;
            }
            
            QDateEdit:on {
                selection-background-color: #3375A3;
            }
            
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            
            QDateEdit::down-arrow {
                image: url(:/qss_icons/rc/down_arrow_disabled.png);
            }
            
            QDateEdit::down-arrow:on,
            QDateEdit::down-arrow:hover,
            QDateEdit::down-arrow:focus {
                image: url(:/qss_icons/rc/down_arrow.png);
            }
            
            QDateEdit QAbstractItemView {
                background-color: #232629;
                border-radius: 4px;
                border: 1px solid #31363B;
                selection-background-color: #3375A3;
            }
            
            QAbstractView:hover{
                border: 1px solid #179AE0;
                color: #EFF0F1;
            }
            
            QAbstractView:selected {
                background: #3375A3;
                color: #31363B;
            }
            
            

        """