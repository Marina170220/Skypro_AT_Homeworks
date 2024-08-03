from Lesson7.Calculator.Pages.Mainpage import CalcMain


def test_calculator(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.find_element()
    calcmain.click_buttons()
    assert "15" in calcmain.get_result()
    